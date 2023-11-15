import bpy
import planet

class N_bodyPanel(bpy.types.Panel, planet):
    bl_label = "Nbody Simulation"
    bl_idname = "PT_Nbody Simulation"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NeuSIM'

    def draw(self,context):
        layout = self.layout

        row = layout.row()
        row.label(text= "Add Planet", icon='CUBE')

    


def register():
    bpy.utils.register_class(N_bodyPanel)
    
def unregister():
    bpy.utils.unregister_class(N_bodyPanel)

if __name__=="__main__":
    register()
