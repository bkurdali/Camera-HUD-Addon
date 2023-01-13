import bpy
from bpy.types import (
    GizmoGroup,
)

class Camera_Movements_UI_Buttons(GizmoGroup):
    bl_idname = "Camera_Movements_UI_Buttons"
    bl_label = "Camera Movements UI Buttons"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'PERSISTENT', 'SCALE'}

    @classmethod
    def poll(cls, context):
        ob = context.object
        return (ob and ob.type == 'CAMERA')

    def draw_prepare(self, context):
        region = context.region

        self.foo_gizmo.matrix_basis[0][3] = region.width - 40
        self.foo_gizmo.matrix_basis[1][3] = 40

    def setup(self, context):
        mpr = self.gizmos.new("GIZMO_GT_button_2d")   # This line crashes Blender
        mpr.icon = 'OUTLINER_OB_CAMERA'
        mpr.draw_options = {'BACKDROP', 'OUTLINE'}

        mpr.alpha = 0.0
        mpr.color_highlight = 0.8, 0.8, 0.8
        mpr.alpha_highlight = 0.2
        props = mpr.target_set_operator("transform.rotate")
        mpr.scale_basis = (80 * 0.35) / 2 # Same as buttons defined in C
        self.foo_gizmo = mpr


bpy.utils.register_class(Camera_Movements_UI_Buttons)
