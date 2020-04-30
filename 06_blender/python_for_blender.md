
# Table of Contents

1.  [The BPY Module](#orgcb901ac)
    1.  [bpy.ops](#org08cb75f)
        1.  [Circle](#org1467929)
        2.  [Sphere (Ico-sphere)](#org5c055c2)
        3.  [Cube](#org235a0a1)
        4.  [Selection (Alternative)](#org0e0416f)
        5.  [Selection](#org3afeab3)
    2.  [bpy.context](#org782f332)
    3.  [bpy.types](#org15d4a0e)
    4.  [bpy.data](#org007c342)



<a id="orgcb901ac"></a>

# The BPY Module


<a id="org08cb75f"></a>

## bpy.ops


<a id="org1467929"></a>

### Circle

    import bpy                                               #imports the bpy library in BLENDER
    
    bpy.ops.mesh.primitive_circle_add(radius=1,
                                      vertices = 20,
                                      location=(0,4,0))

[Circle Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)

1.  parameters

    -   vertices
    -   radius
    -   location=(0.0, 0.0, 0.0)
    -   rotation=(0.0, 0.0, 0.0)


<a id="org5c055c2"></a>

### Sphere (Ico-sphere)

    import bpy                                                #imports the bpy library in BLENDER
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3,
                                          radius=4,
                                          location=(2,7,8),
                                          rotation=(0,0,0))

1.  parameters

    -   subdivisions
    -   radius
    -   location=(0.0, 0.0, 0.0)
    -   rotation=(0.0, 0.0, 0.0)


<a id="org235a0a1"></a>

### Cube

    import bpy                                                #imports the bpy library in BLENDER
    bpy.ops.mesh.primitive_cube_add(size = 3,
                                    location=(2,7,8),
                                    rotation=(0,0,0))

1.  parameters

    -   size
    -   align
    -   location=(0.0, 0.0, 0.0)
    -   rotation=(0.0, 0.0, 0.0)


<a id="org0e0416f"></a>

### Selection (Alternative)

-   bpy.ops.object.select<sub>all</sub>()
    -   action = 'SELECT'
    -   action = 'DESELECT'


<a id="org3afeab3"></a>

### Selection

1.  bpy.ops.object.mode<sub>set</sub>(mode='EDIT')

    -   mode='EDIT'
    -   mode='OBJECT'

2.  bps.ops.mesh.select<sub>mode</sub>(type='FACE')

3.  bps.ops.mesh.select<sub>mode</sub>(type='VERT')


<a id="org782f332"></a>

## bpy.context

1.\`\`\`bpy.context.scene.objects\`\`\`

2.\`\`\`bpy.context.view<sub>layer.objects</sub>\`\`\`

3.\`\`\`bpy.context.selected<sub>objects</sub>\`\`\`

4.bpy.context.active<sub>object</sub>


<a id="org15d4a0e"></a>

## bpy.types

-   operator
-   panel


<a id="org007c342"></a>

## bpy.data

1.my<sub>object.data.vertices</sub>

2.my<sub>object.data.faces</sub>

