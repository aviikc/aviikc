
# Table of Contents

1.  [The BPY Module](#org66d0bd6)
    1.  [bpy.ops](#orgf5afa58)
        1.  [Circle](#orgb6e13dc)
        2.  [Sphere (Ico-sphere)](#orgb062ac7)
        3.  [Cube](#org2b44ae5)
        4.  [Selection (Alternative)](#orgc7bc90c)
        5.  [Selection](#orgc837a6f)
    2.  [bpy.context](#org1680047)
    3.  [bpy.types](#org8fd363e)
    4.  [bpy.data](#org8eb94a1)



<a id="org66d0bd6"></a>

# The BPY Module


<a id="orgf5afa58"></a>

## bpy.ops


<a id="orgb6e13dc"></a>

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


<a id="orgb062ac7"></a>

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


<a id="org2b44ae5"></a>

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


<a id="orgc7bc90c"></a>

### Selection (Alternative)

-   bpy.ops.object.select\_all()
    -   action = 'SELECT'
    -   action = 'DESELECT'


<a id="orgc837a6f"></a>

### Selection

1.  bpy.ops.object.mode\_set(mode='EDIT')

    -   mode='EDIT'
    -   mode='OBJECT'

2.  bps.ops.mesh.select\_mode(type='FACE')

3.  bps.ops.mesh.select\_mode(type='VERT')


<a id="org1680047"></a>

## bpy.context

1.bpy.context.scene.objects

2.bpy.context.view\_layer.objects

3.bpy.context.selected\_objects

4.bpy.context.active\_object


<a id="org8fd363e"></a>

## bpy.types

-   operator
-   panel


<a id="org8eb94a1"></a>

## bpy.data

1.my\_object.data.vertices

2.my\_object.data.faces

