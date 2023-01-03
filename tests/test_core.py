import bpy

from sandbox.core import add_gpencil


def test_add_gpencil():
    gpd_count = len(bpy.data.grease_pencils)
    obj = add_gpencil(bpy.context.scene, "GPencil")

    # A new grease pencil data block should have been created.
    assert len(bpy.data.grease_pencils) == gpd_count + 1
    # Object should be a GP object.
    assert obj.type == "GPENCIL"
    # Object should be linked in active scene.
    assert obj in bpy.context.scene.objects
