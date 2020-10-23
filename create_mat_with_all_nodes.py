# Community answer from BSE : https://blender.stackexchange.com/a/79981/86891

import bpy

        
mat = bpy.data.materials.new("Test")

mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes.clear()

ddir = lambda data, filter_str: [i for i in dir(data) if i.startswith(filter_str)]
get_nodes = lambda cat: [i for i in getattr(bpy.types, cat).category.items(None)]

cycles_categories = ddir(bpy.types, "NODE_MT_category_SH_NEW")
for cat in cycles_categories: 
    for node in get_nodes(cat):
        nodes.new(type=str(node.nodetype))