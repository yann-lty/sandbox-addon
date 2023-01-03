from sandbox import ui


bl_info = {
    "name": "Sandbox",
    "author": "Yann Lanthony",
    "description": "Sanbox Addon",
    "blender": (3, 3, 0),
    "version": (0, 0, 1),
    "location": "View3D > Sidebar > Debug",
    "warning": "",
    "category": "Debug",
}


def register():
    print("[Sandbox] Register")
    print(f"[Sandbox] Now printing version {bl_info['version']}")
    print(f"[Sandbox] Made by {bl_info['author']}")
    ui.register()


def unregister():
    print("[Sandbox] Unregister")
    ui.unregister()
