import bpy
new_mat = bpy.data.materials.get('Test.002')
if not new_mat:
    new_mat = bpy.data.materials.new('Test.002')
    
new_mat.use_nodes = True
node_tree = new_mat.node_tree
nodes = node_tree.nodes
nodes.clear()
    
links = node_tree.links
links.clear()
    
# Nodes :

new_node = nodes.new(type='NodeFrame')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.label_size = 20
new_node.location = (0.0, 0.0)
new_node.name = 'Frame'
new_node.select = False
new_node.width = 200.0

new_node = nodes.new(type='ShaderNodeBlackbody')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Blackbody'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 1500.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeClamp')
new_node.clamp_type = 'MINMAX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Clamp'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 1.0
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeValToRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
cr = new_node.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
new_stop = cr.elements.new(0.0)
new_stop.color = [0.0, 0.0, 0.0, 1.0]
new_stop = cr.elements.new(1.0)
new_stop.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
new_node.location = (0.0, 0.0)
new_node.name = 'ColorRamp'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = 0.5
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeCombineHSV')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Combine HSV'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.0
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 0.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeCombineRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Combine RGB'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.0
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 0.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeCombineXYZ')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Combine XYZ'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.0
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 0.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeMapRange')
new_node.clamp = True
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.interpolation_type = 'LINEAR'
new_node.location = (0.0, 0.0)
new_node.name = 'Map Range'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = 0.0
new_node.inputs[4].default_value = 1.0
new_node.inputs[5].default_value = 4.0
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeMath')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Math'
new_node.operation = 'ADD'
new_node.select = False
new_node.use_clamp = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = 0.5
new_node.inputs[2].default_value = 0.0
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeRGBToBW')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'RGB to BW'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.5, 0.5, 0.5, 1.0]
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeSeparateHSV')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Separate HSV'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeSeparateRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Separate RGB'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeSeparateXYZ')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Separate XYZ'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeShaderToRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Shader to RGB'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeVectorMath')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Vector Math'
new_node.operation = 'ADD'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]
new_node.inputs[3].default_value = 1.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeWavelength')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Wavelength'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 500.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeAmbientOcclusion')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.inside = False
new_node.location = (0.0, 0.0)
new_node.name = 'Ambient Occlusion'
new_node.only_local = False
new_node.samples = 16
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeAttribute')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Attribute'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeBevel')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Bevel'
new_node.samples = 4
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.05000000074505806
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeCameraData')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Camera Data'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeFresnel')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Fresnel'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 1.4500000476837158
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeNewGeometry')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Geometry'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
new_node.outputs[5].default_value = [0.0, 0.0, 0.0]
new_node.outputs[6].default_value = 0.0
new_node.outputs[7].default_value = 0.0
new_node.outputs[8].default_value = 0.0

new_node = nodes.new(type='NodeGroupInput')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Group Input'
new_node.select = False
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeHairInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Hair Info'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
new_node.outputs[4].default_value = 0.0

new_node = nodes.new(type='ShaderNodeLayerWeight')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Layer Weight'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeLightPath')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Light Path'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = 0.0
new_node.outputs[4].default_value = 0.0
new_node.outputs[5].default_value = 0.0
new_node.outputs[6].default_value = 0.0
new_node.outputs[7].default_value = 0.0
new_node.outputs[8].default_value = 0.0
new_node.outputs[9].default_value = 0.0
new_node.outputs[10].default_value = 0.0
new_node.outputs[11].default_value = 0.0
new_node.outputs[12].default_value = 0.0

