import bpy


def add_gpencil(scene: bpy.types.Scene, name: str) -> bpy.types.Object:
    """Add a new grease pencil object named `name` to `scene`."""
    gpd = bpy.data.grease_pencils.new(name)
    obj = bpy.data.objects.new(name, gpd)
    scene.collection.objects.link(obj)
    return obj
