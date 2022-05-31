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
size = 0.3
custom_shape_verts = (
    (0, 0, 0), (size, size, 0), (size, 0, 0),
    (0, size, 0), (size, size, 0), (0, 0, 0),
    )

locked = ((size * 0.3862968683242798, size * 0.8769386410713196, size * 0.0), (size * 0.49802443385124207, size * 0.8148969411849976, size * 0.0), (size * 0.49802443385124207, size * 0.8995057940483093, size * 0.0), (size * 0.49802443385124207, size * 0.8148969411849976, size * 0.0), (size * 0.3862968683242798, size * 0.8769386410713196, size * 0.0), (size * 0.41922473907470703, size * 0.798980712890625, size * 0.0), (size * 0.3862968683242798, size * 0.8769386410713196, size * 0.0), (size * 0.295041024684906, size * 0.8154029846191406, size * 0.0), (size * 0.41922473907470703, size * 0.798980712890625, size * 0.0), (size * 0.641185462474823, size * 0.7555806040763855, size * 0.0), (size * 0.7625436782836914, size * 0.7241472005844116, size * 0.0), (size * 0.7010079026222229, size * 0.8154030442237854, size * 0.0), (size * 0.7010079026222229, size * 0.8154030442237854, size * 0.0), (size * 0.6097519993782043, size * 0.8769387006759644, size * 0.0), (size * 0.5768241286277771, size * 0.798980712890625, size * 0.0), (size * 0.5768241286277771, size * 0.798980712890625, size * 0.0), (size * 0.641185462474823, size * 0.7555806040763855, size * 0.0), (size * 0.7010079026222229, size * 0.8154030442237854, size * 0.0), (size * 0.23350536823272705, size * 0.7241472005844116, size * 0.0), (size * 0.3548634350299835, size * 0.7555806040763855, size * 0.0), (size * 0.295041024684906, size * 0.8154029846191406, size * 0.0), (size * 0.6097519993782043, size * 0.8769387006759644, size * 0.0), (size * 0.49802443385124207, size * 0.8148969411849976, size * 0.0), (size * 0.5768241286277771, size * 0.798980712890625, size * 0.0), (size * 0.23350536823272705, size * 0.7241472005844116, size * 0.0), (size * 0.31146329641342163, size * 0.6912193298339844, size * 0.0), (size * 0.3548634350299835, size * 0.7555806040763855, size * 0.0), (size * 0.6845856308937073, size * 0.6912193298339844, size * 0.0), (size * 0.7625436782836914, size * 0.7241472005844116, size * 0.0), (size * 0.641185462474823, size * 0.7555806040763855, size * 0.0), (size * 0.21093827486038208, size * 0.6124196648597717, size * 0.0), (size * 0.31146329641342163, size * 0.6912193298339844, size * 0.0), (size * 0.23350536823272705, size * 0.7241472005844116, size * 0.0), (size * 0.6845856308937073, size * 0.6912193298339844, size * 0.0), (size * 0.7851107120513916, size * 0.6124196648597717, size * 0.0), (size * 0.7625436782836914, size * 0.7241472005844116, size * 0.0), (size * 0.21093827486038208, size * 0.6124196648597717, size * 0.0), (size * 0.2955470681190491, size * 0.6124196648597717, size * 0.0), (size * 0.31146329641342163, size * 0.6912193298339844, size * 0.0), (size * 0.7005018591880798, size * 0.6124196648597717, size * 0.0), (size * 0.7851107120513916, size * 0.6124196648597717, size * 0.0), (size * 0.6845856308937073, size * 0.6912193298339844, size * 0.0), (size * 0.1658715307712555, size * 0.04843902587890625, size * 0.0), (size * 0.21093827486038208, size * 0.6124196648597717, size * 0.0), (size * 0.1658715307712555, size * 0.6124196648597717, size * 0.0), (size * 0.1658715307712555, size * 0.04843902587890625, size * 0.0), (size * 0.2955470681190491, size * 0.6124196648597717, size * 0.0), (size * 0.21093827486038208, size * 0.6124196648597717, size * 0.0), (size * 0.1658715307712555, size * 0.04843902587890625, size * 0.0), (size * 0.7005018591880798, size * 0.6124196648597717, size * 0.0), (size * 0.2955470681190491, size * 0.6124196648597717, size * 0.0), (size * 0.1658715307712555, size * 0.04843902587890625, size * 0.0), (size * 0.830177366733551, size * 0.04843902587890625, size * 0.0), (size * 0.7005018591880798, size * 0.6124196648597717, size * 0.0), (size * 0.830177366733551, size * 0.04843902587890625, size * 0.0), (size * 0.830177366733551, size * 0.6124196648597717, size * 0.0), (size * 0.7851107120513916, size * 0.6124196648597717, size * 0.0), (size * 0.3548634350299835, size * 0.7555806040763855, size * 0.0), (size * 0.41922473907470703, size * 0.798980712890625, size * 0.0), (size * 0.295041024684906, size * 0.8154029846191406, size * 0.0), (size * 0.49802443385124207, size * 0.8148969411849976, size * 0.0), (size * 0.6097519993782043, size * 0.8769387006759644, size * 0.0), (size * 0.49802443385124207, size * 0.8995057940483093, size * 0.0), (size * 0.830177366733551, size * 0.04843902587890625, size * 0.0), (size * 0.7851107120513916, size * 0.6124196648597717, size * 0.0), (size * 0.7005018591880798, size * 0.6124196648597717, size * 0.0))

