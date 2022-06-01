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
from mathutils import Vector, Matrix


# Gizmo Triangle Coords
size = 0.3
display_scale =  2.5

def locked(size):
    return ((size * 0.45052126, size * 0.87532949, -size * 0.00000273),(size * 0.55065256, size * 0.81972712, -size * 0.00000273),(size * 0.55065256, size * 0.89555436, -size * 0.00000273),(size * 0.55065256, size * 0.81972712, -size * 0.00000273),(size * 0.45052126, size * 0.87532949, -size * 0.00000273),(size * 0.48003152, size * 0.80546290, -size * 0.00000273),(size * 0.45052126, size * 0.87532949, -size * 0.00000273),(size * 0.36873698, size * 0.82018065, -size * 0.00000273),(size * 0.48003152, size * 0.80546290, -size * 0.00000273),(size * 0.67895466, size * 0.76656729, -size * 0.00000273),(size * 0.78771693, size * 0.73839647, -size * 0.00000273),(size * 0.73256809, size * 0.82018071, -size * 0.00000273),(size * 0.73256809, size * 0.82018071, -size * 0.00000273),(size * 0.65078378, size * 0.87532949, -size * 0.00000273),(size * 0.62127352, size * 0.80546290, -size * 0.00000273),(size * 0.62127352, size * 0.80546290, -size * 0.00000273),(size * 0.67895466, size * 0.76656729, -size * 0.00000273),(size * 0.73256809, size * 0.82018071, -size * 0.00000273),(size * 0.31358820, size * 0.73839647, -size * 0.00000273),(size * 0.42235038, size * 0.76656729, -size * 0.00000273),(size * 0.36873698, size * 0.82018065, -size * 0.00000273),(size * 0.65078378, size * 0.87532949, -size * 0.00000273),(size * 0.55065256, size * 0.81972712, -size * 0.00000273),(size * 0.62127352, size * 0.80546290, -size * 0.00000273),(size * 0.31358820, size * 0.73839647, -size * 0.00000273),(size * 0.38345477, size * 0.70888621, -size * 0.00000273),(size * 0.42235038, size * 0.76656729, -size * 0.00000273),(size * 0.71785027, size * 0.70888621, -size * 0.00000273),(size * 0.78771693, size * 0.73839647, -size * 0.00000273),(size * 0.67895466, size * 0.76656729, -size * 0.00000273),(size * 0.29336339, size * 0.63826531, -size * 0.00000273),(size * 0.38345477, size * 0.70888621, -size * 0.00000273),(size * 0.31358820, size * 0.73839647, -size * 0.00000273),(size * 0.71785027, size * 0.70888621, -size * 0.00000273),(size * 0.80794168, size * 0.63826531, -size * 0.00000273),(size * 0.78771693, size * 0.73839647, -size * 0.00000273),(size * 0.29336339, size * 0.63826531, -size * 0.00000273),(size * 0.36919051, size * 0.63826531, -size * 0.00000273),(size * 0.38345477, size * 0.70888621, -size * 0.00000273),(size * 0.73211455, size * 0.63826531, -size * 0.00000273),(size * 0.80794168, size * 0.63826531, -size * 0.00000273),(size * 0.71785027, size * 0.70888621, -size * 0.00000273),(size * 0.25297418, size * 0.13282087, -size * 0.00000273),(size * 0.29336339, size * 0.63826531, -size * 0.00000273),(size * 0.25297418, size * 0.63826531, -size * 0.00000273),(size * 0.25297418, size * 0.13282087, -size * 0.00000273),(size * 0.36919051, size * 0.63826531, -size * 0.00000273),(size * 0.29336339, size * 0.63826531, -size * 0.00000273),(size * 0.25297418, size * 0.13282087, -size * 0.00000273),(size * 0.73211455, size * 0.63826531, -size * 0.00000273),(size * 0.36919051, size * 0.63826531, -size * 0.00000273),(size * 0.25297418, size * 0.13282087, -size * 0.00000273),(size * 0.84833086, size * 0.13282087, -size * 0.00000273),(size * 0.73211455, size * 0.63826531, -size * 0.00000273),(size * 0.84833086, size * 0.13282087, -size * 0.00000273),(size * 0.84833086, size * 0.63826531, -size * 0.00000273),(size * 0.80794168, size * 0.63826531, -size * 0.00000273),(size * 0.42235038, size * 0.76656729, -size * 0.00000273),(size * 0.48003152, size * 0.80546290, -size * 0.00000273),(size * 0.36873698, size * 0.82018065, -size * 0.00000273),(size * 0.55065256, size * 0.81972712, -size * 0.00000273),(size * 0.65078378, size * 0.87532949, -size * 0.00000273),(size * 0.55065256, size * 0.89555436, -size * 0.00000273),(size * 0.84833086, size * 0.13282087, -size * 0.00000273),(size * 0.80794168, size * 0.63826531, -size * 0.00000273),(size * 0.73211455, size * 0.63826531, -size * 0.00000273))
