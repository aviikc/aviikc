import bpy


class TOPBAR_MT_custom_sub_menu(bpy.types.Menu):
    bl_label = "Sub Menu"

    def draw(self, context):
        layout = self.layout
        # layout.operator("mesh.primitive_cube_add")


class TOPBAR_MT_custom_menu(bpy.types.Menu):
    bl_label = "Custom Menu"

    def draw(self, context):
        layout = self.layout
        layout.menu("TOPBAR_MT_custom_sub_menu")

    def menu_draw(self, context):
        self.layout.menu("TOPBAR_MT_custom_menu")


classes = (TOPBAR_MT_custom_sub_menu, TOPBAR_MT_custom_menu)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_custom_menu.menu_draw)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_custom_menu.menu_draw)
    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()