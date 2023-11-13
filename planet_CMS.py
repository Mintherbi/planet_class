import bpy
import random as rand 
from mathutils import Vector
#g =3.
#G = 6.6740831e-11

class planet(bpy.ops.mesh):
    def __init__(self, radius, location, velocity):
        self.object = bpy.ops.mesh.primitive_uv_sphere_add(radius = radius)
        self.object.location = location
        self.velocity = velocity
        self.__mass = 10**radius
        
    def update(self, location, velocity):
        self.object.location = location
        self.velocity = velocity



class system(planet):
    def __init__(self, sys, frame_rate):
        self.system = sys
        self.frame_rate = frame_rate
        self.seconds_per_frame = 1 / frame_rate
        self.__G = 6.6740831e-11

    def update(self):
        for i in self.system:
            acc = Vector(0,0,0)
            for j in self.system.remove(i):
                acc =+ self.acc(j)
            i.velocity =- acc * self.seconds_per_frame
        return self.system
    
    def acc(self, other_planet):
        direction = other_planet.object.location - self.object.location
        d_squared = direction.length_squared
        direction.normalize()
        acc = direction * (self.G * other_planet.mass/ d_squared) 
        return acc



for i in range(5):
    orbit = []
    orbit.append(planet(radius=rand.randrange(1,3), 
                     location=Vector(rand.randrange(-10,10),rand.randrange(-10,10),rand.randrange(-10,10)), 
                     velocity=Vector(rand.randrange(-1,1),rand.randrange(-1,1), rand.randrange(-1,1))))

sys = system(orbit,1)

def n_bodies(scene):
    global sys

    planets = sys.update()

    planets


#get rid of previously set frame_change_pre handlers (if not the same handler may be fired n times)
bpy.app.handlers.frame_change_pre.clear()
#install "two_bodies" as current handler
bpy.app.handlers.frame_change_pre.append(n_bodies)