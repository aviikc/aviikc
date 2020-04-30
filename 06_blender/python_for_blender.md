
# Table of Contents

1.  [The BPY Module](#orgbf3722e)
    1.  [01. The Basic Modules](#org1bbd92c)
        1.  [bpy.ops Link](#org120980d)
        2.  [bpy.context Link](#org8597418)
        3.  [bpy.type Linkk](#orgf7f88b7)
        4.  [bpy.data Link](#org811e2e4)
    2.  [02. BLENDER object, active\_object and selected\_objects](#org397d385)
    3.  [03. Selecting Objects (meshes) in BLENDER.](#org40a1a4c)
        1.  [Using a getter to check whether an object is selected](#orgdb05da8)
    4.  [04. Accessing Attributes](#org90cd30c)



<a id="orgbf3722e"></a>

# The BPY Module

Blender sets up its python environment when it is started and stays active till blender process is killed. Blender provides the bpy module to the Python interpreter. This module can be imported in a script and gives access to Blender data, classes, and functions.

    # To use bpy module 
    import bpy

Unfortunately the ‘bpy’ module cannot be used outside of Blender.

-   Check-out pip install fake-bpy-module-<version> where version could be the blender version you are using. More info at <https://github.com/nutti/fake-bpy-module>
-   Add Blender Intellisense for scripting within blender environment.


<a id="org1bbd92c"></a>

## 01. The Basic Modules


<a id="org120980d"></a>

### bpy.ops [Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)

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

4.  Selection

    1.  bpy.ops.object.select\_all()
    
        -   action = 'SELECT'
        -   action = 'DESELECT'
    
    2.  bpy.ops.object.mode\_set(mode='EDIT')
    
        -   mode='EDIT'
        -   mode='OBJECT'
    
    3.  bps.ops.mesh.select\_mode(type='FACE')
    
    4.  bps.ops.mesh.select\_mode(type='VERT')


<a id="org8597418"></a>

### bpy.context [Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)

1.bpy.context.scene.objects
Returns a collection of scene objects.

    print([i for i in bpy.context.scene.objects])
    # or the statement can also be written as, 
    print(list(bpy.context.scene.objects))
    
    # Please note that printint type of bpy.context.scene.objects yeild "bpy_prop_collection"
    print(type(bpy.context.scene.objects))
    # Results in: <class 'bpy_prop_collection'>

2.bpy.context.selected\_objects

    # After selecting an object on the 3D View 
    print([i for i in bpy.context.selected_objects])
    # With some exception handling incase nothing is selected.
    if bpy.context.selected_objects != []:
        print(list(bpy.context.selected_objects))

3.bpy.context.active\_object


<a id="orgf7f88b7"></a>

### bpy.type [Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)k

-   operator
-   panel


<a id="org811e2e4"></a>

### bpy.data [Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)

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


<a id="org397d385"></a>

## 02. BLENDER object, active\_object and selected\_objects

In blender all objects are outlined in orange. The object which is outlined in yellow is the last selected object or the active object. An active object tends to remain an active object till another object is selected.
Objects in Blender could be of the following types:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Object</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Mesh</td>
<td class="org-left">Meshes are objects composed of Polygonal Faces, Edges and/or Vertices, and can be edited extensively with Blender’s mesh editing tools.</td>
</tr>


<tr>
<td class="org-left">Curve</td>
<td class="org-left">Curves are mathematically defined objects which can be manipulated with control handles or control points (instead of vertices), to manage their length and curvature.</td>
</tr>


<tr>
<td class="org-left">Surface</td>
<td class="org-left">Surfaces are patches of geometry.</td>
</tr>


<tr>
<td class="org-left">Metaball</td>
<td class="org-left">Metaballs have volume. They also have an attribute to attract other metaballs in joining togather forming a larger topology.</td>
</tr>


<tr>
<td class="org-left">Text</td>
<td class="org-left">Text Objects create a two-dimensional representation of a string of characters.</td>
</tr>


<tr>
<td class="org-left">Grease Pencil</td>
<td class="org-left">Grease Pencil Objects are objects created by painting strokes.</td>
</tr>


<tr>
<td class="org-left">Armature</td>
<td class="org-left">Armatures are used for rigging 3D models in order to make them poseable and animateable.</td>
</tr>


<tr>
<td class="org-left">Lattice</td>
<td class="org-left">Lattices are non-renderable wireframes, commonly used for taking additional control over other objects with help of the Lattice Modifier.</td>
</tr>


<tr>
<td class="org-left">Empty</td>
<td class="org-left">Empties are null objects that are simple visual transform nodes that do not render. They are useful for controlling the position or movement of other objects.</td>
</tr>


<tr>
<td class="org-left">Image</td>
<td class="org-left">Images are empty objects that display images in the 3D Viewport. These images can be used to support modeling and animating.</td>
</tr>


<tr>
<td class="org-left">Light</td>
<td class="org-left">Lights for lighting the scene in renders.</td>
</tr>


<tr>
<td class="org-left">Light Probe</td>
<td class="org-left">Lights are used by the Eevee render engine and record lighting information for indirect lighting.</td>
</tr>


<tr>
<td class="org-left">Camera</td>
<td class="org-left">This is the virtual camera that is used to determine what appears in the render. See Cameras in Cycles.</td>
</tr>


<tr>
<td class="org-left">Speaker</td>
<td class="org-left">Speaker brings a source of sound to the scene.</td>
</tr>


<tr>
<td class="org-left">Force Field</td>
<td class="org-left">Force Fields are used in physical simulations. They give simulations external forces.</td>
</tr>


<tr>
<td class="org-left">Collection Instance</td>
<td class="org-left">Instances of existing collections.</td>
</tr>
</tbody>
</table>


<a id="org40a1a4c"></a>

## 03. Selecting Objects (meshes) in BLENDER.


<a id="orgdb05da8"></a>

### Using a getter to check whether an object is selected

-   bpy.context.active\_object.select\_get()


<a id="org90cd30c"></a>

## 04. Accessing Attributes

