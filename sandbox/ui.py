import bpy


class SANDBOX_PT_SimplePanel(bpy.types.Panel):
    """Simple Panel."""

    bl_label = "Sandbox"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Debug"

    def draw(self, context: bpy.types.Context):
        self.layout.prop(context.window, "scene")


classes = (SANDBOX_PT_SimplePanel,)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
