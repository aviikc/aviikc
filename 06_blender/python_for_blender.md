
# Table of Contents

1.  [The BPY Module](#org612a887)
    1.  [bpy.ops](#orgdc71aad)
        1.  [Circle](#org52db228)
        2.  [Sphere (Ico-sphere)](#orgd1438b6)
    2.  [bpy.context](#org86659a6)
    3.  [bpy.types](#org637321a)
    4.  [bpy.data](#orgbcbc45f)



<a id="org612a887"></a>

# The BPY Module


<a id="orgdc71aad"></a>

## bpy.ops


<a id="org52db228"></a>

### Circle

-   bpy.ops.mesh.primitive<sub>circle</sub><sub>add</sub>()

[Circle Link](https://docs.blender.org/api/current/bpy.ops.mesh.html)
parameters

-   vertices
-   radius
-   location=(0.0, 0.0, 0.0)
-   rotation=(0.0, 0.0, 0.0)

    import bpy    #imports the bpy library in BLENDER
    
    
    bpy.ops.mesh.primitive_circle_add(radius=1,
                                      vertices = 20,
                                      location=(0,4,0))


<a id="orgd1438b6"></a>

### Sphere (Ico-sphere)

    import bpy    #imports the bpy library in BLENDER
    - bpy.ops.mesh.primitive_ico_sphere_add(subdivisions = 3,
                                            radius=4,
                                            location=(2,7,8))


<a id="org86659a6"></a>

## bpy.context


<a id="org637321a"></a>

## bpy.types

-   operator
-   panel


<a id="orgbcbc45f"></a>

## bpy.data

