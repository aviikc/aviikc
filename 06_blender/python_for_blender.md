
# Table of Contents

1.  [The BPY Module](#org5af7954)
    1.  [bpy.ops](#orgef250e7)
        1.  [Circle](#orge2069f1)
        2.  [Sphere (Ico-sphere)](#orgdb3d390)
        3.  [Cube](#org90399a5)
        4.  [Selection (Alternative)](#org86664ef)
        5.  [Selection](#orge415496)
    2.  [bpy.context](#orgf660c65)
    3.  [bpy.types](#org81ee63d)
    4.  [bpy.data](#orged8fe39)
2.  [BLENDER object, active\_object and selected\_objects](#org16c5942)
3.  [Selecting Objects (meshes) in BLENDER.](#org1ba11fc)
        1.  [Using a getter to check whether an object is selected](#orgf35946e)
4.  [Accessing Attributes](#org731f033)



<a id="org5af7954"></a>

# The BPY Module


<a id="orgef250e7"></a>

## bpy.ops


<a id="orge2069f1"></a>

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


<a id="orgdb3d390"></a>

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


<a id="org90399a5"></a>

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


<a id="org86664ef"></a>

### Selection (Alternative)

-   bpy.ops.object.select\_all()
    -   action = 'SELECT'
    -   action = 'DESELECT'


<a id="orge415496"></a>

### Selection

1.  bpy.ops.object.mode\_set(mode='EDIT')

    -   mode='EDIT'
    -   mode='OBJECT'

2.  bps.ops.mesh.select\_mode(type='FACE')

3.  bps.ops.mesh.select\_mode(type='VERT')


<a id="orgf660c65"></a>

## bpy.context

1.bpy.context.scene.objects

2.bpy.context.view\_layer.objects

3.bpy.context.selected\_objects

4.bpy.context.active\_object


<a id="org81ee63d"></a>

## bpy.types

-   operator
-   panel


<a id="orged8fe39"></a>

## bpy.data

1.  Exploring the Blend Scene

-   List all objects in the scene.

    print(list(bpy.data.objects))
    
    #Result: [bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Light']]

-Please note bpy.data.objects['Object\_Name'] can be used to check Attributes.   

2.my\_object.data.vertices

3.my\_object.data.faces

4.Another Method to select objects(By Name)

    
    import bpy
    
    
    bpy.ops.mesh.primitive_circle_add(radius=6, vertices=12)
    
    my_circ = bpy.context.object
    cir_verts = len(my_circ.data.vertices)
    
    for i in range(cir_verts):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3, radius=1.2, location = my_circ.data.vertices[i].co)


<a id="org16c5942"></a>

# BLENDER object, active\_object and selected\_objects

In blender all objects are outlined in orange. The object which is outlined in yellow is the last selected object or the active object. An active object tends to remain an active object till another object is selected.


<a id="org1ba11fc"></a>

# Selecting Objects (meshes) in BLENDER.


<a id="orgf35946e"></a>

### Using a getter to check whether an object is selected

-   bpy.context.active\_object.select\_get()


<a id="org731f033"></a>

# Accessing Attributes