new_node = nodes.new(type='ShaderNodeObjectInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Object Info'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = 0.0
new_node.outputs[4].default_value = 0.0

new_node = nodes.new(type='ShaderNodeParticleInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Particle Info'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = 0.0
new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
new_node.outputs[5].default_value = 0.0
new_node.outputs[6].default_value = [0.0, 0.0, 0.0]
new_node.outputs[7].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'RGB'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.5, 0.5, 0.5, 1.0]

new_node = nodes.new(type='ShaderNodeTangent')
new_node.axis = 'Z'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.direction_type = 'RADIAL'
new_node.location = (0.0, 0.0)
new_node.name = 'Tangent'
new_node.select = False
new_node.width = 150.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeTexCoord')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.from_instancer = False
new_node.location = (0.0, 0.0)
new_node.name = 'Texture Coordinate'
new_node.object = None
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
new_node.outputs[3].default_value = [0.0, 0.0, 0.0]
new_node.outputs[4].default_value = [0.0, 0.0, 0.0]
new_node.outputs[5].default_value = [0.0, 0.0, 0.0]
new_node.outputs[6].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeUVAlongStroke')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'UV Along Stroke'
new_node.select = False
new_node.use_tips = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeUVMap')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.from_instancer = False
new_node.location = (0.0, 0.0)
new_node.name = 'UV Map'
new_node.select = False
new_node.width = 150.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeValue')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Value'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = 0.5

new_node = nodes.new(type='ShaderNodeVertexColor')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Vertex Color'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeVolumeInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Volume Info'
new_node.select = False
new_node.width = 140.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = 0.0

new_node = nodes.new(type='ShaderNodeWireframe')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Wireframe'
new_node.select = False
new_node.use_pixel_size = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.009999999776482582
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='NodeReroute')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Reroute'
new_node.select = False
new_node.width = 16.0

