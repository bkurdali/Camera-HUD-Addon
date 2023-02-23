if "bpy" in locals():
    import importlib
    importlib.reload(icon_shapes)

else:
    from . import icon_shapes

import bpy
import bpy_extras
import mathutils
import math

from bpy_extras import view3d_utils
from mathutils import Vector, Matrix


# Gizmo Triangle Coords

def sizify(iterable, size):
    return [[size * co for co in tri] for tri in iterable] 

def locked(size):
    return sizify(icon_shapes.locked, size)

def unlocked(size):
    return sizify(icon_shapes.unlocked, size)

def home(size):
    return sizify(icon_shapes.home, size)

def ruler(size):
    return sizify(icon_shapes.ruler, size)

size = 2.0
arcside = sizify(icon_shapes.arcside, size)

((-size * 0.49039260, size * 0.09754515, size * 0.00000000),(-size * 0.44747975, size * 0.18535216, size * 0.00000000),(-size * 0.46193975, size * 0.19134170, size * 0.00000000),(-size * 0.41573477, size * 0.27778512, size * 0.00000000),(-size * 0.34248617, size * 0.34248620, size * 0.00000000),(-size * 0.35355338, size * 0.35355341, size * 0.00000000),(-size * 0.41573477, -size * 0.27778512, size * 0.00000000),(-size * 0.34248614, -size * 0.34248620, size * 0.00000000),(-size * 0.40272108, -size * 0.26908967, size * 0.00000000),(-size * 0.46193975, -size * 0.19134170, size * 0.00000000),(-size * 0.47504196, -size * 0.09449171, size * 0.00000000),(-size * 0.49039263, -size * 0.09754515, size * 0.00000000),(-size * 0.49039260, size * 0.09754515, size * 0.00000000),(-size * 0.48434860, size * 0.00000000, size * 0.00000000),(-size * 0.47504193, size * 0.09449171, size * 0.00000000),(-size * 0.41573477, size * 0.27778512, size * 0.00000000),(-size * 0.44747975, size * 0.18535216, size * 0.00000000),(-size * 0.40272108, size * 0.26908967, size * 0.00000000),(-size * 0.41573477, -size * 0.27778512, size * 0.00000000),(-size * 0.44747975, -size * 0.18535216, size * 0.00000000),(-size * 0.46193975, -size * 0.19134170, size * 0.00000000),(-size * 0.49039263, -size * 0.09754515, size * 0.00000000),(-size * 0.48434860, size * 0.00000000, size * 0.00000000),(-size * 0.50000000, size * 0.00000000, size * 0.00000000),(-size * 0.49039260, size * 0.09754515, size * 0.00000000),(-size * 0.47504193, size * 0.09449171, size * 0.00000000),(-size * 0.44747975, size * 0.18535216, size * 0.00000000),(-size * 0.41573477, size * 0.27778512, size * 0.00000000),(-size * 0.40272108, size * 0.26908967, size * 0.00000000),(-size * 0.34248617, size * 0.34248620, size * 0.00000000),(-size * 0.41573477, -size * 0.27778512, size * 0.00000000),(-size * 0.35355335, -size * 0.35355341, size * 0.00000000),(-size * 0.34248614, -size * 0.34248620, size * 0.00000000),(-size * 0.46193975, -size * 0.19134170, size * 0.00000000),(-size * 0.44747975, -size * 0.18535216, size * 0.00000000),(-size * 0.47504196, -size * 0.09449171, size * 0.00000000),(-size * 0.49039260, size * 0.09754515, size * 0.00000000),(-size * 0.50000000, size * 0.00000000, size * 0.00000000),(-size * 0.48434860, size * 0.00000000, size * 0.00000000),(-size * 0.41573477, size * 0.27778512, size * 0.00000000),(-size * 0.46193975, size * 0.19134170, size * 0.00000000),(-size * 0.44747975, size * 0.18535216, size * 0.00000000),(-size * 0.41573477, -size * 0.27778512, size * 0.00000000),(-size * 0.40272108, -size * 0.26908967, size * 0.00000000),(-size * 0.44747975, -size * 0.18535216, size * 0.00000000),(-size * 0.49039263, -size * 0.09754515, size * 0.00000000),(-size * 0.47504196, -size * 0.09449171, size * 0.00000000),(-size * 0.48434860, size * 0.00000000, size * 0.00000000))
arcbottom = ((size * 0.27778518, -size * 0.41573477, size * 0.00000000),(size * 0.18525776, -size * 0.44725186, size * 0.00000000),(size * 0.19134170, -size * 0.46193975, size * 0.00000000),(size * 0.09754515, -size * 0.49039263, size * 0.00000000),(size * 0.00000000, -size * 0.48410192, size * 0.00000000),(size * 0.00000000, -size * 0.50000000, size * 0.00000000),(-size * 0.09754512, -size * 0.49039257, size * 0.00000000),(-size * 0.18525776, -size * 0.44725186, size * 0.00000000),(-size * 0.19134170, -size * 0.46193975, size * 0.00000000),(-size * 0.35355338, -size * 0.35355341, size * 0.00000000),(-size * 0.26895261, -size * 0.40251598, size * 0.00000000),(-size * 0.34231177, -size * 0.34231180, size * 0.00000000),(size * 0.35355341, -size * 0.35355332, size * 0.00000000),(size * 0.26895270, -size * 0.40251598, size * 0.00000000),(size * 0.27778518, -size * 0.41573477, size * 0.00000000),(size * 0.19134170, -size * 0.46193975, size * 0.00000000),(size * 0.09444358, -size * 0.47480002, size * 0.00000000),(size * 0.09754515, -size * 0.49039263, size * 0.00000000),(-size * 0.09754512, -size * 0.49039257, size * 0.00000000),(size * 0.00000000, -size * 0.48410192, size * 0.00000000),(-size * 0.09444356, -size * 0.47479996, size * 0.00000000),(-size * 0.27778509, -size * 0.41573477, size * 0.00000000),(-size * 0.18525776, -size * 0.44725186, size * 0.00000000),(-size * 0.26895261, -size * 0.40251598, size * 0.00000000),(size * 0.27778518, -size * 0.41573477, size * 0.00000000),(size * 0.26895270, -size * 0.40251598, size * 0.00000000),(size * 0.18525776, -size * 0.44725186, size * 0.00000000),(size * 0.09754515, -size * 0.49039263, size * 0.00000000),(size * 0.09444358, -size * 0.47480002, size * 0.00000000),(size * 0.00000000, -size * 0.48410192, size * 0.00000000),(-size * 0.09754512, -size * 0.49039257, size * 0.00000000),(-size * 0.09444356, -size * 0.47479996, size * 0.00000000),(-size * 0.18525776, -size * 0.44725186, size * 0.00000000),(-size * 0.35355338, -size * 0.35355341, size * 0.00000000),(-size * 0.27778509, -size * 0.41573477, size * 0.00000000),(-size * 0.26895261, -size * 0.40251598, size * 0.00000000),(size * 0.35355341, -size * 0.35355332, size * 0.00000000),(size * 0.34231180, -size * 0.34231171, size * 0.00000000),(size * 0.26895270, -size * 0.40251598, size * 0.00000000),(size * 0.19134170, -size * 0.46193975, size * 0.00000000),(size * 0.18525776, -size * 0.44725186, size * 0.00000000),(size * 0.09444358, -size * 0.47480002, size * 0.00000000),(-size * 0.09754512, -size * 0.49039257, size * 0.00000000),(size * 0.00000000, -size * 0.50000000, size * 0.00000000),(size * 0.00000000, -size * 0.48410192, size * 0.00000000),(-size * 0.27778509, -size * 0.41573477, size * 0.00000000),(-size * 0.19134170, -size * 0.46193975, size * 0.00000000),(-size * 0.18525776, -size * 0.44725186, size * 0.00000000))

