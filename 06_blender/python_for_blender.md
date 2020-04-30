
# Table of Contents

1.  [The BPY Module](#orga2f6f89)
    1.  [Section 1 - The Basic Modules](#org2a193c7)
        1.  [bpy.ops](#org19ee16c)
        2.  [bpy.context](#orgb27f0de)
        3.  [bpy.types](#orgb1e94c7)
        4.  [bpy.data](#orgb832461)
    2.  [BLENDER object, active\_object and selected\_objects](#orge13fa60)
    3.  [Selecting Objects (meshes) in BLENDER.](#org09fe8f1)
        1.  [Using a getter to check whether an object is selected](#org3d3f9f9)
    4.  [Accessing Attributes](#org8a08e5d)



<a id="orga2f6f89"></a>

# The BPY Module

Blender sets up its python environment when it is started and stays active till blender process is killed. Blender provides the bpy module to the Python interpreter. This module can be imported in a script and gives access to Blender data, classes, and functions.

    # To use bpy module 
    import bpy


<a id="org2a193c7"></a>

## Section 1 - The Basic Modules


<a id="org19ee16c"></a>

### bpy.ops

1.  Circle

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

2.  Sphere (Ico-sphere)

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

3.  Cube

        import bpy                                                #imports the bpy library in BLENDER
        bpy.ops.mesh.primitive_cube_add(size = 3,
                                        location=(2,7,8),
                                        rotation=(0,0,0))
    
    1.  parameters
    
        -   size
        -   align
        -   location=(0.0, 0.0, 0.0)
        -   rotation=(0.0, 0.0, 0.0)

4.  Selection (Alternative)

5.  Selection

    1.  bpy.ops.object.select\_all()
    
        -   action = 'SELECT'
        -   action = 'DESELECT'
    
    2.  bpy.ops.object.mode\_set(mode='EDIT')
    
        -   mode='EDIT'
        -   mode='OBJECT'
    
    3.  bps.ops.mesh.select\_mode(type='FACE')
    
    4.  bps.ops.mesh.select\_mode(type='VERT')


<a id="orgb27f0de"></a>

### bpy.context

1.bpy.context.scene.objects

2.bpy.context.view\_layer.objects

3.bpy.context.selected\_objects

4.bpy.context.active\_object


<a id="orgb1e94c7"></a>

### bpy.types

-   operator
-   panel


<a id="orgb832461"></a>

### bpy.data

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


<a id="orge13fa60"></a>

## BLENDER object, active\_object and selected\_objects

In blender all objects are outlined in orange. The object which is outlined in yellow is the last selected object or the active object. An active object tends to remain an active object till another object is selected.


<a id="org09fe8f1"></a>

## Selecting Objects (meshes) in BLENDER.


<a id="org3d3f9f9"></a>

### Using a getter to check whether an object is selected

-   bpy.context.active\_object.select\_get()


<a id="org8a08e5d"></a>

## Accessing Attributes

