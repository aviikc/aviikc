
# Table of Contents

1.  [The BPY Module](#org6bfd69a)
    1.  [Section 1 - The Basic Modules](#org165fb3d)
        1.  [bpy.ops Doc Link](#orgf057924)
        2.  [bpy.context](#org0eafa75)
        3.  [bpy.types](#org9fec98c)
        4.  [bpy.data](#orgbe7ff01)
    2.  [BLENDER object, active\_object and selected\_objects](#orgca6cdd8)
    3.  [Selecting Objects (meshes) in BLENDER.](#orgb0950a5)
        1.  [Using a getter to check whether an object is selected](#org6dded43)
    4.  [Accessing Attributes](#org2a93b19)



<a id="org6bfd69a"></a>

# The BPY Module

Blender sets up its python environment when it is started and stays active till blender process is killed. Blender provides the bpy module to the Python interpreter. This module can be imported in a script and gives access to Blender data, classes, and functions.

    # To use bpy module 
    import bpy

Unfortunately the ‘bpy’ module cannot be used outside of Blender.

-   Check-out pip install fake-bpy-module-<version> where version could be the blender version you are using. More info at <https://github.com/nutti/fake-bpy-module>
-   Add Blender Intellisense for scripting within blender environment.


<a id="org165fb3d"></a>

## Section 1 - The Basic Modules


<a id="orgf057924"></a>

### bpy.ops [Doc Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)

1.  Circle

        import bpy                                               #imports the bpy library in BLENDER
        
        bpy.ops.mesh.primitive_circle_add(radius=1,
                                          vertices = 20,
                                          location=(0,4,0))
    
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


<a id="org0eafa75"></a>

### bpy.context

1.bpy.context.scene.objects
Returns a collection of scene objects.

    print([i for i in bpy.context.scene.objects])
    # or the statement can also be written as, 
    print(list(bpy.context.scene.objects))
    
    # Please note that printint type of bpy.context.scene.objects yeild "bpy_prop_collection"
    print(type(bpy.context.scene.objects))
    # Results in: <class 'bpy_prop_collection'>

2.bpy.context.selected\_objects

3.bpy.context.active\_object


<a id="org9fec98c"></a>

### bpy.types

-   operator
-   panel


<a id="orgbe7ff01"></a>

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


<a id="orgca6cdd8"></a>

## BLENDER object, active\_object and selected\_objects

In blender all objects are outlined in orange. The object which is outlined in yellow is the last selected object or the active object. An active object tends to remain an active object till another object is selected.


<a id="orgb0950a5"></a>

## Selecting Objects (meshes) in BLENDER.


<a id="org6dded43"></a>

### Using a getter to check whether an object is selected

-   bpy.context.active\_object.select\_get()


<a id="org2a93b19"></a>

## Accessing Attributes

