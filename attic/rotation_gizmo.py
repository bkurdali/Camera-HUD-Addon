# Example of a custom widget that defines its own geometry.
#
# Usage: Select a light in the 3D view and drag the arrow at it's rear
# to change it's energy value.
#
import bpy
import mathutils
from bpy.types import (
    Gizmo,
    GizmoGroup,
)

# Coordinates (each one is a triangle).


size = 2.0
arcside = ((-size * 0.35355338, size * 0.35355341, size * 0.00000000),(-size * 0.41573477, size * 0.27778512, size * 0.00000000),(-size * 0.46193975, size * 0.19134170, size * 0.00000000),(-size * 0.49039260, size * 0.09754515, size * 0.00000000),(-size * 0.50000000, size * 0.00000000, size * 0.00000000),(-size * 0.49039263, -size * 0.09754515, size * 0.00000000),(-size * 0.46193975, -size * 0.19134170, size * 0.00000000),(-size * 0.41573477, -size * 0.27778512, size * 0.00000000),(-size * 0.35355335, -size * 0.35355341, size * 0.00000000))
arcbottom = ((-size * 0.35355338, -size * 0.35355341, size * 0.00000000),(-size * 0.27778509, -size * 0.41573477, size * 0.00000000),(-size * 0.19134170, -size * 0.46193975, size * 0.00000000),(-size * 0.09754512, -size * 0.49039257, size * 0.00000000),(size * 0.00000000, -size * 0.50000000, size * 0.00000000),(size * 0.09754515, -size * 0.49039263, size * 0.00000000),(size * 0.19134170, -size * 0.46193975, size * 0.00000000),(size * 0.27778518, -size * 0.41573477, size * 0.00000000),(size * 0.35355341, -size * 0.35355332, size * 0.00000000))

moveside = sorted(
    [(size * 0.41864729, -size * 0.08419549, size * 0.00000000),(size * 0.41864729, size * 0.08419549, size * 0.00000000),(size * 0.50284278, size * 0.00000000, size * 0.00000000)],
    key=lambda x: x[1],
    )
moveup = sorted(
    ((size * 0.08419552, size * 0.41864729, size * 0.00000000),(-size * 0.08419549, size * 0.41864729, size * 0.00000000),(size * 0.00000006, size * 0.50284278, size * 0.00000000)),
    key=lambda x: x[0],
    )
movedepth = ((-size * 0.05862415, size * 0.06000002, size * 0.00000000),(-size * 0.00862414, size * 0.00000000, size * 0.00000000),(size * 0.05862415, -size * 0.06000002, size * 0.00000000),(size * 0.00862414, size * 0.00000000, size * 0.00000000),(-size * 0.05862415, -size * 0.06000002, size * 0.00000000),(size * 0.05862415, size * 0.06000002, size * 0.00000000))

class Transformer(Gizmo):
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
            self.custom_shape = self.new_custom_shape('LINE_STRIP', arcside)


class ArcBottomWidget(Transformer):
    bl_idname = "VIEW3D_GT_arc_bottom_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('LINE_STRIP', arcbottom)


class XMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_xmove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('LINE_STRIP', moveside)


class YMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_ymove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('LINE_STRIP', moveup)


class ZMoveWidget(Transformer):
    bl_idname = "VIEW3D_GT_zmove_widget"

    def setup(self):
        if not hasattr(self, "custom_shape"):
            self.custom_shape = self.new_custom_shape('LINE_STRIP', movedepth)


class CameraTransformGroup(GizmoGroup):
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
            context.region_data.view_perspective == 'CAMERA' and context.active_object == cam and len(selected) == 1 and cam in selected
            )

    def setup(self, context):
        # Assign the 'offset' target property to the light energy.
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

classes = (
    ArcSideWidget,
    ArcBottomWidget,
    XMoveWidget,
    YMoveWidget,
    ZMoveWidget,
    CameraTransformGroup,
)

for cls in classes:
    bpy.utils.register_class(cls)
