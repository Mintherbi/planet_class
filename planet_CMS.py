import bpy
import random as rand 
from mathutils import Vector
#g =3.
#G = 6.6740831e-11

class Planet:
    def __init__(self, radius, location, velocity):
        bpy.ops.mesh.primitive_uv_sphere_add(radius = radius)
        self.object = bpy.context.active_object
        self.object.location = location
        self.velocity = velocity
        self.mass = 10**radius
        
    def update(self, acc, rate):
        self.velocity -= acc * rate
        self.location += self.velocity * rate


class system(Planet):
    def __init__(self, sys, frame_rate):
        self.system = sys
        self.frame_rate = frame_rate
        self.seconds_per_frame = 1 / frame_rate
        self.G = 6.6740831e-11

    def update(self):
        for i in self.system:
            acc = Vector((0,0,0))
            for j in self.system.pop(i):
                acc += self.acc(self.system[j])
            self.system[i].update(acc, self.seconds_per_frame)
    
    def acc(self, other_planet):
        direction = other_planet.object.location - self.object.location
        d_squared = direction.length_squared
        direction.normalize()
        acc = direction * (self.G * other_planet.mass/ d_squared) 
        return acc

orbit = []

for i in range(3):
    orbit.append(Planet(radius=rand.randrange(1,3), 
                     location=Vector((rand.randrange(-10,10),rand.randrange(-10,10),rand.randrange(-10,10))), 
                     velocity=Vector((rand.randrange(-1,1),rand.randrange(-1,1), rand.randrange(-1,1)))))

sys = system(orbit,1)

def n_bodies(scene):
    global sys
    sys.update()
    sys.system


#get rid of previously set frame_change_pre handlers (if not the same handler may be fired n times)
bpy.app.handlers.frame_change_pre.clear()
#install "two_bodies" as current handler
bpy.app.handlers.frame_change_pre.append(n_bodies)