unlocked = ((size * 0.3347567915916443, size * 0.7555806040763855, size * 0.0), (size * 0.44880616664886475, size * 0.7241472005844116, size * 0.0), (size * 0.3987385034561157, size * 0.8154029846191406, size * 0.0), (size * 0.17789548635482788, size * 0.798980712890625, size * 0.0), (size * 0.23358383774757385, size * 0.8148969411849976, size * 0.0), (size * 0.14267821609973907, size * 0.8769387006759644, size * 0.0), (size * 0.23358383774757385, size * 0.8148969411849976, size * 0.0), (size * 0.32448944449424744, size * 0.8769386410713196, size * 0.0), (size * 0.23358383774757385, size * 0.8995057940483093, size * 0.0), (size * 0.3987385034561157, size * 0.8154029846191406, size * 0.0), (size * 0.32448944449424744, size * 0.8769386410713196, size * 0.0), (size * 0.2892721891403198, size * 0.798980712890625, size * 0.0), (size * 0.2892721891403198, size * 0.798980712890625, size * 0.0), (size * 0.3347567915916443, size * 0.7555806040763855, size * 0.0), (size * 0.3987385034561157, size * 0.8154029846191406, size * 0.0), (size * 0.13241085410118103, size * 0.7555806040763855, size * 0.0), (size * 0.17789548635482788, size * 0.798980712890625, size * 0.0), (size * 0.0684291273355484, size * 0.8154030442237854, size * 0.0), (size * 0.0684291273355484, size * 0.8154030442237854, size * 0.0), (size * 0.17789548635482788, size * 0.798980712890625, size * 0.0), (size * 0.14267821609973907, size * 0.8769387006759644, size * 0.0), (size * 0.018361438065767288, size * 0.7241472005844116, size * 0.0), (size * 0.10173964500427246, size * 0.6912193298339844, size * 0.0), (size * 0.13241085410118103, size * 0.7555806040763855, size * 0.0), (size * 0.36542800068855286, size * 0.6912193298339844, size * 0.0), (size * 0.44880616664886475, size * 0.7241472005844116, size * 0.0), (size * 0.3347567915916443, size * 0.7555806040763855, size * 0.0), (size * 0.0, size * 0.6124196648597717, size * 0.0), (size * 0.10173964500427246, size * 0.6912193298339844, size * 0.0), (size * 0.018361438065767288, size * 0.7241472005844116, size * 0.0), (size * 0.36542800068855286, size * 0.6912193298339844, size * 0.0), (size * 0.46716758608818054, size * 0.6124196648597717, size * 0.0), (size * 0.44880616664886475, size * 0.7241472005844116, size * 0.0), (size * 0.0, size * 0.6124196648597717, size * 0.0), (size * 0.09049153327941895, size * 0.6124196648597717, size * 0.0), (size * 0.10173964500427246, size * 0.6912193298339844, size * 0.0), (size * 0.376676082611084, size * 0.6124196648597717, size * 0.0), (size * 0.46716758608818054, size * 0.6124196648597717, size * 0.0), (size * 0.36542800068855286, size * 0.6912193298339844, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 0.376676082611084, size * 0.6124196648597717, size * 0.0), (size * 0.33569416403770447, size * 0.6124196648597717, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 0.46716758608818054, size * 0.6124196648597717, size * 0.0), (size * 0.376676082611084, size * 0.6124196648597717, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 1.0, size * 0.6124196648597717, size * 0.0), (size * 0.46716758608818054, size * 0.6124196648597717, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 0.9082762598991394, size * 0.5257151126861572, size * 0.0), (size * 1.0, size * 0.6124196648597717, size * 0.0), (size * 0.9082762598991394, size * 0.5257151126861572, size * 0.0), (size * 1.0, size * 0.04843902587890625, size * 0.0), (size * 1.0, size * 0.6124196648597717, size * 0.0), (size * 0.33569416403770447, size * 0.04843902587890625, size * 0.0), (size * 0.4274178743362427, size * 0.13514354825019836, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 0.9082762598991394, size * 0.13514354825019836, size * 0.0), (size * 1.0, size * 0.04843902587890625, size * 0.0), (size * 0.9082762598991394, size * 0.5257151126861572, size * 0.0), (size * 0.33569416403770447, size * 0.04843902587890625, size * 0.0), (size * 0.9082762598991394, size * 0.13514354825019836, size * 0.0), (size * 0.4274178743362427, size * 0.13514354825019836, size * 0.0), (size * 0.33569416403770447, size * 0.04843902587890625, size * 0.0), (size * 1.0, size * 0.04843902587890625, size * 0.0), (size * 0.9082762598991394, size * 0.13514354825019836, size * 0.0), (size * 0.32448944449424744, size * 0.8769386410713196, size * 0.0), (size * 0.23358383774757385, size * 0.8148969411849976, size * 0.0), (size * 0.2892721891403198, size * 0.798980712890625, size * 0.0), (size * 0.018361438065767288, size * 0.7241472005844116, size * 0.0), (size * 0.13241085410118103, size * 0.7555806040763855, size * 0.0), (size * 0.0684291273355484, size * 0.8154030442237854, size * 0.0), (size * 0.14267821609973907, size * 0.8769387006759644, size * 0.0), (size * 0.23358383774757385, size * 0.8148969411849976, size * 0.0), (size * 0.23358383774757385, size * 0.8995057940483093, size * 0.0), (size * 0.33569416403770447, size * 0.04843902587890625, size * 0.0), (size * 0.4274178743362427, size * 0.5257151126861572, size * 0.0), (size * 0.33569416403770447, size * 0.6124196648597717, size * 0.0))

