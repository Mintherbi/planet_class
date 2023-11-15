import bpy
import random as rand
from mathutils import Vector

G = 6.6740831e-11
#new code
class Planet:
    def __init__(self, radius, location, velocity):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=radius)
        self.object = bpy.context.active_object
        self.object.location = location
        self.velocity = velocity
        self.mass = 1000**radius


class System:
    def __init__(self, sys=None, frame_rate=1):
        self.system = sys if sys else []
        self.frame_rate = frame_rate
        self.seconds_per_frame = 1 / frame_rate

    def update(self):
        for i in self.system:
            acc = Vector((0, 0, 0))
            for j in self.system:
                if i != j : 
                    direction = j.object.location - i.object.location
                    d_squared = direction.length_squared
                    direction.normalize()
                    acc_j = direction * (G * j.mass / d_squared)
                    acc += acc_j
            i.velocity += self.frame_rate * acc
            i.object.location += i.velocity * self.frame_rate
        return self.system


# Create a system with 5 planets
orbit = [Planet(radius=rand.randrange(2, 5),
                location=Vector((rand.randrange(-20, 20), rand.randrange(-20, 20), rand.randrange(-20, 20))),
                velocity=Vector((rand.random()*2-1, rand.random()*2-1, rand.random()*2-1)))
         for _ in range(3)]

sys = System(orbit, 1)

def n_bodies(scene):
    global sys
    sys.update()

# Clear previously set frame_change_pre handlers
bpy.app.handlers.frame_change_pre.clear()
# Install "n_bodies" as the current handler
bpy.app.handlers.frame_change_pre.append(n_bodies)