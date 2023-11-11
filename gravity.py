import bpy
from mathutils import Vector

# !!! 

#get first object and arbitrary location
bpy.ops.mesh.primitive_uv_sphere_add(radius=2)
o1 = bpy.context.active_object
o1.location.x = -5

#same for second one
bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
o2 = bpy.context.active_object
o2.location.x = 10

#define constants: G and masses
G = 6.6740831e-11
m1 = 1e+11
m2 = 1e+05

#initial speeds
v1 = Vector( ( 0, 0.01, 0 ) )
v2 = Vector( ( 0, -0.5, 0 ) )

#frame rate for calculation
frame_rate = 1 #24 (normally 24 but 1 is faster)
seconds_per_frame = 1 / frame_rate

def two_bodies(scene):
    #import globals in the function scope
    global o1, o2, G, m1, m2, v1, v2
    global seconds_per_frame
    
    #calc current direction between the objects
    direction = o1.location - o2.location
    
    #calc the squared distance 
    d_squared = direction.length_squared
    #keep the direction of the strength
    direction.normalize()
    
    #calc new speed vectors
    v1 = v1 - (direction * (G * m2 / d_squared) * seconds_per_frame)
    v2 = v2 + (direction * (G * m1 / d_squared) * seconds_per_frame)
    
    #calc new locations
    o1.location += v1 * seconds_per_frame
    o2.location += v2 * seconds_per_frame

#get rid of previously set frame_change_pre handlers (if not the same handler may be fired n times)
bpy.app.handlers.frame_change_pre.clear()
#install "two_bodies" as current handler
bpy.app.handlers.frame_change_pre.append(two_bodies)