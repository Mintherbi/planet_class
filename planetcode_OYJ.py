import bpy
from mathutils import Vector

#cdfa
class Planet:
    def __init__(self, name, radius, mass, position, velocity):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.position = position
        self.velocity = velocity

def create_planet(planet):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=Slanet.radius)
    obj = bpy.context.active_object
    obj.location = planet.position
    obj.name = planet.name
    return obj

def n_body_system(scene):
    global planets, G

    for i, planet in enumerate(planets):
        acceleration = Vector((0, 0, 0))

        for j, other_planet in enumerate(planets):
            if i != j:
                direction = other_planet.position - planet.position
                distance_squared = direction.length_squared
                direction.normalize()
                acceleration += direction * (G * other_planet.mass / distance_squared)

        planet.velocity += acceleration
        planet.position += planet.velocity

        bpy.data.objects[planet.name].location = planet.position


G = 6.6740831e-11

planets = [
    Planet("Planet 1", 2, 1e+11, Vector((-5, 0, 0)), Vector((0, 0.01, 0))),
    Planet("Planet 2", 1, 1e+06, Vector((10, 0, 0)), Vector((0, -0.5, 0))),
    Planet("Planet 3", 1.5, 1e+02, Vector((0, 10, 0)), Vector((0, 0.01, 0)))
]

for planet in planets:
    create_planet(planet)

# Add handler for n-body system calculation
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(n_body_system)
