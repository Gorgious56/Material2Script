"""
This scripts "serializes" the active material of the currently selected object
And creates a script readable by the Blender API to recreate said Material.
As any Blender script, it is free to use in any way shape or form.
V 1.1 - 2020-10-23 : Fixed NodeSocketVirtual error, add utility reference files for all shader node
V 1.2 - 2021-03-16 : Fix leftover string in code generation

Fork - 2025-03-16 : Switch to __repr__ for serialization (for NodeSocketRotation, in Blender 4.3)

"""

import bpy

from bpy.types import (
    NodeSocketShader,
    NodeSocketVirtual,
    NodeSocketVector,
    NodeSocketVectorDirection,
    NodeSocketVectorXYZ,
    NodeSocketVectorTranslation,
    NodeSocketVectorEuler,
    NodeSocketColor,

    NodeReroute,

    Object,
    Image,
    ImageUser,
    Text,
    ParticleSystem,
    CurveMapping,
    ColorRamp,

    ShaderNodeTree,
)

from mathutils import Vector, Color


ERROR = "~ ERROR ~"

def get_link_statement(link):
    """
    Build the statement to re-create given link
    """
    return f"""\
links.new({link.from_node.path_from_id()}.outputs[{get_socket_index(link.from_socket)}]\
, {link.to_node.path_from_id()}.inputs[{get_socket_index(link.to_socket)}])\
    """


def value_from_socket(socket):
    """
    Returns the evaluated value of a node socket's default value
    """
    # A Shader socket (green dot) doesn't have a default value :
    if isinstance(socket, (NodeSocketShader, NodeSocketVirtual)):
        return ERROR
    elif isinstance(socket, (
            NodeSocketVector,
            NodeSocketVectorXYZ,
            NodeSocketVectorTranslation,
            NodeSocketVectorEuler,
            NodeSocketVectorDirection)):
        return f"{[socket.default_value[i] for i in range(3)]}"
    elif isinstance(socket, NodeSocketColor):
        return f"{[socket.default_value[i] for i in range(4)]}"
    else:
        # Euler objects are handled here, by NodeSocketRotation
        # (by __repr__, which is different from __str__)
        return socket.default_value.__repr__()


