import bpy

from rna_prop_ui import rna_idprop_ui_create

from mathutils import Color


def create(obj):  # noqa
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(6):
        arm.rigify_colors.add()

    arm.rigify_colors[0].name = "Root"
    arm.rigify_colors[0].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[0].normal = Color((0.4353, 0.1843, 0.4157))
    arm.rigify_colors[0].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[0].standard_colors_lock = True
    arm.rigify_colors[1].name = "IK"
    arm.rigify_colors[1].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[1].normal = Color((0.6039, 0.0000, 0.0000))
    arm.rigify_colors[1].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[1].standard_colors_lock = True
    arm.rigify_colors[2].name = "Special"
    arm.rigify_colors[2].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[2].normal = Color((0.9569, 0.7882, 0.0471))
    arm.rigify_colors[2].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[2].standard_colors_lock = True
    arm.rigify_colors[3].name = "Tweak"
    arm.rigify_colors[3].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[3].normal = Color((0.0392, 0.2118, 0.5804))
    arm.rigify_colors[3].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[3].standard_colors_lock = True
    arm.rigify_colors[4].name = "FK"
    arm.rigify_colors[4].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[4].normal = Color((0.1176, 0.5686, 0.0353))
    arm.rigify_colors[4].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[4].standard_colors_lock = True
    arm.rigify_colors[5].name = "Extra"
    arm.rigify_colors[5].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[5].normal = Color((0.9686, 0.2510, 0.0941))
    arm.rigify_colors[5].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[5].standard_colors_lock = True

    bone_collections = {}

    for bcoll in list(arm.collections):
        arm.collections.remove(bcoll)

    def add_bone_collection(name, *, ui_row=0, ui_title='', sel_set=False, color_set_id=0):
        new_bcoll = arm.collections.new(name)
        new_bcoll.rigify_ui_row = ui_row
        new_bcoll.rigify_ui_title = ui_title
        new_bcoll.rigify_sel_set = sel_set
        new_bcoll.rigify_color_set_id = color_set_id
        bone_collections[name] = new_bcoll

    def assign_bone_collections(pose_bone, *coll_names):
        assert not len(pose_bone.bone.collections)
        for name in coll_names:
            bone_collections[name].assign(pose_bone)

    def assign_bone_collection_refs(params, attr_name, *coll_names):
        ref_list = getattr(params, attr_name + '_coll_refs', None)
        if ref_list is not None:
            for name in coll_names:
                ref_list.add().set_collection(bone_collections[name])

    add_bone_collection('Face', ui_row=1, color_set_id=5)
    add_bone_collection('Face (Primary)', ui_row=2, color_set_id=2)
    add_bone_collection('Face (Secondary)', ui_row=2, color_set_id=3)
    add_bone_collection('Torso', ui_row=3, color_set_id=3)
    add_bone_collection('Torso (Tweak)', ui_row=4, color_set_id=4)
    add_bone_collection('Fingers', ui_row=5, color_set_id=6)
    add_bone_collection('Fingers (Detail)', ui_row=6, color_set_id=5)
    add_bone_collection('Arm.L (IK)', ui_row=7, color_set_id=2)
    add_bone_collection('Arm.L (FK)', ui_row=8, color_set_id=5)
    add_bone_collection('Arm.L (Tweak)', ui_row=9, color_set_id=4)
    add_bone_collection('Arm.R (IK)', ui_row=7, color_set_id=2)
    add_bone_collection('Arm.R (FK)', ui_row=8, color_set_id=5)
    add_bone_collection('Arm.R (Tweak)', ui_row=9, color_set_id=4)
    add_bone_collection('Leg.L (IK)', ui_row=10, color_set_id=2)
    add_bone_collection('Leg.L (FK)', ui_row=11, color_set_id=5)
    add_bone_collection('Leg.L (Tweak)', ui_row=12, color_set_id=4)
    add_bone_collection('Leg.R (IK)', ui_row=10, color_set_id=2)
    add_bone_collection('Leg.R (FK)', ui_row=11, color_set_id=5)
    add_bone_collection('Leg.R (Tweak)', ui_row=12, color_set_id=4)
    add_bone_collection('Root', ui_row=15, color_set_id=1)

    bones = {}

    bone = arm.edit_bones.new('spine')
    bone.head = 0.0000, 0.0106, 0.9675
    bone.tail = 0.0000, -0.0040, 1.1192
    bone.roll = -0.0000
    bone.use_connect = False
    bones['spine'] = bone.name
    bone = arm.edit_bones.new('spine.001')
    bone.head = 0.0000, -0.0040, 1.1192
    bone.tail = 0.0000, 0.0094, 1.2186
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine']]
    bones['spine.001'] = bone.name
    bone = arm.edit_bones.new('thigh.L')
    bone.head = 0.0903, 0.0240, 0.9346
    bone.tail = 0.1328, 0.0397, 0.5159
    bone.roll = 1.5921
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.L'] = bone.name
    bone = arm.edit_bones.new('thigh.R')
    bone.head = -0.0903, 0.0240, 0.9346
    bone.tail = -0.1328, 0.0397, 0.5159
    bone.roll = -1.5921
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['thigh.R'] = bone.name
    bone = arm.edit_bones.new('spine.002')
    bone.head = 0.0000, 0.0094, 1.2186
    bone.tail = 0.0000, 0.0329, 1.3880
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['spine.002'] = bone.name
    bone = arm.edit_bones.new('shin.L')
    bone.head = 0.1328, 0.0397, 0.5159
    bone.tail = 0.1521, 0.0738, 0.1240
    bone.roll = 1.5925
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.L']]
    bones['shin.L'] = bone.name
    bone = arm.edit_bones.new('shin.R')
    bone.head = -0.1328, 0.0397, 0.5159
    bone.tail = -0.1521, 0.0738, 0.1240
    bone.roll = -1.5925
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thigh.R']]
    bones['shin.R'] = bone.name
    bone = arm.edit_bones.new('spine.003')
    bone.head = 0.0000, 0.0329, 1.3880
    bone.tail = 0.0000, 0.0552, 1.4832
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.002']]
    bones['spine.003'] = bone.name
    bone = arm.edit_bones.new('foot.L')
    bone.head = 0.1521, 0.0738, 0.1240
    bone.tail = 0.1626, -0.0570, 0.0162
    bone.roll = -0.0423
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.L']]
    bones['foot.L'] = bone.name
    bone = arm.edit_bones.new('foot.R')
    bone.head = -0.1521, 0.0738, 0.1240
    bone.tail = -0.1626, -0.0570, 0.0162
    bone.roll = 0.0423
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['shin.R']]
    bones['foot.R'] = bone.name
    bone = arm.edit_bones.new('spine.004')
    bone.head = 0.0000, 0.0552, 1.4832
    bone.tail = 0.0000, 0.0561, 1.6126
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.004'] = bone.name
    bone = arm.edit_bones.new('shoulder.L')
    bone.head = 0.0235, 0.0740, 1.4291
    bone.tail = 0.1243, 0.1036, 1.4399
    bone.roll = -1.5708
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.L'] = bone.name
    bone = arm.edit_bones.new('shoulder.R')
    bone.head = -0.0235, 0.0740, 1.4291
    bone.tail = -0.1243, 0.1036, 1.4399
    bone.roll = 1.5708
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['shoulder.R'] = bone.name
    bone = arm.edit_bones.new('toe.L')
    bone.head = 0.1626, -0.0570, 0.0162
    bone.tail = 0.1545, -0.1203, 0.0144
    bone.roll = -0.2618
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.L']]
    bones['toe.L'] = bone.name
    bone = arm.edit_bones.new('heel.02.L')
    bone.head = 0.1411, 0.1219, 0.0000
    bone.tail = 0.2211, 0.1219, 0.0000
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['foot.L']]
    bones['heel.02.L'] = bone.name
    bone = arm.edit_bones.new('toe.R')
    bone.head = -0.1626, -0.0570, 0.0162
    bone.tail = -0.1545, -0.1203, 0.0144
    bone.roll = 0.2618
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['foot.R']]
    bones['toe.R'] = bone.name
    bone = arm.edit_bones.new('heel.02.R')
    bone.head = -0.1411, 0.1219, 0.0000
    bone.tail = -0.2211, 0.1219, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['foot.R']]
    bones['heel.02.R'] = bone.name
    bone = arm.edit_bones.new('spine.005')
    bone.head = 0.0000, 0.0561, 1.6126
    bone.tail = 0.0000, 0.0610, 1.7299
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['spine.005'] = bone.name
    bone = arm.edit_bones.new('upper_arm.L')
    bone.head = 0.1153, 0.0751, 1.4071
    bone.tail = 0.3201, 0.1163, 1.2145
    bone.roll = -1.6802
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.L']]
    bones['upper_arm.L'] = bone.name
    bone = arm.edit_bones.new('upper_arm.R')
    bone.head = -0.1153, 0.0751, 1.4071
    bone.tail = -0.3201, 0.1163, 1.2145
    bone.roll = 1.6802
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.R']]
    bones['upper_arm.R'] = bone.name
    bone = arm.edit_bones.new('forearm.L')
    bone.head = 0.3201, 0.1163, 1.2145
    bone.tail = 0.4874, 0.0301, 1.0781
    bone.roll = -1.5334
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.L']]
    bones['forearm.L'] = bone.name
    bone = arm.edit_bones.new('forearm.R')
    bone.head = -0.3201, 0.1163, 1.2145
    bone.tail = -0.4874, 0.0301, 1.0781
    bone.roll = 1.5334
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['upper_arm.R']]
    bones['forearm.R'] = bone.name
    bone = arm.edit_bones.new('hand.L')
    bone.head = 0.4874, 0.0301, 1.0781
    bone.tail = 0.5474, -0.0116, 1.0188
    bone.roll = 0.7854
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.L']]
    bones['hand.L'] = bone.name
    bone = arm.edit_bones.new('hand.R')
    bone.head = -0.4874, 0.0301, 1.0781
    bone.tail = -0.5474, -0.0116, 1.0188
    bone.roll = -0.7854
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['forearm.R']]
    bones['hand.R'] = bone.name
    bone = arm.edit_bones.new('f_index.01.L')
    bone.head = 0.5381, -0.0300, 1.0126
    bone.tail = 0.5530, -0.0396, 0.9820
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.L']]
    bones['f_index.01.L'] = bone.name
    bone = arm.edit_bones.new('thumb.01.L')
    bone.head = 0.4934, -0.0050, 1.0437
    bone.tail = 0.4942, -0.0311, 1.0260
    bone.roll = 0.2618
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.L']]
    bones['thumb.01.L'] = bone.name
    bone = arm.edit_bones.new('f_middle.01.L')
    bone.head = 0.5508, -0.0113, 1.0106
    bone.tail = 0.5683, -0.0203, 0.9772
    bone.roll = -0.2618
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.L']]
    bones['f_middle.01.L'] = bone.name
    bone = arm.edit_bones.new('f_ring.01.L')
    bone.head = 0.5525, 0.0086, 1.0073
    bone.tail = 0.5690, 0.0023, 0.9790
    bone.roll = -0.5236
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.L']]
    bones['f_ring.01.L'] = bone.name
    bone = arm.edit_bones.new('f_pinky.01.L')
    bone.head = 0.5489, 0.0272, 1.0076
    bone.tail = 0.5635, 0.0259, 0.9815
    bone.roll = -0.7854
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.L']]
    bones['f_pinky.01.L'] = bone.name
    bone = arm.edit_bones.new('f_index.01.R')
    bone.head = -0.5381, -0.0300, 1.0126
    bone.tail = -0.5530, -0.0396, 0.9820
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.R']]
    bones['f_index.01.R'] = bone.name
    bone = arm.edit_bones.new('thumb.01.R')
    bone.head = -0.4934, -0.0050, 1.0437
    bone.tail = -0.4942, -0.0311, 1.0260
    bone.roll = -0.2618
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.R']]
    bones['thumb.01.R'] = bone.name
    bone = arm.edit_bones.new('f_middle.01.R')
    bone.head = -0.5508, -0.0113, 1.0106
    bone.tail = -0.5683, -0.0203, 0.9772
    bone.roll = 0.2618
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.R']]
    bones['f_middle.01.R'] = bone.name
    bone = arm.edit_bones.new('f_ring.01.R')
    bone.head = -0.5525, 0.0086, 1.0073
    bone.tail = -0.5690, 0.0023, 0.9790
    bone.roll = 0.5236
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.R']]
    bones['f_ring.01.R'] = bone.name
    bone = arm.edit_bones.new('f_pinky.01.R')
    bone.head = -0.5489, 0.0272, 1.0076
    bone.tail = -0.5635, 0.0259, 0.9815
    bone.roll = 0.7854
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['hand.R']]
    bones['f_pinky.01.R'] = bone.name
    bone = arm.edit_bones.new('f_index.02.L')
    bone.head = 0.5530, -0.0396, 0.9820
    bone.tail = 0.5585, -0.0461, 0.9554
    bone.roll = 0.3044
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_index.01.L']]
    bones['f_index.02.L'] = bone.name
    bone = arm.edit_bones.new('thumb.02.L')
    bone.head = 0.4942, -0.0311, 1.0260
    bone.tail = 0.4964, -0.0521, 0.9998
    bone.roll = 0.2020
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thumb.01.L']]
    bones['thumb.02.L'] = bone.name
    bone = arm.edit_bones.new('f_middle.02.L')
    bone.head = 0.5683, -0.0203, 0.9772
    bone.tail = 0.5757, -0.0269, 0.9498
    bone.roll = 0.0022
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_middle.01.L']]
    bones['f_middle.02.L'] = bone.name
    bone = arm.edit_bones.new('f_ring.02.L')
    bone.head = 0.5690, 0.0023, 0.9790
    bone.tail = 0.5748, -0.0027, 0.9518
    bone.roll = -0.1482
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_ring.01.L']]
    bones['f_ring.02.L'] = bone.name
    bone = arm.edit_bones.new('f_pinky.02.L')
    bone.head = 0.5635, 0.0259, 0.9815
    bone.tail = 0.5717, 0.0239, 0.9583
    bone.roll = -0.6040
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_pinky.01.L']]
    bones['f_pinky.02.L'] = bone.name
    bone = arm.edit_bones.new('f_index.02.R')
    bone.head = -0.5530, -0.0396, 0.9820
    bone.tail = -0.5585, -0.0461, 0.9554
    bone.roll = -0.3044
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_index.01.R']]
    bones['f_index.02.R'] = bone.name
    bone = arm.edit_bones.new('thumb.02.R')
    bone.head = -0.4942, -0.0311, 1.0260
    bone.tail = -0.4964, -0.0521, 0.9998
    bone.roll = -0.2020
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thumb.01.R']]
    bones['thumb.02.R'] = bone.name
    bone = arm.edit_bones.new('f_middle.02.R')
    bone.head = -0.5683, -0.0203, 0.9772
    bone.tail = -0.5757, -0.0269, 0.9498
    bone.roll = -0.0022
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_middle.01.R']]
    bones['f_middle.02.R'] = bone.name
    bone = arm.edit_bones.new('f_ring.02.R')
    bone.head = -0.5690, 0.0023, 0.9790
    bone.tail = -0.5748, -0.0027, 0.9518
    bone.roll = 0.1482
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_ring.01.R']]
    bones['f_ring.02.R'] = bone.name
    bone = arm.edit_bones.new('f_pinky.02.R')
    bone.head = -0.5635, 0.0259, 0.9815
    bone.tail = -0.5717, 0.0239, 0.9583
    bone.roll = 0.6040
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_pinky.01.R']]
    bones['f_pinky.02.R'] = bone.name
    bone = arm.edit_bones.new('f_index.03.L')
    bone.head = 0.5585, -0.0461, 0.9554
    bone.tail = 0.5666, -0.0537, 0.9317
    bone.roll = 0.1551
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_index.02.L']]
    bones['f_index.03.L'] = bone.name
    bone = arm.edit_bones.new('thumb.03.L')
    bone.head = 0.4964, -0.0521, 0.9998
    bone.tail = 0.4970, -0.0689, 0.9784
    bone.roll = 0.3097
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thumb.02.L']]
    bones['thumb.03.L'] = bone.name
    bone = arm.edit_bones.new('f_middle.03.L')
    bone.head = 0.5757, -0.0269, 0.9498
    bone.tail = 0.5869, -0.0337, 0.9254
    bone.roll = -0.1971
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_middle.02.L']]
    bones['f_middle.03.L'] = bone.name
    bone = arm.edit_bones.new('f_ring.03.L')
    bone.head = 0.5748, -0.0027, 0.9518
    bone.tail = 0.5833, -0.0066, 0.9291
    bone.roll = -0.3228
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_ring.02.L']]
    bones['f_ring.03.L'] = bone.name
    bone = arm.edit_bones.new('f_pinky.03.L')
    bone.head = 0.5717, 0.0239, 0.9583
    bone.tail = 0.5792, 0.0222, 0.9405
    bone.roll = -0.6636
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_pinky.02.L']]
    bones['f_pinky.03.L'] = bone.name
    bone = arm.edit_bones.new('f_index.03.R')
    bone.head = -0.5585, -0.0461, 0.9554
    bone.tail = -0.5666, -0.0537, 0.9317
    bone.roll = -0.1551
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_index.02.R']]
    bones['f_index.03.R'] = bone.name
    bone = arm.edit_bones.new('thumb.03.R')
    bone.head = -0.4964, -0.0521, 0.9998
    bone.tail = -0.4970, -0.0689, 0.9784
    bone.roll = -0.3097
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['thumb.02.R']]
    bones['thumb.03.R'] = bone.name
    bone = arm.edit_bones.new('f_middle.03.R')
    bone.head = -0.5757, -0.0269, 0.9498
    bone.tail = -0.5869, -0.0337, 0.9254
    bone.roll = 0.1971
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_middle.02.R']]
    bones['f_middle.03.R'] = bone.name
    bone = arm.edit_bones.new('f_ring.03.R')
    bone.head = -0.5748, -0.0027, 0.9518
    bone.tail = -0.5833, -0.0066, 0.9291
    bone.roll = 0.3228
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_ring.02.R']]
    bones['f_ring.03.R'] = bone.name
    bone = arm.edit_bones.new('f_pinky.03.R')
    bone.head = -0.5717, 0.0239, 0.9583
    bone.tail = -0.5792, 0.0222, 0.9405
    bone.roll = 0.6636
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['f_pinky.02.R']]
    bones['f_pinky.03.R'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['spine']]
    pbone.rigify_type = 'spines.basic_spine'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.pivot_pos = 2
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Torso (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Torso (Tweak)')
    pbone = obj.pose.bones[bones['spine.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['thigh.L']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    try:
        pbone.rigify_parameters.limb_type = 'leg'
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.L (FK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.L (Tweak)')
    pbone = obj.pose.bones[bones['thigh.R']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    try:
        pbone.rigify_parameters.limb_type = 'leg'
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.R (FK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.R (Tweak)')
    pbone = obj.pose.bones[bones['spine.002']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['shin.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['shin.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['spine.003']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['foot.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['foot.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['spine.004']]
    pbone.rigify_type = 'spines.super_head'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.connect_chain = True
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Torso (Tweak)')
    pbone = obj.pose.bones[bones['shoulder.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['shoulder.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'YXZ'
    assign_bone_collections(pbone, 'Torso')
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['toe.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['heel.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.L (IK)')
    pbone = obj.pose.bones[bones['toe.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['heel.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Leg.R (IK)')
    pbone = obj.pose.bones[bones['spine.005']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Torso')
    pbone = obj.pose.bones[bones['upper_arm.L']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.L (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.L (FK)')
    pbone = obj.pose.bones[bones['upper_arm.R']]
    pbone.rigify_type = 'limbs.super_limb'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.R (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.R (FK)')
    pbone = obj.pose.bones[bones['forearm.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    pbone = obj.pose.bones[bones['forearm.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    pbone = obj.pose.bones[bones['hand.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.L (IK)')
    pbone = obj.pose.bones[bones['hand.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Arm.R (IK)')
    pbone = obj.pose.bones[bones['f_index.01.L']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['thumb.01.L']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_middle.01.L']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_ring.01.L']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_pinky.01.L']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_index.01.R']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['thumb.01.R']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_middle.01.R']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_ring.01.R']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_pinky.01.R']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Detail)')
    pbone = obj.pose.bones[bones['f_index.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['thumb.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_middle.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_ring.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_pinky.02.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_index.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['thumb.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_middle.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_ring.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_pinky.02.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_index.03.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['thumb.03.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_middle.03.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_ring.03.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_pinky.03.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_index.03.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['thumb.03.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_middle.03.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_ring.03.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')
    pbone = obj.pose.bones[bones['f_pinky.03.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fingers')

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        bone.bbone_x = bone.bbone_z = bone.length * 0.05
        arm.edit_bones.active = bone

    arm.collections.active_index = 0

    return bones


if __name__ == "__main__":
    create(bpy.context.active_object)
