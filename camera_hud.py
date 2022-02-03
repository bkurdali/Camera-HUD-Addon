bl_info = {
    "name": "Camera Hud",
    "author": "Bassam Kurdali",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Not a HUD",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy
import bpy_extras
import mathutils
import math

from bpy_extras import view3d_utils


# Gizmo Triangle Coords

# Button
size = .3
custom_shape_verts = (
    (0, 0, 0), (size, size, 0), (size, 0, 0),
    (0, size, 0), (size, size, 0), (0, 0, 0),
    )
    
# Slider

width = size
thick = width / 10
height = size * 10
base_shape_verts = (    
    (0, 0, 0), (width, -thick, 0), (width, 0, 0),
    (0, -thick, 0), (width, -thick, 0), (0, 0, 0),

    (0, -height, 0), (width, -thick - height, 0), (width, -height, 0),
    (0, -thick - height, 0), (width, -thick - height, 0), (0, -height, 0),
    )
slider_shape_verts = (
    (0, -size/4, 0), (size, size/4, 0), (size, -size/4, 0),
    (0, size/4, 0), (size, size/4, 0), (0, -size/4, 0),
    )


class ButtonWidget(bpy.types.Gizmo):
    """ Custom 'button' gizmo for camera """
    bl_idname = "VIEW3D_GT_button_widget"

    def draw(self, context):
        self.draw_custom_shape(self.custom_shape)

    def draw_select(self, context, select_id):
        self.draw_custom_shape(self.custom_shape, select_id=select_id)

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape(
                'TRIS', custom_shape_verts)
                
                
class MyCustomShapeWidget(Gizmo):
    bl_idname = "VIEW3D_GT_custom_shape_widget"
    bl_target_properties = (
        {"id": "offset", "type": 'FLOAT', "array_length": 1},
    )

    __slots__ = (
        "custom_shape",
        "init_mouse_y",
        "init_value",
    )

    def _update_offset_matrix(self):
        # offset behind the light
        self.matrix_offset.col[3][2] = self.target_get_value("offset") / -10.0

    def draw(self, context):
        self._update_offset_matrix()
        self.draw_custom_shape(self.custom_shape)

    def draw_select(self, context, select_id):
        self._update_offset_matrix()
        self.draw_custom_shape(self.custom_shape, select_id=select_id)

    def setup(self):
        if not hasattr(self, "base_shape"):
            self.base_shape = self.new_custom_shape('TRIS', base_shape_verts)
        if not hasattr(self, "slider_shape"):
            self.base_shape = self.new_custom_shape('TRIS', slider_shape_verts)


    def invoke(self, context, event):
        self.init_mouse_y = event.mouse_y
        self.init_value = self.target_get_value("offset")
        return {'RUNNING_MODAL'}

    def exit(self, context, cancel):
        context.area.header_text_set(None)
        if cancel:
            self.target_set_value("offset", self.init_value)

    def modal(self, context, event, tweak):
        delta = (event.mouse_y - self.init_mouse_y) / 10.0
        if 'SNAP' in tweak:
            delta = round(delta)
        if 'PRECISE' in tweak:
            delta /= 10.0
        value = self.init_value - delta
        self.target_set_value("offset", value)
        context.area.header_text_set("My Gizmo: %.4f" % value)
        return {'RUNNING_MODAL'}



def gizmo_matrix(context):
    """ Get the gizmo matrix so it sits next to the camera frame """
    space = context.space_data
    ob = space.camera
    cam = ob.data
    z = 1 # probs doesn't matter, can set to clipsta +.1 or so
    loc = mathutils.Vector((
        math.tan(cam.angle_x/2) * z,
        -math.tan(cam.angle_x/2) * 1080 * z / 1920,
        -z))
    loc_cam = mathutils.Matrix.Translation(loc) @ ob.matrix_world 
    loc_cam = ob.matrix_world @ mathutils.Matrix.Translation(loc)
    return loc_cam.normalized()


def gizmo_color(context):
    """ Color the gizmo based on lock_camera """
    space = context.space_data
    return (1.0, 0.5, 0.0) if space.lock_camera else (0.0, 0.0, 0.0)


class ToggleView(bpy.types.Operator):
    bl_idname = "object.toggle_view"
    bl_label = "Toggle Lock Camera"
    bl_description = "Toggle camera view locked/unlocked"
    
    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'VIEW_3D'
    
    def execute(self, context):
        context.space_data.lock_camera = not context.space_data.lock_camera
        return {'FINISHED'}

       
class ViewLockGroup(bpy.types.GizmoGroup):
    bl_idname = "VIEW_GGT_Lock_View"
    bl_label = "Lock Camera View"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'3D', 'PERSISTENT', 'SELECT'}

    @classmethod
    def poll(cls, context):
        return (
            context.region_data.view_perspective == 'CAMERA'
            )

    def setup(self, context):

        gz = self.gizmos.new(ButtonWidget.bl_idname)
        gz.target_set_operator(ToggleView.bl_idname) 

        gz.matrix_basis =  gizmo_matrix(context)
        gz.color = gizmo_color(context)
        gz.alpha = 0.5

        gz.color_highlight = gz.color
        gz.alpha_highlight = 1.0

        self.view_lock_gizmo = gz

    def refresh(self, context):
        space = context.space_data
        gz = self.view_lock_gizmo
        gz.color = gizmo_color(context)
        gz.color_highlight = gz.color
        gz.matrix_basis =  gizmo_matrix(context)
        
    def draw_prepare(self, context):
        gz = self.view_lock_gizmo
        gz.matrix_basis = gizmo_matrix(context)


def register():
    bpy.utils.register_class(ButtonWidget)
    bpy.utils.register_class(ToggleView)
    bpy.utils.register_class(ViewLockGroup)


def unregister():
    bpy.utils.unregister_class(ButtonWidget)
    bpy.utils.unregister_class(ToggleView)
    bpy.utils.unregister_class(ViewLockGroup)
    
if __name__ == "__main__":
    register()