moveside = sorted(
    [(size * 0.41864729, -size * 0.08419549, size * 0.00000000),(size * 0.41864729, size * 0.08419549, size * 0.00000000),(size * 0.50284278, size * 0.00000000, size * 0.00000000)],
    key=lambda x: x[1],
    )
moveup = sorted(
    ((size * 0.08419552, size * 0.41864729, size * 0.00000000),(-size * 0.08419549, size * 0.41864729, size * 0.00000000),(size * 0.00000006, size * 0.50284278, size * 0.00000000)),
    key=lambda x: x[0],
    )

moveside = ((size * 0.50640213, size * 0.08419549, size * 0.00000000),(size * 0.57384509, size * 0.00000000, size * 0.00000000),(size * 0.49228519, size * 0.08155994, size * 0.00000000),(size * 0.50640213, -size * 0.08419549, size * 0.00000000),(size * 0.57384509, size * 0.00000000, size * 0.00000000),(size * 0.59059763, size * 0.00000000, size * 0.00000000),(size * 0.50640213, size * 0.08419549, size * 0.00000000),(size * 0.59059763, size * 0.00000000, size * 0.00000000),(size * 0.57384509, size * 0.00000000, size * 0.00000000),(size * 0.50640213, -size * 0.08419549, size * 0.00000000),(size * 0.49228519, -size * 0.08155994, size * 0.00000000),(size * 0.57384509, size * 0.00000000, size * 0.00000000))
moveup = ((-size * 0.08419549, size * 0.50640190, size * 0.00000000),(size * 0.00000006, size * 0.57384485, size * 0.00000000),(-size * 0.08155994, size * 0.49228495, size * 0.00000000),(size * 0.08419552, size * 0.50640190, size * 0.00000000),(size * 0.00000006, size * 0.57384485, size * 0.00000000),(size * 0.00000006, size * 0.59059739, size * 0.00000000),(-size * 0.08419549, size * 0.50640190, size * 0.00000000),(size * 0.00000006, size * 0.59059739, size * 0.00000000),(size * 0.00000006, size * 0.57384485, size * 0.00000000),(size * 0.08419552, size * 0.50640190, size * 0.00000000),(size * 0.08155997, size * 0.49228495, size * 0.00000000),(size * 0.00000006, size * 0.57384485, size * 0.00000000))
movedepth = ((size * 0.06000001, -size * 0.05862415, size * 0.00000000),(-size * 0.00000000, -size * 0.02464572, size * 0.00000000),(size * 0.00000000, -size * 0.00862414, size * 0.00000000),(size * 0.06000002, size * 0.05862414, size * 0.00000000),(size * 0.00000000, size * 0.02422005, size * 0.00000000),(size * 0.00000000, size * 0.00862414, size * 0.00000000),(-size * 0.06000001, size * 0.05862415, size * 0.00000000),(size * 0.00000000, size * 0.02422005, size * 0.00000000),(-size * 0.06000001, size * 0.07422006, size * 0.00000000),(-size * 0.06000002, -size * 0.05862414, size * 0.00000000),(-size * 0.00000000, -size * 0.02464572, size * 0.00000000),(-size * 0.06000002, -size * 0.07464573, size * 0.00000000),(size * 0.06000001, -size * 0.05862415, size * 0.00000000),(size * 0.06000001, -size * 0.07464573, size * 0.00000000),(-size * 0.00000000, -size * 0.02464572, size * 0.00000000),(size * 0.06000002, size * 0.05862414, size * 0.00000000),(size * 0.06000002, size * 0.07422006, size * 0.00000000),(size * 0.00000000, size * 0.02422005, size * 0.00000000),(-size * 0.06000001, size * 0.05862415, size * 0.00000000),(size * 0.00000000, size * 0.00862414, size * 0.00000000),(size * 0.00000000, size * 0.02422005, size * 0.00000000),(-size * 0.06000002, -size * 0.05862414, size * 0.00000000),(size * 0.00000000, -size * 0.00862414, size * 0.00000000),(-size * 0.00000000, -size * 0.02464572, size * 0.00000000))


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
        size = bpy.context.preferences.addons["camera_hud"].preferences.size
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
        size = bpy.context.preferences.addons["camera_hud"].preferences.size
        if not hasattr(self, "home_shape"):
            self.home_shape = self.new_custom_shape(
                'TRIS', home(size))


