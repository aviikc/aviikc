
# Table of Contents

1.  [The BPY Module](#orgdf27e02)
    1.  [bpy.ops](#orga70f450)
        1.  [Circle](#orge6316c7)
        2.  [Sphere (Ico-sphere)](#orge677d99)
        3.  [Cube](#org03ce1e2)
        4.  [Selection (Alternative)](#orged0a6c7)
        5.  [Selection](#org08c293d)
    2.  [bpy.context](#org4d02e39)
    3.  [bpy.types](#org02e694c)
    4.  [bpy.data](#orge655ce1)



<a id="orgdf27e02"></a>

# The BPY Module


<a id="orga70f450"></a>

## bpy.ops


<a id="orge6316c7"></a>

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


<a id="orge677d99"></a>

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


<a id="org03ce1e2"></a>

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


<a id="orged0a6c7"></a>

### Selection (Alternative)

-   bpy.ops.object.select\_all()
    -   action = 'SELECT'
    -   action = 'DESELECT'


<a id="org08c293d"></a>

### Selection

1.  bpy.ops.object.mode\_set(mode='EDIT')

    -   mode='EDIT'
    -   mode='OBJECT'

2.  bps.ops.mesh.select\_mode(type='FACE')

3.  bps.ops.mesh.select\_mode(type='VERT')


<a id="org4d02e39"></a>

## bpy.context

1.bpy.context.scene.objects

2.bpy.context.view\_layer.objects

3.bpy.context.selected\_objects

4.bpy.context.active\_object


<a id="org02e694c"></a>

## bpy.types

-   operator
-   panel


<a id="orge655ce1"></a>

## bpy.data

1.my\_object.data.vertices

2.my\_object.data.faces

    
    import bpy
    
    
    bpy.ops.mesh.primitive_circle_add(radius=6, vertices=12)
    
    my_circ = bpy.context.object
    cir_verts = len(my_circ.data.vertices)
    
    for i in range(cir_verts):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3, radius=1.2, location = my_circ.data.vertices[i].co)