class NodeCreator:
    """
    Helper class to programmatically recreate the passed node
    """
    # These props are internal or read-only
    # and aren't useful in the serialization.
    default_props = (
        "dimensions",
        "draw_buttons",
        "draw_buttons_ext",
        "input_template",
        "inputs",
        "internal_links",
        "isAnimationNode",
        "is_registered_node_type",
        "output_template",
        "outputs",
        "poll",
        "poll_instance",
        "rna_type",
        "socket_value_update",
        "type",
        "update",
        "viewLocation",

        "texture_mapping",
        "color_mapping",

        "filepath",

        "cache_point_density",
        "calc_point_density",
        "calc_point_density_minmax",

        "interface",

        "height",
        "show_options",
        "show_preview",
        "show_texture",
        "width_hidden",

        # don't know what these are, but they break the material generated code
        "debug_zone_body_lazy_function_graph",
        "debug_zone_lazy_function_graph",
    )

    def __init__(self, node):
        """
        Initialize the node inputs and outputs,
        and the different fields' default values
        """
        self.node = node
        self.input_default_values = []
        self.output_default_values = []
        if not isinstance(node, NodeReroute):
            for _input in node.inputs:
                self.input_default_values.append(value_from_socket(_input))
            for output in node.outputs:
                self.output_default_values.append(value_from_socket(output))

        self.type = type(node).__name__
        self.properties = []  # Could use an ordered dict instead.
        for prop_name in dir(node):
            if prop_name.startswith("_") or prop_name.startswith("bl_"):
                continue
            if prop_name in NodeCreator.default_props:
                continue
            self.properties.append((prop_name, getattr(node, prop_name)))

    def statements(self):
        """
        Build the chain of statements to programmatically recreate the node
        """
        statements = []
        statements.append(f"new_node = nodes.new(type='{self.type}')")
        self.properties = sorted(self.properties, key=lambda p: p[0])
        for prop, value in self.properties:
            if isinstance(value, ImageUser):
                statements.append(f"""\
img_text = new_node.{prop}
img_text.frame_current = {value.frame_current}
img_text.frame_duration = {value.frame_duration}
img_text.frame_offset = {value.frame_offset}
img_text.frame_start = {value.frame_start}
img_text.use_auto_refresh = {value.use_auto_refresh}
img_text.use_cyclic = {value.use_cyclic}
img_text.tile = {value.tile}\
                """)
                continue
            if isinstance(value, ParticleSystem):
                # /!\ Make sure this is executed after node.object statement
                statements.append(f"""\
if new_node.object:
    new_node.{prop} = new_node.object.particle_systems.get('{value.name}')
                """)
                continue
            if isinstance(value, CurveMapping):
                statements.append(f"""\
map = new_node.{prop}
map.clip_max_x = {value.clip_max_x}
map.clip_max_y = {value.clip_max_y}
map.clip_min_x = {value.clip_min_x}
map.clip_min_y = {value.clip_min_y}
map.tone = '{value.tone}'
map.use_clip = {value.use_clip}\
                """)
                # Remove the 2 starting default points and only these :
                for i, curve in enumerate(value.curves):
                    statements.append(f"map_c = map.curves[{i}]")
                    for point in curve.points:
                        statements.append(f"""\
map_c.points.new({point.location[0]}, {point.location[1]})""")
                    statements.append("""\
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True\
                    """)
                statements.append(f"map.update()")
                continue
            if isinstance(value, ColorRamp):
                statements.append(f"""\
cr = new_node.{prop}
cr.color_mode = '{value.color_mode}'
cr.hue_interpolation = '{value.hue_interpolation}'
cr.interpolation = '{value.interpolation}'\
                """)
                for stop in value.elements:
                    statements.append(f"""new_stop = cr.elements.new({stop.position})
new_stop.color = {[ch for ch in stop.color]}""")
                # Remove the 2 starting default stops and only these :
                statements.append("""\
removed_black = removed_white = False
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True\
                """)
                continue
            if isinstance(value, ShaderNodeTree):
                statements.append(f"""\
ng = bpy.data.node_groups.get('{value.name}')
if not ng:
    new_node.label = \"Missing Node Group : '{value.name}'\"
else:
    new_node.{prop} = ng\
                """)
                continue

            if prop in ("hide", "mute", "use_custom_color"):
                if value:
                    statements.append(f"new_node.{prop} = {value}")
            elif prop == "text" and not value:
                continue
            elif prop in ("select", "shrink"):
                if not value:
                    statements.append(f"new_node.{prop} = {value}")
            elif isinstance(value, str):
                if value:
                    statements.append(f"new_node.{prop} = '{value}'")
            elif isinstance(value, Vector):
                if len(value) == 2:
                    statements.append(
                        f"new_node.{prop} = ({value[0]}, {value[1]})")
                else:
                    statements.append(
                        f"new_node.{prop} = ({value[0]}, {value[1]}, {value[2]})")
            elif isinstance(value, Object):
                statements.append(
                    f"new_node.{prop} = bpy.data.objects.get('{value.name}')")
            elif isinstance(value, Image):
                statements.append(
                    f"new_node.{prop} = bpy.data.images.get('{value.name}')")
            elif isinstance(value, Text):
                if value:
                    statements.append(
                        f"new_node.{prop} = bpy.data.texts.get('{value.name}')")
            elif prop == "parent":
                if value:
                    statements.append(f"""\
parent = nodes.get('{value.name}')
if parent:
    new_node.parent = parent
    while True:
        new_node.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break\
                    """)
            elif isinstance(value, Color):
                statements.append(
                    f"new_node.{prop} = ({value[0]}, {value[1]}, {value[2]})")
            else:
                statements.append(f"new_node.{prop} = {value}")
        for i, dv in enumerate(self.input_default_values):
            if dv == ERROR:
                continue
            statements.append(f"new_node.inputs[{i}].default_value = {dv}")

        for i, dv in enumerate(self.output_default_values):
            if dv == ERROR:
                continue
            statements.append(f"new_node.outputs[{i}].default_value = {dv}")

        if not isinstance(self.node, NodeReroute):
            for _input in self.node.inputs:
                if _input.hide:
                    statements.append(
                        f"new_node.inputs[{get_socket_index(_input)}].hide = True")
            for output in self.node.outputs:
                if output.hide:
                    statements.append(
                        f"new_node.outputs[{get_socket_index(output)}].hide = True")
#        DEBUG Print node location as a label :
#        statements.append("new_node.label = str(new_node.location[0]).split('.')[0] + ', ' + str(new_node.location[1]).split('.')[0]")

        return statements


def serialize_material(mat):
    """
    Returns the ordered statements necessary to build the 
    Mateiral generation script
    """
    node_tree = mat.node_tree
    statements = [f"""\
import bpy
new_mat = bpy.data.materials.get('{mat.name}')
if not new_mat:
    new_mat = bpy.data.materials.new('{mat.name}')
    
new_mat.use_nodes = True
node_tree = new_mat.node_tree
nodes = node_tree.nodes
nodes.clear()
    
links = node_tree.links
links.clear()
    """]

    statements.append("# Nodes :\n")
    for node in node_tree.nodes:
        for st in NodeCreator(node).statements():
            statements.append(st)
        statements.append("")

    if node_tree.links:
        statements.append("# Links :\n")
        for link in node_tree.links:
            statements.append(get_link_statement(link))

    return statements


def write_material_to_text_block(obj):
    """
    Create or overwrite a text block with the same name as the material
    Which contains all the necessary statements to duplicate the material
    """
    if not obj or obj.type not in ('MESH', 'CURVE', 'VOLUME', 'SURFACE', 'FONT', 'META', 'GPENCIL'):
        return
    am = obj.active_material
    if not am or not am.use_nodes:
        return
    statements = serialize_material(am)

    text_block = bpy.data.texts.get(am.name)
    if text_block:
        text_block.clear()
    else:
        text_block = bpy.data.texts.new(am.name)

    for st in statements:
        text_block.write(st)
        text_block.write("\n")

    return text_block


def get_socket_index(socket):
    return socket.path_from_id().split(".")[-1].split("[")[-1][:-1]


if __name__ == "__main__":
    text_block = write_material_to_text_block(bpy.context.active_object)