new_node = nodes.new(type='ShaderNodeBrightContrast')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Bright/Contrast'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 0.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeGamma')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Gamma'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeHueSaturation')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Hue Saturation Value'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = 1.0
new_node.inputs[4].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeInvert')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Invert'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeLightFalloff')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Light Falloff'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 100.0
new_node.inputs[1].default_value = 0.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeMixRGB')
new_node.blend_type = 'MIX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Mix'
new_node.select = False
new_node.use_alpha = False
new_node.use_clamp = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = [0.5, 0.5, 0.5, 1.0]
new_node.inputs[2].default_value = [0.5, 0.5, 0.5, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeRGBCurve')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
map = new_node.mapping
map.clip_max_x = 1.0
map.clip_max_y = 1.0
map.clip_min_x = 0.0
map.clip_min_y = 0.0
map.tone = 'STANDARD'
map.use_clip = True                
map_c = map.curves[0]
map_c.points.new(0.0, 0.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map_c = map.curves[1]
map_c.points.new(0.0, 0.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map_c = map.curves[2]
map_c.points.new(0.0, 0.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map_c = map.curves[3]
map_c.points.new(0.0, 0.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map.update()
new_node.name = 'RGB Curves'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBump')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.invert = False
new_node.location = (0.0, 0.0)
new_node.name = 'Bump'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = 1.0
new_node.inputs[4].default_value = 1.0
new_node.inputs[5].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeDisplacement')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Displacement'
new_node.select = False
new_node.space = 'OBJECT'
new_node.width = 140.0
new_node.inputs[0].default_value = 0.0
new_node.inputs[1].default_value = 0.5
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeMapping')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Mapping'
new_node.select = False
new_node.vector_type = 'POINT'
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]
new_node.inputs[3].default_value = [1.0, 1.0, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeNormal')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Normal'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 1.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeNormalMap')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Normal Map'
new_node.select = False
new_node.space = 'TANGENT'
new_node.width = 150.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = [0.5, 0.5, 1.0, 1.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeVectorCurve')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
map = new_node.mapping
map.clip_max_x = 1.0
map.clip_max_y = 1.0
map.clip_min_x = -1.0
map.clip_min_y = -1.0
map.tone = 'STANDARD'
map.use_clip = True                
map_c = map.curves[0]
map_c.points.new(-1.0, -1.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map_c = map.curves[1]
map_c.points.new(-1.0, -1.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map_c = map.curves[2]
map_c.points.new(-1.0, -1.0)
map_c.points.new(1.0, 1.0)
removed_start = removed_end = False
for i in range(len(map_c.points) - 1, -1, -1):
    p = map_c.points[i]
    if not removed_start and p.location[0] == map.clip_min_x and p.location[1] == map.clip_min_y:
        map_c.points.remove(p)
        removed_start = True
    if not removed_end and p.location[0] == 1 and p.location[1] == 1:
        map_c.points.remove(p)
        removed_end = True                    
map.update()
new_node.name = 'Vector Curves'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = 1.0
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeVectorDisplacement')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Vector Displacement'
new_node.select = False
new_node.space = 'TANGENT'
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 1.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeVectorRotate')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.invert = False
new_node.location = (0.0, 0.0)
new_node.name = 'Vector Rotate'
new_node.rotation_type = 'AXIS_ANGLE'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]
new_node.inputs[2].default_value = [0.0, 0.0, 1.0]
new_node.inputs[3].default_value = 0.0
new_node.inputs[4].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeVectorTransform')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.convert_from = 'WORLD'
new_node.convert_to = 'OBJECT'
new_node.location = (0.0, 0.0)
new_node.name = 'Vector Transform'
new_node.select = False
new_node.vector_type = 'VECTOR'
new_node.width = 140.0
new_node.inputs[0].default_value = [0.5, 0.5, 0.5]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeOutputAOV')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[1].default_value = 0.0

new_node = nodes.new(type='NodeGroupOutput')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (0.0, 0.0)
new_node.name = 'Group Output'
new_node.select = False
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeOutputLight')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (0.0, 0.0)
new_node.name = 'Light Output'
new_node.select = False
new_node.target = 'ALL'
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeOutputLineStyle')
new_node.blend_type = 'MIX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (0.0, 0.0)
new_node.name = 'Line Style Output'
new_node.select = False
new_node.target = 'ALL'
new_node.use_alpha = False
new_node.use_clamp = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 0.0, 1.0, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = 1.0

new_node = nodes.new(type='ShaderNodeOutputMaterial')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = False
new_node.location = (0.0, 0.0)
new_node.name = 'Material Output.001'
new_node.select = False
new_node.target = 'ALL'
new_node.width = 140.0
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeOutputWorld')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (0.0, 0.0)
new_node.name = 'World Output'
new_node.select = False
new_node.target = 'ALL'
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeScript')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.mode = 'INTERNAL'
new_node.name = 'Script'
new_node.script = None
new_node.select = False
new_node.use_auto_update = False
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeAddShader')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Add Shader'
new_node.select = False
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeBsdfAnisotropic')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'GGX'
new_node.location = (0.0, 0.0)
new_node.name = 'Anisotropic BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.5
new_node.inputs[2].default_value = 0.5
new_node.inputs[3].default_value = 0.0
new_node.inputs[4].default_value = [0.0, 0.0, 0.0]
new_node.inputs[5].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBackground')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Background'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 1.0

new_node = nodes.new(type='ShaderNodeBsdfDiffuse')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Diffuse BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeEmission')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Emission'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[1].default_value = 1.0

new_node = nodes.new(type='ShaderNodeBsdfGlass')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'BECKMANN'
new_node.location = (0.0, 0.0)
new_node.name = 'Glass BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 1.4500000476837158
new_node.inputs[3].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfGlossy')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'GGX'
new_node.location = (0.0, 0.0)
new_node.name = 'Glossy BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.5
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfHair')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.component = 'Reflection'
new_node.location = (0.0, 0.0)
new_node.name = 'Hair BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 0.10000000149011612
new_node.inputs[3].default_value = 1.0
new_node.inputs[4].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeHoldout')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Holdout'
new_node.select = False
new_node.width = 140.0

new_node = nodes.new(type='ShaderNodeMixShader')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Mix Shader'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = 0.5

new_node = nodes.new(type='ShaderNodeBsdfPrincipled')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'GGX'
new_node.location = (0.0, 0.0)
new_node.name = 'Principled BSDF.001'
new_node.select = False
new_node.subsurface_method = 'BURLEY'
new_node.width = 240.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = [1.0, 0.20000000298023224, 0.10000000149011612]
new_node.inputs[3].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[4].default_value = 0.0
new_node.inputs[5].default_value = 0.5
new_node.inputs[6].default_value = 0.0
new_node.inputs[7].default_value = 0.5
new_node.inputs[8].default_value = 0.0
new_node.inputs[9].default_value = 0.0
new_node.inputs[10].default_value = 0.0
new_node.inputs[11].default_value = 0.5
new_node.inputs[12].default_value = 0.0
new_node.inputs[13].default_value = 0.029999999329447746
new_node.inputs[14].default_value = 1.4500000476837158
new_node.inputs[15].default_value = 0.0
new_node.inputs[16].default_value = 0.0
new_node.inputs[17].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[18].default_value = 1.0
new_node.inputs[19].default_value = [0.0, 0.0, 0.0]
new_node.inputs[20].default_value = [0.0, 0.0, 0.0]
new_node.inputs[21].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfHairPrincipled')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Principled Hair BSDF'
new_node.parametrization = 'COLOR'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = [0.01751299947500229, 0.005762999877333641, 0.002059000078588724, 1.0]
new_node.inputs[1].default_value = 0.800000011920929
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[4].default_value = [0.24553099274635315, 0.5199999809265137, 1.3650000095367432]
new_node.inputs[5].default_value = 0.30000001192092896
new_node.inputs[6].default_value = 0.30000001192092896
new_node.inputs[7].default_value = 0.0
new_node.inputs[8].default_value = 1.5499999523162842
new_node.inputs[9].default_value = 0.03490658476948738
new_node.inputs[10].default_value = 0.0
new_node.inputs[11].default_value = 0.0
new_node.inputs[12].default_value = 0.0

new_node = nodes.new(type='ShaderNodeVolumePrincipled')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Principled Volume'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = [0.5, 0.5, 0.5, 1.0]
new_node.inputs[1].default_value = 
new_node.inputs[2].default_value = 1.0
new_node.inputs[3].default_value = density
new_node.inputs[4].default_value = 0.0
new_node.inputs[5].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[6].default_value = 0.0
new_node.inputs[7].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[8].default_value = 0.0
new_node.inputs[9].default_value = [1.0, 1.0, 1.0, 1.0]
new_node.inputs[10].default_value = 1000.0
new_node.inputs[11].default_value = temperature

new_node = nodes.new(type='ShaderNodeBsdfRefraction')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'BECKMANN'
new_node.location = (0.0, 0.0)
new_node.name = 'Refraction BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 1.4500000476837158
new_node.inputs[3].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeEeveeSpecular')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Specular'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = [0.029999999329447746, 0.029999999329447746, 0.029999999329447746, 1.0]
new_node.inputs[2].default_value = 0.20000000298023224
new_node.inputs[3].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[4].default_value = 0.0
new_node.inputs[5].default_value = [0.0, 0.0, 0.0]
new_node.inputs[6].default_value = 0.0
new_node.inputs[7].default_value = 0.0
new_node.inputs[8].default_value = [0.0, 0.0, 0.0]
new_node.inputs[9].default_value = 1.0

new_node = nodes.new(type='ShaderNodeSubsurfaceScattering')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.falloff = 'BURLEY'
new_node.location = (0.0, 0.0)
new_node.name = 'Subsurface Scattering'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = [1.0, 0.20000000298023224, 0.10000000149011612]
new_node.inputs[3].default_value = 0.0
new_node.inputs[4].default_value = 0.0
new_node.inputs[5].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfToon')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.component = 'DIFFUSE'
new_node.location = (0.0, 0.0)
new_node.name = 'Toon BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.5
new_node.inputs[2].default_value = 0.0
new_node.inputs[3].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfTranslucent')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Translucent BSDF'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfTransparent')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Transparent BSDF'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [1.0, 1.0, 1.0, 1.0]

new_node = nodes.new(type='ShaderNodeBsdfVelvet')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Velvet BSDF'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeVolumeAbsorption')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Volume Absorption'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 1.0

new_node = nodes.new(type='ShaderNodeVolumeScatter')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Volume Scatter'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 1.0
new_node.inputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexBrick')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Brick Texture'
new_node.offset = 0.5
new_node.offset_frequency = 2
new_node.select = False
new_node.squash = 1.0
new_node.squash_frequency = 2
new_node.width = 150.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[2].default_value = [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0]
new_node.inputs[3].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[4].default_value = 5.0
new_node.inputs[5].default_value = 0.019999999552965164
new_node.inputs[6].default_value = 0.10000000149011612
new_node.inputs[7].default_value = 0.0
new_node.inputs[8].default_value = 0.5
new_node.inputs[9].default_value = 0.25
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexChecker')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Checker Texture'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[2].default_value = [0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0]
new_node.inputs[3].default_value = 5.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexEnvironment')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.image = None
img_text = new_node.image_user")
img_text.frame_current = 0
img_text.frame_duration = 100
img_text.frame_offset = 0
img_text.frame_start = 1
img_text.use_auto_refresh = False
img_text.use_cyclic = False
img_text.tile = 0                
new_node.interpolation = 'Linear'
new_node.location = (0.0, 0.0)
new_node.name = 'Environment Texture'
new_node.projection = 'EQUIRECTANGULAR'
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeTexGradient')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.gradient_type = 'LINEAR'
new_node.location = (0.0, 0.0)
new_node.name = 'Gradient Texture'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexIES')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.ies = None
new_node.location = (0.0, 0.0)
new_node.mode = 'INTERNAL'
new_node.name = 'IES Texture'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 1.0
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexImage')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.extension = 'REPEAT'
new_node.image = None
img_text = new_node.image_user")
img_text.frame_current = 0
img_text.frame_duration = 100
img_text.frame_offset = 0
img_text.frame_start = 1
img_text.use_auto_refresh = False
img_text.use_cyclic = False
img_text.tile = 0                
new_node.interpolation = 'Linear'
new_node.location = (0.0, 0.0)
new_node.name = 'Image Texture'
new_node.projection = 'FLAT'
new_node.projection_blend = 0.0
new_node.select = False
new_node.width = 240.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexMagic')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Magic Texture'
new_node.select = False
new_node.turbulence_depth = 2
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 5.0
new_node.inputs[2].default_value = 1.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexMusgrave')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.musgrave_dimensions = '3D'
new_node.musgrave_type = 'FBM'
new_node.name = 'Musgrave Texture'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 5.0
new_node.inputs[3].default_value = 2.0
new_node.inputs[4].default_value = 2.0
new_node.inputs[5].default_value = 2.0
new_node.inputs[6].default_value = 0.0
new_node.inputs[7].default_value = 1.0
new_node.outputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexNoise')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Noise Texture'
new_node.noise_dimensions = '3D'
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 5.0
new_node.inputs[3].default_value = 2.0
new_node.inputs[4].default_value = 0.5
new_node.inputs[5].default_value = 0.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeTexPointDensity')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.interpolation = 'Linear'
new_node.location = (0.0, 0.0)
new_node.name = 'Point Density'
new_node.object = None
new_node.particle_color_source = 'PARTICLE_AGE'
new_node.particle_system = None
new_node.point_source = 'PARTICLE_SYSTEM'
new_node.radius = 0.30000001192092896
new_node.resolution = 100
new_node.select = False
new_node.space = 'OBJECT'
new_node.vertex_color_source = 'VERTEX_COLOR'
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexSky')
new_node.air_density = 1.0
new_node.altitude = 0.0
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.dust_density = 1.0
new_node.ground_albedo = 0.30000001192092896
new_node.location = (0.0, 0.0)
new_node.name = 'Sky Texture'
new_node.ozone_density = 1.0
new_node.select = False
new_node.sky_type = 'NISHITA'
new_node.sun_direction = (0.0, 0.0, 1.0)
new_node.sun_disc = True
new_node.sun_elevation = 0.2617993950843811
new_node.sun_intensity = 1.0
new_node.sun_rotation = 0.0
new_node.sun_size = 0.009512044489383698
new_node.turbidity = 2.200000047683716
new_node.width = 150.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeTexVoronoi')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distance = 'EUCLIDEAN'
new_node.feature = 'F1'
new_node.location = (0.0, 0.0)
new_node.name = 'Voronoi Texture'
new_node.select = False
new_node.voronoi_dimensions = '3D'
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = 5.0
new_node.inputs[3].default_value = 1.0
new_node.inputs[4].default_value = 0.5
new_node.inputs[5].default_value = 1.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[2].default_value = [0.0, 0.0, 0.0]
new_node.outputs[3].default_value = 0.0
new_node.outputs[4].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexWave')
new_node.bands_direction = 'X'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (0.0, 0.0)
new_node.name = 'Wave Texture'
new_node.rings_direction = 'X'
new_node.select = False
new_node.wave_profile = 'SIN'
new_node.wave_type = 'BANDS'
new_node.width = 150.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 5.0
new_node.inputs[2].default_value = 0.0
new_node.inputs[3].default_value = 2.0
new_node.inputs[4].default_value = 1.0
new_node.inputs[5].default_value = 0.5
new_node.inputs[6].default_value = 0.0
new_node.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexWhiteNoise')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (1.8810313940048218, 0.0)
new_node.name = 'White Noise Texture'
new_node.noise_dimensions = '3D'
parent = nodes.get('Frame')
if parent:
    new_node.parent = parent
    while True:
        new_node.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
new_node.select = False
new_node.width = 140.0
new_node.inputs[0].default_value = [0.0, 0.0, 0.0]
new_node.inputs[1].default_value = 0.0
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeBsdfPrincipled')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'GGX'
new_node.location = (10.0, 300.0)
new_node.name = 'Principled BSDF'
new_node.subsurface_method = 'BURLEY'
new_node.width = 240.0
new_node.inputs[0].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = [1.0, 0.20000000298023224, 0.10000000149011612]
new_node.inputs[3].default_value = [0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0]
new_node.inputs[4].default_value = 0.0
new_node.inputs[5].default_value = 0.5
new_node.inputs[6].default_value = 0.0
new_node.inputs[7].default_value = 0.5
new_node.inputs[8].default_value = 0.0
new_node.inputs[9].default_value = 0.0
new_node.inputs[10].default_value = 0.0
new_node.inputs[11].default_value = 0.5
new_node.inputs[12].default_value = 0.0
new_node.inputs[13].default_value = 0.029999999329447746
new_node.inputs[14].default_value = 1.4500000476837158
new_node.inputs[15].default_value = 0.0
new_node.inputs[16].default_value = 0.0
new_node.inputs[17].default_value = [0.0, 0.0, 0.0, 1.0]
new_node.inputs[18].default_value = 1.0
new_node.inputs[19].default_value = [0.0, 0.0, 0.0]
new_node.inputs[20].default_value = [0.0, 0.0, 0.0]
new_node.inputs[21].default_value = [0.0, 0.0, 0.0]

new_node = nodes.new(type='ShaderNodeOutputMaterial')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (300.0, 300.0)
new_node.name = 'Material Output'
new_node.target = 'ALL'
new_node.width = 140.0
new_node.inputs[2].default_value = [0.0, 0.0, 0.0]

# Links :

links.new(nodes["Principled BSDF"].outputs[0], nodes["Material Output"].inputs[0])    
