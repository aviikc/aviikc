
# Table of Contents

1.  [The BPY Module](#orgc869faa)
    1.  [bpy.ops](#org2d5c426)
        1.  [Circle](#orge56a73a)
        2.  [Sphere (Ico-sphere)](#orgb02f71b)
        3.  [Cube](#orgc983e1f)
        4.  [Selection (Alternative)](#org139e7d2)
        5.  [Selection](#org7dd9613)
    2.  [bpy.context](#org9931236)
    3.  [bpy.types](#org843039f)
    4.  [bpy.data](#orgafec8a5)



<a id="orgc869faa"></a>

# The BPY Module


<a id="org2d5c426"></a>

## bpy.ops


<a id="orge56a73a"></a>

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


<a id="orgb02f71b"></a>

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


<a id="orgc983e1f"></a>

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


<a id="org139e7d2"></a>

### Selection (Alternative)

-   bpy.ops.object.select<sub>all</sub>()
    -   action = 'SELECT'
    -   action = 'DESELECT'


<a id="org7dd9613"></a>

### Selection

1.  bpy.ops.object.mode<sub>set</sub>(mode='EDIT')

    -   mode='EDIT'
    -   mode='OBJECT'

2.  bps.ops.mesh.select<sub>mode</sub>(type='FACE')

3.  bps.ops.mesh.select<sub>mode</sub>(type='VERT')


<a id="org9931236"></a>

## bpy.context

1.bpy.context.scene.objects

2.bpy.context.view<sub>layer.objects</sub>

3.bpy.context.selected<sub>objects</sub>

4.bpy.context.active<sub>object</sub>


<a id="org843039f"></a>

## bpy.types

-   operator
-   panel


<a id="orgafec8a5"></a>

## bpy.data

1.my<sub>object.data.vertices</sub>

2.my<sub>object.data.faces</sub>