def unlocked(size):
    return ((size * 0.31537026, size * 0.76656723, -size * 0.00000273),(size * 0.41758227, size * 0.73839641, -size * 0.00000273),(size * 0.37271118, size * 0.82018059, -size * 0.00000273),(size * 0.17478977, size * 0.80546284, -size * 0.00000273),(size * 0.22469814, size * 0.81972706, -size * 0.00000273),(size * 0.14322776, size * 0.87532949, -size * 0.00000273),(size * 0.22469814, size * 0.81972706, -size * 0.00000273),(size * 0.30616856, size * 0.87532943, -size * 0.00000273),(size * 0.22469814, size * 0.89555430, -size * 0.00000273),(size * 0.37271118, size * 0.82018059, -size * 0.00000273),(size * 0.30616856, size * 0.87532943, -size * 0.00000273),(size * 0.27460653, size * 0.80546284, -size * 0.00000273),(size * 0.27460653, size * 0.80546284, -size * 0.00000273),(size * 0.31537026, size * 0.76656723, -size * 0.00000273),(size * 0.37271118, size * 0.82018059, -size * 0.00000273),(size * 0.13402605, size * 0.76656723, -size * 0.00000273),(size * 0.17478977, size * 0.80546284, -size * 0.00000273),(size * 0.07668506, size * 0.82018065, -size * 0.00000273),(size * 0.07668506, size * 0.82018065, -size * 0.00000273),(size * 0.17478977, size * 0.80546284, -size * 0.00000273),(size * 0.14322776, size * 0.87532949, -size * 0.00000273),(size * 0.03181396, size * 0.73839641, -size * 0.00000273),(size * 0.10653823, size * 0.70888615, -size * 0.00000273),(size * 0.13402605, size * 0.76656723, -size * 0.00000273),(size * 0.34285805, size * 0.70888615, -size * 0.00000273),(size * 0.41758227, size * 0.73839641, -size * 0.00000273),(size * 0.31537026, size * 0.76656723, -size * 0.00000273),(size * 0.01535828, size * 0.63826525, -size * 0.00000273),(size * 0.10653823, size * 0.70888615, -size * 0.00000273),(size * 0.03181396, size * 0.73839641, -size * 0.00000273),(size * 0.34285805, size * 0.70888615, -size * 0.00000273),(size * 0.43403792, size * 0.63826525, -size * 0.00000273),(size * 0.41758227, size * 0.73839641, -size * 0.00000273),(size * 0.01535828, size * 0.63826525, -size * 0.00000273),(size * 0.09645758, size * 0.63826525, -size * 0.00000273),(size * 0.10653823, size * 0.70888615, -size * 0.00000273),(size * 0.35293865, size * 0.63826525, -size * 0.00000273),(size * 0.43403792, size * 0.63826525, -size * 0.00000273),(size * 0.34285805, size * 0.70888615, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.35293865, size * 0.63826525, -size * 0.00000273),(size * 0.31621033, size * 0.63826525, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.43403792, size * 0.63826525, -size * 0.00000273),(size * 0.35293865, size * 0.63826525, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.91156697, size * 0.63826525, -size * 0.00000273),(size * 0.43403792, size * 0.63826525, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.82936341, size * 0.56055987, -size * 0.00000273),(size * 0.91156697, size * 0.63826525, -size * 0.00000273),(size * 0.82936341, size * 0.56055987, -size * 0.00000273),(size * 0.91156697, size * 0.13282087, -size * 0.00000273),(size * 0.91156697, size * 0.63826525, -size * 0.00000273),(size * 0.31621033, size * 0.13282087, -size * 0.00000273),(size * 0.39841390, size * 0.21052623, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.82936341, size * 0.21052623, -size * 0.00000273),(size * 0.91156697, size * 0.13282087, -size * 0.00000273),(size * 0.82936341, size * 0.56055987, -size * 0.00000273),(size * 0.31621033, size * 0.13282087, -size * 0.00000273),(size * 0.82936341, size * 0.21052623, -size * 0.00000273),(size * 0.39841390, size * 0.21052623, -size * 0.00000273),(size * 0.31621033, size * 0.13282087, -size * 0.00000273),(size * 0.91156697, size * 0.13282087, -size * 0.00000273),(size * 0.82936341, size * 0.21052623, -size * 0.00000273),(size * 0.30616856, size * 0.87532943, -size * 0.00000273),(size * 0.22469814, size * 0.81972706, -size * 0.00000273),(size * 0.27460653, size * 0.80546284, -size * 0.00000273),(size * 0.03181396, size * 0.73839641, -size * 0.00000273),(size * 0.13402605, size * 0.76656723, -size * 0.00000273),(size * 0.07668506, size * 0.82018065, -size * 0.00000273),(size * 0.14322776, size * 0.87532949, -size * 0.00000273),(size * 0.22469814, size * 0.81972706, -size * 0.00000273),(size * 0.22469814, size * 0.89555430, -size * 0.00000273),(size * 0.31621033, size * 0.13282087, -size * 0.00000273),(size * 0.39841390, size * 0.56055987, -size * 0.00000273),(size * 0.31621033, size * 0.63826525, -size * 0.00000273))