class Transformer(bpy.types.Gizmo):
    bl_target_properties = (
        {"id": "offset", "type": 'FLOAT', "array_length": 1},
    )

    __slots__ = (
        "custom_shape",
        "init_mouse_y",
        "init_value",
    )


    def draw(self, context):
        self.draw_custom_shape(self.custom_shape)

    def draw_select(self, context, select_id):
        self.draw_custom_shape(self.custom_shape, select_id=select_id)

    def invoke(self, context, event):
        self.init_mouse_y = event.mouse_y
        return {'RUNNING_MODAL'}

    def exit(self, context, cancel):
        context.area.header_text_set(None)

    def modal(self, context, event, tweak):
        return {'RUNNING_MODAL'}

class ArcSideWidget(Transformer):
    bl_idname = "VIEW3D_GT_arc_side_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('TRIS', arcside)


class ArcBottomWidget(Transformer):
    bl_idname = "VIEW3D_GT_arc_bottom_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('TRIS', arcbottom)


class XMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_xmove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('TRIS', moveside)


class YMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_ymove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('TRIS', moveup)


class ZMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_zmove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('TRIS', movedepth)


class CameraTransformGroup(bpy.types.GizmoGroup):
    bl_idname = "OBJECT_GGT_light_test"
    bl_label = "Test Light Widget"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'3D', 'PERSISTENT'}

    @classmethod
    def poll(cls, context):
        cam = context.space_data.camera
        selected = context.selected_objects
        return (
            context.region_data.view_perspective == 'CAMERA' and context.active_object == cam and
            len(selected) == 1 and cam in selected
            )

    def setup(self, context):
        ob = context.object
        # gz = self.gizmos.new(MyCustomShapeWidget.bl_idname)
        theme = context.preferences.themes['Default'].user_interface
        color = (theme.axis_x, theme.axis_y, theme.axis_z)
        rotators = [
            {
                'name': ArcSideWidget.bl_idname,
                'prop': 'x_rotation_gizmo',
                'scale': 1.2,},
            {
                'name': ArcBottomWidget.bl_idname,
                'prop': 'y_rotation_gizmo',
                'scale': 1.2,},
            {
                'name': "GIZMO_GT_dial_3d",
                'prop': 'z_rotation_gizmo',
                'scale':1.0,}]
        locators = [
            {
                'name': XMoveWidget.bl_idname,
                'prop': 'x_location_gizmo',
                'scale': 1.2,},
            {
                'name': YMoveWidget.bl_idname,
                'prop': 'y_location_gizmo',
                'scale': 1.2,},
            {
                'name': ZMoveWidget.bl_idname,
                'prop': 'z_location_gizmo',
                'scale': 1,},
        ]
        def set_gizmo(i, rotator, operator):
            gz = self.gizmos.new(rotator['name'])
            props = gz.target_set_operator(operator)
            for axis in range(3):
                props.constraint_axis[axis]= i == axis
            props.orient_type = 'LOCAL'
            gz.matrix_basis = (ob.matrix_world @ mathutils.Matrix.Translation(mathutils.Vector((0,0,-1)))).normalized()
            gz.color = color[i]
            gz.alpha = 0.9
            gz.color_highlight = 1.0, 1.0, 1.0
            gz.alpha_highlight = 1.0
            gz.scale_basis = rotator["scale"]
            gz.use_draw_modal = True
            setattr(self, rotator["prop"], gz)

        for i, rotator in enumerate(rotators):
            set_gizmo(i, rotator, "transform.rotate")


        for i, locator in enumerate(locators):
            set_gizmo(i, locator, "transform.translate")

    def refresh(self, context):
        ob = context.object
        for gz in (self.z_rotation_gizmo, self.x_rotation_gizmo, self.y_rotation_gizmo, self.x_location_gizmo, self.y_location_gizmo, self.z_location_gizmo):
            gz.matrix_basis = (ob.matrix_world @ mathutils.Matrix.Translation(mathutils.Vector((0,0,-1)))).normalized()


