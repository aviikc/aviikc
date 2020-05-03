from bpy.types import Panel


class MyFirstBlenderUI(Panel):
    """My Tooltip"""
    bl_idname = "MY_PT_panel"           #Warning: 'panel.panel1' doesn't contain '_PT_' with prefix & suffix
    bl_label = 'My First Ui Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My Panel3'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        # Draws A Text Label
        self.layout.row().label(text = "Hello Class")
        
        #Adding a Button
        row = layout.row()
        row.operator(text="Botton Text")
        
def register():
    from bpy.utils import register_class
    register_class(MyFirstBlenderUI)
    
def unregister():
    from bpy.utils import unregister_class
    unregister_class(MyFirstBlenderUI)
    
if __name__ == "__main__":
    register()