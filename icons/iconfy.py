import bpy
import os
import re

COLLECTION_NAME = "icon_meshes"
MULTIPLIER = "size"
FILENAME = "icon_shapes.py"

CLEAN_ALL = True


def get_objects(collection):
    """ mesh_object.name: variable name - remove any characters after '_' """
    return {ob.name: ob.name.split('_')[0] for ob in collection.objects if ob.type == 'MESH'}


def poly_list(mesh, multiplier):
    """Stringed tuple of multipliered triangle coords - assumes mesh is already triangulated """
    polies_raw = [[mesh.vertices[v].co for v in f.vertices] for f in mesh.polygons ]
    if any(len(polies) > 3 for polies in polies_raw):
        raise ValueError(f"Mesh {mesh.name} is not a triangle mesh")
    verts_raw = [co for f in polies_raw for co in f]
    if len(verts_raw) == 0: # No faces
        verts_raw = [v.co for v in mesh.vertices] # just use the verts
    
    def string(iterable):
        return f"({', '.join([f'{co:.8f}' for co in iterable])})"
    
    def multiply(match_obj):
        for group in match_obj.groups():
            if group:
                return f"{group[0]}{multiplier} * {group[1:]}"
    pattern = "([^\d][\d|\.]*[\d$])"
    verts = f"({','.join([string(co) for co in verts_raw])})"
    return re.sub(pattern, multiply, verts)


def make_icon(obj, name, multiplier):
    """ returns name = (triangle coords multiplied with multiplier) """
    shape = poly_list(obj.data, multiplier)
    return f"{name} = {shape}\n"


def write_icons(outfile, collection, size):
    """ make icon strings out of appropriate meshes """
    icons = get_objects(collection)
    with open(outfile, 'w') as output:
        output.writelines([
            make_icon(bpy.data.objects[icon_obj], icon_shape, size)
            for icon_obj, icon_shape in icons.items()
            ]) 


def clean_data_names(context):
    """ Sanitize object data names in file for better error message """
    for ob in context.scene.objects:
        if not ob.data:
            continue
        ob.data.name = ob.name


def main(filename, collection_name, multiplier, clean_all):
    if clean_all:
        clean_data_names(bpy.context)
    filepath = os.path.join(os.path.split(bpy.context.blend_data.filepath)[0], filename)
    collection = bpy.data.collections[collection_name]        
    write_icons(filepath, collection, multiplier)     

if __name__ == '__main__':

    main(FILENAME, COLLECTION_NAME, MULTIPLIER, CLEAN_ALL)