class GizmoData:

    def __init__(self, context, offset_x=0, offset_y=0, anchor="bottom_left"):
        self.context = context
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.anchor = anchor
        self.space = context.space_data
        self.area = context.area
        self.ui = self.area.regions[3]
        self.scene = context.scene
        self.ob = self.space.camera
        self.cam = self.ob.data
        self.size = context.preferences.addons["camera_hud"].preferences.size
        self.display_scale = context.preferences.addons["camera_hud"].preferences.display_scale
        self.gizmo_size = context.preferences.view.gizmo_size
        self.res_x, self.res_y = (
            self.scene.render.resolution_x, self.scene.render.resolution_y)
        self.loc_vec = self.matrix_base()        

    def matrix_base(self):
        """ Get the gizmo matrix so it sits next to the camera frame """

        z = self.cam.clip_start + .01
        # we can have 'wrong' sensor fitting for the display aspect
        aspect = self.res_x / self.res_y
        shift_flip = self.cam.sensor_fit != ('VERTICAL' if aspect > 1 else 'HORIZONTAL')
        landscape = (aspect > 1) if shift_flip else (aspect < 1)

        angle = self.cam.angle / 2
        base = math.tan(angle) * z
        
        x = base if landscape else base * aspect
        y = base / aspect if landscape else base
        largest = max(x, y) if shift_flip else min(x, y)

        # first we're getting camera space coords of the anchor
        loc = Vector((
            x + largest * 2 * self.cam.shift_x,
            -y + largest * 2 * self.cam.shift_y,
            -z
            ))
        # in world space:
        loc_cam = self.ob.matrix_world @ Matrix.Translation(loc)
        # just the translation part
        loc_vec= loc_cam.to_translation()
        return loc_vec    
    
    def matrix_2d(self):
        """ Get the gizmo matrix so it sits next to the camera frame """
        loc2d = bpy_extras.view3d_utils.location_3d_to_region_2d(
            self.context.region,
            self.space.region_3d,
            self.loc_vec)

        maxwidth = self.area.width - self.ui.width
        loc2d[1] = max(loc2d[1], self.display_scale * self.gizmo_size * self.size * 2)
        loc2d[0] = min(loc2d[0], maxwidth - self.display_scale * self.gizmo_size * self.size * 2 )
        loc2d = loc2d + self.display_scale * self.gizmo_size * self.size * Vector((self.offset_x, self.offset_y))
        # and subtract gizmo width
        return loc2d + Vector((self.display_scale * self.gizmo_size * self.size, 0))

    def matrix_3d(self):
        """ Get the gizmo matrix so it sits next to the camera frame """ 
        
        # lets calculate the 3D vector again
        loc_shift = bpy_extras.view3d_utils.region_2d_to_location_3d(
            self.context.region,
            self.space.region_3d,
            self.matrix_2d(),
            self.loc_vec
            )
        # shift it in and out of camera space to get the orientation right
        loc_out = self.ob.matrix_world.inverted() @ Matrix.Translation(loc_shift)
        loc_cam = self.ob.matrix_world @ Matrix.Translation(loc_out.to_translation())
        return loc_cam.normalized()

    def color(self):
        """ Color the gizmo based on lock_camera """
        return self.context.preferences.themes['Default'].user_interface.gizmo_primary


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
    bl_options = {'PERSISTENT', 'SCALE'}

    @classmethod
    def poll(cls, context):
        return (
            context.region_data.view_perspective == 'CAMERA'
            )

    def setup(self, context):

        gz1 = self.gizmos.new("GIZMO_GT_button_2d") 
        gz1.icon = 'LOCKVIEW_OFF'
        gz2 = self.gizmos.new("GIZMO_GT_button_2d")
        gz2.icon = 'LOCKVIEW_ON'
        
        for gz in (gz1, gz2):
            gz.draw_options = {'BACKDROP', 'OUTLINE'}
            gz.alpha = 0.0
            gz.color_highlight = 0.8, 0.8, 0.8
            gz.alpha_highlight = 0.2
            props = gz.target_set_operator(ToggleView.bl_idname)
            gz.scale_basis = (80 * 0.35) / 2 # Same as buttons defined in C
        self.view_lock_gizmo = gz1
        self.view_unlock_gizmo= gz2
        self.draw_prepare(context)

    def refresh(self, context):
        self.draw_prepare(context)
        
    def draw_prepare(self, context):
        for gz in (self.view_lock_gizmo, self.view_unlock_gizmo):
            gz_vector = GizmoData(context).matrix_2d()
            gz.matrix_basis[0][3] = gz_vector[0]
            gz.matrix_basis[1][3] = gz_vector[1]            
        self.view_lock_gizmo.hide = context.space_data.lock_camera
        self.view_unlock_gizmo.hide = not self.view_lock_gizmo.hide


