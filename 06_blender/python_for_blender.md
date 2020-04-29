
# Table of Contents

1.  [The BPY Module](#org8c18038)
    1.  [bpy.ops](#org5f48d04)
        1.  [Circle](#orge165520)
        2.  [Sphere (Ico-sphere)](#org666a089)
    2.  [bpy.context](#org3e022f1)
    3.  [bpy.types](#org20bb139)
    4.  [bpy.data](#org58bccad)



<a id="org8c18038"></a>

# The BPY Module


<a id="org5f48d04"></a>

## bpy.ops


<a id="orge165520"></a>

### Circle

    import bpy                                               #imports the bpy library in BLENDER
    
    bpy.ops.mesh.primitive_circle_add(radius=1,
                                      vertices = 20,
                                      location=(0,4,0))

[Circle Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)
parameters

-   vertices
-   radius
-   location=(0.0, 0.0, 0.0)
-   rotation=(0.0, 0.0, 0.0)


<a id="org666a089"></a>

### Sphere (Ico-sphere)

    import bpy                                                #imports the bpy library in BLENDER
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3,
                                          radius=4,
                                          location=(2,7,8)
                                          rotation=(0,0,0))


<a id="org3e022f1"></a>

## bpy.context


<a id="org20bb139"></a>

## bpy.types

-   operator
-   panel


<a id="org58bccad"></a>

## bpy.data