class ButtonWidget(bpy.types.Gizmo):
    """ Custom 'button' gizmo for camera """
    bl_idname = "VIEW3D_GT_button_widget"
    
    locked: bpy.props.BoolProperty(default=True)

    def shape(self):
        return self.locked_shape if self.locked else self.unlocked_shape

    def draw(self, context):
        self.draw_custom_shape(self.shape())

    def draw_select(self, context, select_id):
        self.draw_custom_shape(self.shape(), select_id=select_id)

    def setup(self):
        # TODO remove the size offset once matrix is figured out
        if not hasattr(self, "unlocked_shape"):
            self.unlocked_shape = self.new_custom_shape(
                'TRIS', [(co[0] - size, co[1], co[2]) for co in unlocked])
        if not hasattr(self, "locked_shape"):
            self.locked_shape = self.new_custom_shape(
                'TRIS', [(co[0] - size, co[1], co[2]) for co in locked])


def gizmo_matrix(context):
    """ Get the gizmo matrix so it sits next to the camera frame """
    space = context.space_data
    scene = context.scene
    ob = space.camera
    cam = ob.data
    
    z = cam.clip_start + .01
    
    gizmo_size = context.preferences.view.gizmo_size

    
    res_x, res_y = (scene.render.resolution_x, scene.render.resolution_y)
    landscape = res_x > res_y
    angle = cam.angle_x / 2 if landscape else cam.angle_y / 2
    base = math.tan(angle) * z
    x = base if landscape else base * res_x / res_y
    y = base * res_y / res_x if landscape else base
    largest = max(x, y)

    print()
    loc = mathutils.Vector((
        x + largest * 2 * cam.shift_x ,
        -y + largest * 2 * cam.shift_y,
        -z
        ))
    print(loc)

    loc2d = bpy_extras.view3d_utils.location_3d_to_region_2d(
        context.region,
        context.space_data.region_3d,
        loc)

    origin2d = loc2d - mathutils.Vector((gizmo_size * size, 0))

    loc = bpy_extras.view3d_utils.region_2d_to_location_3d(
        context.region,
        context.space_data.region_3d,
        origin2d,
        loc
        )

    print(loc)
    loc_cam = mathutils.Matrix.Translation(loc) @ ob.matrix_world 
    loc_cam = ob.matrix_world @ mathutils.Matrix.Translation(loc)
    
    return loc_cam.normalized()


def gizmo_color(context):
    """ Color the gizmo based on lock_camera """
    space = context.space_data
    return context.preferences.themes['Default'].user_interface.gizmo_primary
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
