from bpy.types import Panel


class MyPanels(Panel):
    bl_idname      = "MY_PT_panel"
    bl_label       = "My Ui Panel"
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        
        self.layout.row().label(text = "Hello Class")
        self.layout.row().operator("mesh.primitive_cube_add")
        
def register():
    from bpy.utils import register_class
    register_class(MyPanels)
    
def unregister():
    from bpy.utils import unregister_class
    unregister_class(MyPanelss)
    
if __name__ == "__main__":
    register()