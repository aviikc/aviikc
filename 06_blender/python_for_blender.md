
# Table of Contents

1.  [The BPY Module](#org81b116e)
    1.  [bpy.ops](#org2d2a594)
        1.  [Circle](#orgb5d89ae)
        2.  [Sphere (Ico-sphere)](#org1a5193a)
    2.  [bpy.context](#org2b3bbb4)
    3.  [bpy.types](#orgc886d04)
    4.  [bpy.data](#org7c390cf)



<a id="org81b116e"></a>

# The BPY Module


<a id="org2d2a594"></a>

## bpy.ops


<a id="orgb5d89ae"></a>

### Circle

-   bpy.ops.mesh.primitive<sub>circle</sub><sub>add</sub>()

[Circle Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)
parameters

-   vertices
-   radius
-   location=(0.0, 0.0, 0.0)
-   rotation=(0.0, 0.0, 0.0)

    import bpy                                               #imports the bpy library in BLENDER
    
    bpy.ops.mesh.primitive_circle_add(radius=1,
                                      vertices = 20,
                                      location=(0,4,0))


<a id="org1a5193a"></a>

### Sphere (Ico-sphere)

    import bpy                                                #imports the bpy library in BLENDER
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3,
                                          radius=4,
                                          location=(2,7,8)
                                          rotation=(0,0,0))


<a id="org2b3bbb4"></a>

## bpy.context


<a id="orgc886d04"></a>

## bpy.types

-   operator
-   panel


<a id="org7c390cf"></a>

## bpy.data