class FrameCameraGroup(bpy.types.GizmoGroup):
    bl_idname = "VIEW_GGT_Frame_camera_bounds"
    bl_label = "Frame Camera Bounds"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'PERSISTENT', 'SCALE'}

    @classmethod
    def poll(cls, context):
        return (
            context.region_data.view_perspective == 'CAMERA'
            )

    def setup(self, context):

        gz = self.gizmos.new("GIZMO_GT_button_2d")
        gz.icon = "MOD_OPACITY"
        gz.draw_options = {'BACKDROP', 'OUTLINE'}
        gz.alpha = 0.0
        gz.color_highlight = 0.8, 0.8, 0.8
        gz.alpha_highlight = 0.2
        gz.scale_basis = (80 * 0.35) / 2 # Same as buttons defined in C
        gz.target_set_operator("view3d.view_center_camera")
        self.frame_camera_gizmo = gz
        self.draw_prepare(context)

    def refresh(self, context):
        self.draw_prepare(context)
        
    def draw_prepare(self, context):
        gz = self.frame_camera_gizmo
        gz_vector = GizmoData(context, offset_y=1).matrix_2d()
        gz.matrix_basis[0][3] = gz_vector[0]
        gz.matrix_basis[1][3] = gz_vector[1]  


def gizmo_register():
    bpy.utils.register_class(ViewLockWidget)
    bpy.utils.register_class(HomeWidget)
    bpy.utils.register_class(ToggleView)
    bpy.utils.register_class(ViewLockGroup)
    bpy.utils.register_class(FrameCameraGroup)


def gizmo_unregister():
    bpy.utils.unregister_class(ViewLockGroup)
    bpy.utils.unregister_class(FrameCameraGroup)
    bpy.utils.unregister_class(ViewLockWidget)
    bpy.utils.unregister_class(HomeWidget)
    bpy.utils.unregister_class(ToggleView)

transform_classes = (
    ArcSideWidget,
    ArcBottomWidget,
    XMoveWidget,
    YMoveWidget,
    ZMoveWidget,
    CameraTransformGroup,
)


def register():
    gizmo_register()
    for cls in transform_classes:
        bpy.utils.register_class(cls)


def unregister():
    gizmo_unregister()
    for cls in reversed(transform_classes):
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()

