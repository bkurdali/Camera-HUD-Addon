bl_info = {
    "name": "Camera Hud",
    "author": "Bassam Kurdali",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "View3D",
    "description": "Not a HUD",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(camera_hud)
else:
    from . import camera_hud
    
import bpy

# Property updaters


def size_update(self, context):
    """ A bit of an ungainly solution to update gizmos on size change """
    camera_hud.gizmo_unregister()
    camera_hud.gizmo_register()


class HudPreferences(bpy.types.AddonPreferences):
    bl_idname = "camera_hud"

    size: bpy.props.FloatProperty(
        name="Size", default=0.3, min=0.1, max=2.0, update=size_update)
    display_scale: bpy.props.FloatProperty(
        name="Spacing", default=1.0, min=1.0, max=3.0)

    def draw(self, context):
        self.layout.prop(self, "size")
        self.layout.prop(self, "display_scale")


def register():
    bpy.utils.register_class(HudPreferences)
    camera_hud.register()


def unregister():
    bpy.utils.unregister_class(HudPreferences)
    camera_hud.unregister()

if __name__ == '__main__':
    register()
