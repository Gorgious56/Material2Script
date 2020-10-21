import bpy

new_mat = bpy.data.materials.get('EF_particle_hair_color_G')
if not new_mat:
    new_mat = bpy.data.materials.new('EF_particle_hair_color_G')
    
new_mat.use_nodes = True
node_tree = new_mat.node_tree

nodes = node_tree.nodes
nodes.clear()
    
links = node_tree.links
links.clear()
    
# Nodes :

new_node = nodes.new(type='ShaderNodeBsdfDiffuse')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (235.80970764160156, 199.11444091796875)
new_node.name = 'Diffuse BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.519574761390686, 0.589681088924408, 0.800000011920929, 1.0)
new_node.inputs[1].default_value = 0.0
new_node.inputs[2].default_value = (0.0, 0.0, 0.0)

new_node = nodes.new(type='ShaderNodeMixShader')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (439.19952392578125, 235.810791015625)
new_node.name = 'Mix Shader'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 0.10000002384185791

new_node = nodes.new(type='ShaderNodeBsdfGlossy')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.distribution = 'BECKMANN'
new_node.location = (238.48367309570312, 68.69038391113281)
new_node.name = 'Glossy BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
new_node.inputs[1].default_value = 0.4472135901451111
new_node.inputs[2].default_value = (0.0, 0.0, 0.0)

new_node = nodes.new(type='ShaderNodeBsdfTranslucent')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (449.6629638671875, 32.70069885253906)
new_node.name = 'Translucent BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
new_node.inputs[1].default_value = (0.0, 0.0, 0.0)

new_node = nodes.new(type='ShaderNodeMixShader')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (642.0435791015625, 199.26397705078125)
new_node.name = 'Mix Shader.002'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = 0.19999998807907104

new_node = nodes.new(type='ShaderNodeBsdfTransparent')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (647.4756469726562, 34.12403869628906)
new_node.name = 'Transparent BSDF'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (1.0, 1.0, 1.0, 0.0)

new_node = nodes.new(type='ShaderNodeOutputMaterial')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.is_active_output = True
new_node.location = (1050.7769775390625, 182.18377685546875)
new_node.name = 'Material Output'
new_node.select = False
new_node.target = 'ALL'
new_node.width = 120.0
new_node.inputs[2].default_value = (0.0, 0.0, 0.0)

new_node = nodes.new(type='ShaderNodeHairInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (343.1547546386719, 344.3904724121094)
new_node.name = 'Hair Info.001'
new_node.select = False
new_node.width = 88.9613037109375
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = (0.0, 0.0, 0.0)
new_node.outputs[4].default_value = 0.0
new_node.outputs[0].hide = True
new_node.outputs[2].hide = True
new_node.outputs[3].hide = True

new_node = nodes.new(type='ShaderNodeMixShader')
new_node.color = (0.6079999804496765, 0.01349994819611311, 0.0)
new_node.label = 'TransparencyMixer'
new_node.location = (856.6805419921875, 185.11688232421875)
new_node.name = 'Mix Shader.003'
new_node.select = False
new_node.use_custom_color = True
new_node.width = 150.0
new_node.inputs[0].default_value = 0.0

new_node = nodes.new(type='ShaderNodeMixRGB')
new_node.blend_type = 'MIX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (317.4822998046875, -232.9078826904297)
new_node.name = 'Mix.001'
new_node.select = False
new_node.use_alpha = False
new_node.use_clamp = False
new_node.width = 144.9847412109375
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = (0.1337222456932068, 0.5, 0.06079360842704773, 1.0)
new_node.inputs[2].default_value = (0.5, 0.0, 0.4400014877319336, 1.0)
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)

new_node = nodes.new(type='ShaderNodeMixRGB')
new_node.blend_type = 'MIX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (507.0151062011719, -98.8270034790039)
new_node.name = 'Mix.002'
new_node.select = False
new_node.use_alpha = False
new_node.use_clamp = False
new_node.width = 144.9847412109375
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
new_node.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)

new_node = nodes.new(type='ShaderNodeMixRGB')
new_node.blend_type = 'MIX'
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (43.96592712402344, -404.8095397949219)
new_node.name = 'Mix'
new_node.select = False
new_node.use_alpha = False
new_node.use_clamp = False
new_node.width = 144.9847412109375
new_node.inputs[0].default_value = 0.5
new_node.inputs[1].default_value = (0.5, 0.5, 0.5, 1.0)
new_node.inputs[2].default_value = (0.5, 0.5, 0.5, 1.0)
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)