def home(size):
    return ((size * 0.13588154, size * 0.26217312, size * 0.00000000),(size * 0.39078629, size * 0.27160430, size * 0.00000000),(size * 0.26804948, size * 0.39434111, size * 0.00000000),(size * 0.09999990, size * 0.10000005, size * 0.00000000),(size * 0.13588154, size * 0.26217312, size * 0.00000000),(size * 0.09999996, size * 0.30000001, size * 0.00000000),(size * 0.13588154, size * 0.26217312, size * 0.00000000),(size * 0.25861835, size * 0.13943630, size * 0.00000000),(size * 0.39078629, size * 0.27160430, size * 0.00000000),(size * 0.09999990, size * 0.10000005, size * 0.00000000),(size * 0.25861835, size * 0.13943630, size * 0.00000000),(size * 0.13588154, size * 0.26217312, size * 0.00000000),(size * 0.09999990, size * 0.10000005, size * 0.00000000),(size * 0.30000001, size * 0.10000002, size * 0.00000000),(size * 0.25861835, size * 0.13943630, size * 0.00000000),(size * 0.10000000, size * 0.69999999, size * 0.00000000),(size * 0.13943632, size * 0.74138165, size * 0.00000000),(size * 0.10000000, size * 0.90000004, size * 0.00000000),(size * 0.13943632, size * 0.74138165, size * 0.00000000),(size * 0.26217312, size * 0.86411846, size * 0.00000000),(size * 0.10000000, size * 0.90000004, size * 0.00000000),(size * 0.26217312, size * 0.86411846, size * 0.00000000),(size * 0.30000001, size * 0.90000004, size * 0.00000000),(size * 0.10000000, size * 0.90000004, size * 0.00000000),(size * 0.13943632, size * 0.74138165, size * 0.00000000),(size * 0.39434111, size * 0.73195052, size * 0.00000000),(size * 0.26217312, size * 0.86411846, size * 0.00000000),(size * 0.27160430, size * 0.60921371, size * 0.00000000),(size * 0.39434111, size * 0.73195052, size * 0.00000000),(size * 0.13943632, size * 0.74138165, size * 0.00000000),(size * 0.60565889, size * 0.26804948, size * 0.00000000),(size * 0.86056370, size * 0.25861835, size * 0.00000000),(size * 0.72839570, size * 0.39078629, size * 0.00000000),(size * 0.86056370, size * 0.25861835, size * 0.00000000),(size * 0.89999998, size * 0.09999990, size * 0.00000000),(size * 0.89999998, size * 0.30000001, size * 0.00000000),(size * 0.73782688, size * 0.13588154, size * 0.00000000),(size * 0.86056370, size * 0.25861835, size * 0.00000000),(size * 0.60565889, size * 0.26804948, size * 0.00000000),(size * 0.73782688, size * 0.13588154, size * 0.00000000),(size * 0.89999998, size * 0.09999990, size * 0.00000000),(size * 0.86056370, size * 0.25861835, size * 0.00000000),(size * 0.69999999, size * 0.09999996, size * 0.00000000),(size * 0.89999998, size * 0.09999990, size * 0.00000000),(size * 0.73782688, size * 0.13588154, size * 0.00000000),(size * 0.74138165, size * 0.86056370, size * 0.00000000),(size * 0.90000010, size * 0.89999998, size * 0.00000000),(size * 0.69999999, size * 0.89999998, size * 0.00000000),(size * 0.74138165, size * 0.86056370, size * 0.00000000),(size * 0.86411846, size * 0.73782688, size * 0.00000000),(size * 0.90000010, size * 0.89999998, size * 0.00000000),(size * 0.86411846, size * 0.73782688, size * 0.00000000),(size * 0.90000004, size * 0.69999999, size * 0.00000000),(size * 0.90000010, size * 0.89999998, size * 0.00000000),(size * 0.60921371, size * 0.72839570, size * 0.00000000),(size * 0.86411846, size * 0.73782688, size * 0.00000000),(size * 0.74138165, size * 0.86056370, size * 0.00000000),(size * 0.60921371, size * 0.72839570, size * 0.00000000),(size * 0.73195052, size * 0.60565889, size * 0.00000000),(size * 0.86411846, size * 0.73782688, size * 0.00000000))


class HudPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    size: bpy.props.FloatProperty(
        name="Size", default=0.3, min=0.1, max=2.0)
    display_scale: bpy.props.FloatProperty(
        name="Spacing", default=1.0, min=1.0, max=3.0)

    def draw(self, context):
        self.layout.prop(self, "size")
        self.layout.prop(self, "display_scale")

    
class ViewLockWidget(bpy.types.Gizmo):
    """ Custom 'button' gizmo for camera """
    bl_idname = "VIEW3D_GT_viewlock_widget"
    
    locked: bpy.props.BoolProperty(default=True)

    def shape(self):
        return self.locked_shape if self.locked else self.unlocked_shape

    def draw(self, context):
        self.draw_custom_shape(self.shape())

    def draw_select(self, context, select_id):
        self.draw_custom_shape(self.shape(), select_id=select_id)

    def setup(self):
        size = bpy.context.preferences.addons[__name__].preferences.size
        if not hasattr(self, "unlocked_shape"):
            self.unlocked_shape = self.new_custom_shape(
                'TRIS', unlocked(size))
        if not hasattr(self, "locked_shape"):
            self.locked_shape = self.new_custom_shape(
                'TRIS', locked(size))


class HomeWidget(bpy.types.Gizmo):
    """ Custom 'full screen' gizmo for camera """
    bl_idname = "VIEW3D_GT_frame_all_widget"

    def draw(self, context):
        self.draw_custom_shape(self.home_shape)

    def draw_select(self, context, select_id):
        self.draw_custom_shape(self.home_shape, select_id=select_id)

    def setup(self):
        size = bpy.context.preferences.addons[__name__].preferences.size
        if not hasattr(self, "home_shape"):
            self.home_shape = self.new_custom_shape(
                'TRIS', home(size))


