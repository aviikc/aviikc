
# Table of Contents

1.  [The BPY Module](#org7302976)
    1.  [Section 1 - The Basic Modules](#org5f5cb78)
        1.  [bpy.ops](#org58e03aa)
        2.  [bpy.context](#orgc797c9d)
        3.  [bpy.types](#org2af640f)
        4.  [bpy.data](#org2080538)
    2.  [BLENDER object, active\_object and selected\_objects](#org5a52491)
    3.  [Selecting Objects (meshes) in BLENDER.](#orge7ca95c)
        1.  [Using a getter to check whether an object is selected](#org702c8b9)
    4.  [Accessing Attributes](#org02b7d36)



<a id="org7302976"></a>

# The BPY Module


<a id="org5f5cb78"></a>

## Section 1 - The Basic Modules


<a id="org58e03aa"></a>

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


<a id="orgc797c9d"></a>

### bpy.context

1.bpy.context.scene.objects

2.bpy.context.view\_layer.objects

3.bpy.context.selected\_objects

4.bpy.context.active\_object


<a id="org2af640f"></a>

### bpy.types

-   operator
-   panel


<a id="org2080538"></a>

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


<a id="org5a52491"></a>

## BLENDER object, active\_object and selected\_objects

In blender all objects are outlined in orange. The object which is outlined in yellow is the last selected object or the active object. An active object tends to remain an active object till another object is selected.


<a id="orge7ca95c"></a>

## Selecting Objects (meshes) in BLENDER.


<a id="org702c8b9"></a>

### Using a getter to check whether an object is selected

-   bpy.context.active\_object.select\_get()


<a id="org02b7d36"></a>

## Accessing Attributes
