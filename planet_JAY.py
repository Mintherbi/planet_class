import bpy
from mathutils import Vector
#g =3.
G = 6.6740831e-11

class planet():
    def __init__(self, radius, location, velocity, mass):
        bpy.ops.mesh.primitive_uv_sphere_add(radius = radius)
        self.object = bpy.context.active_object
        self.object.location = location
        self.velocity = Vector(velocity)
        self.mass = mass
        
    def calc_force(self, other_planet):
        direction = other_planet.object.location - self.object.location
        d_squared = direction.length_squared
        direction.normalize()
        acc = direction * (G * other_planet.mass/ d_squared) 
        return acc

    def update_velocity_and_location(self, acc, seconds_per_frame):
        self.velocity += acc * seconds_per_frame
        self.object.location += self.velocity * seconds_per_frame



####################################################################
# 우리의 gravity.py의 2-bodies에 적용해보자면...

# planet1 = planet(radius=2, location=(-5, 0, 0), velocity=( 0, 0.01, 0 ), mass=1e+11)
# planet2 = planet(radius=1, location=(10, 0, 0), velocity=( 0, -0.5, 0 ), mass=1e+05)

# #frame rate for calculation
# frame_rate = 1 #24 (normally 24 but 1 is faster)
# seconds_per_frame = 1 / frame_rate

# def two_bodies(scene):
#     global seconds_per_frame

#     force_1to2 = planet1.calc_force(planet2)
#     force_2to1 = -force_1to2

#     planet1.update_velocity_and_location(force_1to2, seconds_per_frame)
#     planet2.update_velocity_and_location(force_2to1, seconds_per_frame)

# #get rid of previously set frame_change_pre handlers (if not the same handler may be fired n times)
# bpy.app.handlers.frame_change_pre.clear()
# #install "two_bodies" as current handler
# bpy.app.handlers.frame_change_pre.append(two_bodies)



####################################################################
# 이번엔 3-bodies

planet1 = planet(radius=2, location=(-5, 0, 0), velocity=( 0, 0.01, 0 ), mass=1e+11)
planet2 = planet(radius=1, location=(10, 0, 0), velocity=( 0, -0.5, 0 ), mass=1e+05)
planet3 = planet(radius=3, location=(0, 20, 0), velocity=( 0, 0.05, 0 ), mass=1e+10)

#frame rate for calculation
frame_rate = 1 #24 (normally 24 but 1 is faster)
seconds_per_frame = 1 / frame_rate

def three_bodies(scene):
    global seconds_per_frame

    force_1to2 = planet1.calc_force(planet2)
    force_2to1 = -force_1to2
    force_1to3 = planet1.calc_force(planet3)
    force_3to1 = -force_1to3
    force_2to3 = planet2.calc_force(planet3)
    force_3to2 = -force_2to3

    force_1 = force_1to2 + force_1to3
    force_2 = force_2to1 + force_2to3
    force_3 = force_3to1 + force_3to2

    planet1.update_velocity_and_location(force_1, seconds_per_frame)
    planet2.update_velocity_and_location(force_2, seconds_per_frame)
    planet3.update_velocity_and_location(force_3, seconds_per_frame)

#get rid of previously set frame_change_pre handlers (if not the same handler may be fired n times)
bpy.app.handlers.frame_change_pre.clear()
#install "two_bodies" as current handler
bpy.app.handlers.frame_change_pre.append(three_bodies)