def gizmo_matrix(context, offset_x=0, offset_y=0, anchor="bottom_left"):
    """ Get the gizmo matrix so it sits next to the camera frame """
    space = context.space_data
    area = context.area
    ui = area.regions[3]

    scene = context.scene
    ob = space.camera
    cam = ob.data

    preferences = context.preferences

    z = cam.clip_start + .01

    gizmo_size = preferences.view.gizmo_size
    size = preferences.addons[__name__].preferences.size
    display_scale = preferences.addons[__name__].preferences.display_scale

    res_x, res_y = (scene.render.resolution_x, scene.render.resolution_y)
    landscape = res_x > res_y
    angle = cam.angle_x / 2 if landscape else cam.angle_y / 2
    base = math.tan(angle) * z
    x = base if landscape else base * res_x / res_y
    y = base * res_y / res_x if landscape else base
    largest = max(x, y)

    # first we're getting camera space coords of the anchor
    loc = Vector((
        x + largest * 2 * cam.shift_x ,
        -y + largest * 2 * cam.shift_y,
        -z
        ))
    # in world space:
    loc_cam = ob.matrix_world @ Matrix.Translation(loc)
    # just the translation part
    loc_vec= loc_cam.to_translation()



    # now we get that in screen pixels
    loc2d = bpy_extras.view3d_utils.location_3d_to_region_2d(
        context.region,
        context.space_data.region_3d,
        loc_vec)

    maxwidth = context.area.width - ui.width

    loc2d[1] = max(loc2d[1], 0)
    loc2d[0] = min(loc2d[0], maxwidth)
    loc2d = loc2d + display_scale * gizmo_size * size * Vector((offset_x, offset_y))

    # and subtract gizmo width
    origin2d = loc2d - Vector((display_scale * gizmo_size * size, 0))
    # lets calculate the 3D vector again
    loc_shift = bpy_extras.view3d_utils.region_2d_to_location_3d(
        context.region,
        context.space_data.region_3d,
        origin2d,
        loc_vec
        )
    # shift it in and out of camera space to get the orientation right
    loc_out = ob.matrix_world.inverted() @ Matrix.Translation(loc_shift)
    loc_cam = ob.matrix_world @ Matrix.Translation(loc_out.to_translation())

    return loc_cam.normalized()


def gizmo_color(context):
    """ Color the gizmo based on lock_camera """
    space = context.space_data
    return context.preferences.themes['Default'].user_interface.gizmo_primary


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

        gz = self.gizmos.new(ViewLockWidget.bl_idname)
        gz.target_set_operator(ToggleView.bl_idname) 

        gz.matrix_basis =  gizmo_matrix(context)
        gz.color = gizmo_color(context)
        gz.alpha = 0.5

        gz.color_highlight = gz.color
        gz.alpha_highlight = 1.0
        gz.locked = context.space_data.lock_camera
        self.view_lock_gizmo = gz

    def refresh(self, context):
        space = context.space_data
        gz = self.view_lock_gizmo
        gz.color = gizmo_color(context)
        gz.color_highlight = gz.color
        gz.locked = context.space_data.lock_camera
        gz.matrix_basis =  gizmo_matrix(context)
        
    def draw_prepare(self, context):
        gz = self.view_lock_gizmo
        gz.locked = context.space_data.lock_camera
        gz.matrix_basis = gizmo_matrix(context)


class FrameCameraGroup(bpy.types.GizmoGroup):
    bl_idname = "VIEW_GGT_Frame_camera_bounds"
    bl_label = "Frame Camera Bounds"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'3D', 'PERSISTENT', 'SELECT'}

    @classmethod
    def poll(cls, context):
        return (
            context.region_data.view_perspective == 'CAMERA'
            )

    def setup(self, context):

        gz = self.gizmos.new(HomeWidget.bl_idname)
        gz.target_set_operator("view3d.view_center_camera")

        gz.matrix_basis =  gizmo_matrix(context, offset_y=1)
        gz.color = gizmo_color(context)
        gz.alpha = 0.5

        gz.color_highlight = gz.color
        gz.alpha_highlight = 1.0

        self.frame_camera_gizmo = gz

    def refresh(self, context):
        space = context.space_data
        gz = self.frame_camera_gizmo
        gz.color = gizmo_color(context)
        gz.color_highlight = gz.color
        gz.matrix_basis =  gizmo_matrix(context, offset_y=1)
        
    def draw_prepare(self, context):
        gz = self.frame_camera_gizmo
        gz.matrix_basis = gizmo_matrix(context, offset_y=1)


def register():
    bpy.utils.register_class(HudPreferences)
    bpy.utils.register_class(ViewLockWidget)
    bpy.utils.register_class(HomeWidget)
    bpy.utils.register_class(ToggleView)
    bpy.utils.register_class(ViewLockGroup)
    bpy.utils.register_class(FrameCameraGroup)


def unregister():
    bpy.utils.unregister_class(ViewLockWidget)
    bpy.utils.unregister_class(HomeWidget)
    bpy.utils.unregister_class(ToggleView)
    bpy.utils.unregister_class(ViewLockGroup)
    bpy.utils.unregister_class(FrameCameraGroup)
    bpy.utils.unregister_class(HudPreferences)
    
if __name__ == "__main__":
    register()