new_node = nodes.new(type='ShaderNodeTexChecker')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-578.3488159179688, 17.36746597290039)
new_node.name = 'Checker Texture.003'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.0, 0.0, 0.0)
new_node.inputs[1].default_value = (1.0, 0.9888644814491272, 0.9972161054611206, 1.0)
new_node.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.inputs[3].default_value = 3.0
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexChecker')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-578.3488159179688, -150.51806640625)
new_node.name = 'Checker Texture'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.0, 0.0, 0.0)
new_node.inputs[1].default_value = (0.0033736228942871094, 0.0, 1.0, 1.0)
new_node.inputs[2].default_value = (1.0, 0.6074838638305664, 0.0, 1.0)
new_node.inputs[3].default_value = 3.0
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexChecker')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-579.5281372070312, -318.2123718261719)
new_node.name = 'Checker Texture.001'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.0, 0.0, 0.0)
new_node.inputs[1].default_value = (1.0, 0.0, 0.8120222091674805, 1.0)
new_node.inputs[2].default_value = (0.007115019951015711, 1.0, 0.0, 1.0)
new_node.inputs[3].default_value = 3.0
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeTexChecker')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-574.23681640625, -496.1028137207031)
new_node.name = 'Checker Texture.002'
new_node.select = False
new_node.width = 150.0
new_node.inputs[0].default_value = (0.0, 0.0, 0.0)
new_node.inputs[1].default_value = (0.0, 1.0, 0.9939942359924316, 1.0)
new_node.inputs[2].default_value = (1.0, 0.0014712200500071049, 0.0, 1.0)
new_node.inputs[3].default_value = 3.0
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeSeparateRGB')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-293.50048828125, -124.01487731933594)
new_node.name = 'Separate RGB'
new_node.select = False
new_node.width = 106.88275146484375
new_node.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0

new_node = nodes.new(type='ShaderNodeValToRGB')
new_node.color = (0.6079999804496765, 0.027366386726498604, 0.0)
cr = new_node.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
new_stop = cr.elements.new(0.1262764185667038)
new_stop.color = [0.0, 0.0, 0.0, 1.0]
new_stop = cr.elements.new(0.35256919264793396)
new_stop.color = [1.0, 0.0, 0.0, 1.0]
new_stop = cr.elements.new(0.6228208541870117)
new_stop.color = [0.0, 1.0, 0.0, 1.0]
new_stop = cr.elements.new(0.821428656578064)
new_stop.color = [0.0, 0.0, 1.0, 1.0]
removed_black = removed_white = False
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
new_node.label = 'Texture Position Control'
new_node.location = (-748.9963989257812, 300.0088806152344)
new_node.name = 'ColorRamp'
new_node.select = False
new_node.use_custom_color = True
new_node.width = 297.79962158203125
new_node.inputs[0].default_value = 0.5
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

new_node = nodes.new(type='ShaderNodeHairInfo')
new_node.color = (0.6079999804496765, 0.6079999804496765, 0.6079999804496765)
new_node.location = (-861.0517578125, 328.3812561035156)
new_node.name = 'Hair Info'
new_node.select = False
new_node.width = 93.9661865234375
new_node.outputs[0].default_value = 0.0
new_node.outputs[1].default_value = 0.0
new_node.outputs[2].default_value = 0.0
new_node.outputs[3].default_value = (0.0, 0.0, 0.0)
new_node.outputs[4].default_value = 0.0
new_node.outputs[0].hide = True
new_node.outputs[2].hide = True
new_node.outputs[3].hide = True

new_node = nodes.new(type='ShaderNodeValToRGB')
new_node.color = (0.6079999804496765, 0.012484187260270119, 0.0)
cr = new_node.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
new_stop = cr.elements.new(0.75)
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
new_node.label = 'TransparencyControl'
new_node.location = (550.2793579101562, 461.2242736816406)
new_node.name = 'ColorRamp.001'
new_node.use_custom_color = True
new_node.width = 240.0
new_node.inputs[0].default_value = 0.5
new_node.outputs[0].default_value = (0.0, 0.0, 0.0, 1.0)
new_node.outputs[1].default_value = 0.0

# Links :

links.new(nodes["Diffuse BSDF"].outputs[0], nodes["Mix Shader"].inputs[1])    
links.new(nodes["Hair Info"].outputs[1], nodes["ColorRamp"].inputs[0])    
links.new(nodes["Glossy BSDF"].outputs[0], nodes["Mix Shader"].inputs[2])    
links.new(nodes["Hair Info.001"].outputs[1], nodes["ColorRamp.001"].inputs[0])    
links.new(nodes["Mix Shader"].outputs[0], nodes["Mix Shader.002"].inputs[1])    
links.new(nodes["Translucent BSDF"].outputs[0], nodes["Mix Shader.002"].inputs[2])    
links.new(nodes["Mix Shader.002"].outputs[0], nodes["Mix Shader.003"].inputs[1])    
links.new(nodes["Mix Shader.003"].outputs[0], nodes["Material Output"].inputs[0])    
links.new(nodes["Transparent BSDF"].outputs[0], nodes["Mix Shader.003"].inputs[2])    
links.new(nodes["Mix"].outputs[0], nodes["Mix.001"].inputs[1])    
links.new(nodes["Separate RGB"].outputs[1], nodes["Mix.001"].inputs[0])    
links.new(nodes["Mix.001"].outputs[0], nodes["Mix.002"].inputs[1])    
links.new(nodes["Separate RGB"].outputs[2], nodes["Mix.002"].inputs[0])    
links.new(nodes["Separate RGB"].outputs[0], nodes["Mix"].inputs[0])    
links.new(nodes["ColorRamp"].outputs[0], nodes["Separate RGB"].inputs[0])    
links.new(nodes["Checker Texture"].outputs[0], nodes["Mix.001"].inputs[2])    
links.new(nodes["Checker Texture.003"].outputs[0], nodes["Mix.002"].inputs[2])    
links.new(nodes["Checker Texture.001"].outputs[0], nodes["Mix"].inputs[2])    
links.new(nodes["Checker Texture.002"].outputs[0], nodes["Mix"].inputs[1])    
links.new(nodes["Mix.002"].outputs[0], nodes["Diffuse BSDF"].inputs[0])    
