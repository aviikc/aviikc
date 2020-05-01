
# Table of Contents

1.  [Blender UI](#orgf7cf081)
    1.  [B](#orgb44a437)
    2.  [Panels](#org4a8f35a)
    3.  [Contexts](#org5d59ad6)
        1.  [Panel Locations](#org33f88b4)
        2.  [Panel Region](#orgf567fbf)


<a id="orgf7cf081"></a>

# Blender UI

Blender's interface is drawn entirely in OpenGL which allows you to customize your interface to suit your needs. Windows and other interface elements can be panned, zoomed and their content moved around.
<br/>
Blender user interface is based on 3 main principles.

-   **Non Overlapping:** The UI permits you to view all relevant options and tools at a glance without pushing or dragging windows around.
-   **Non Blocking:**  Tools and interface options do not block the user from any other parts of Blender. Blender doesn't pop up requesters that require the user to fill in data before things execute.
-   **Non Modal:** User input should remain as consistent and predictable as possible without changing commonly used methods (mouse, keyboard) on the fly. \*\* Menus


<a id="orgb44a437"></a>

## B


<a id="org4a8f35a"></a>

## Panels


<a id="org5d59ad6"></a>

## Contexts

Designing an UI or Add-on is basically a combination of supplying Properties and the inheritance of built-in Type classes (Panel, Operator, Menu etc.).


<a id="org33f88b4"></a>

### Panel Locations

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Location</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Empty</td>
<td class="org-left">Empty</td>
</tr>


<tr>
<td class="org-left">VIEW\_3D</td>
<td class="org-left">3D Viewport, Manipulate objects in a 3D environment.</td>
</tr>


<tr>
<td class="org-left">IMAGE\_EDITOR</td>
<td class="org-left">UV/Image Editor, View and edit images and UV Maps.</td>
</tr>


<tr>
<td class="org-left">NODE\_EDITOR</td>
<td class="org-left">Node Editor, Editor for node-based shading and compositing tools.</td>
</tr>


<tr>
<td class="org-left">SEQUENCE\_EDITOR</td>
<td class="org-left">Video Sequencer, Video editing tools.</td>
</tr>


<tr>
<td class="org-left">CLIP\_EDITOR</td>
<td class="org-left">Movie Clip Editor, Motion tracking tools.</td>
</tr>


<tr>
<td class="org-left">DOPESHEET\_EDITOR</td>
<td class="org-left">Dope Sheet, Adjust timing of keyframes.</td>
</tr>


<tr>
<td class="org-left">GRAPH\_EDITOR</td>
<td class="org-left">Graph Editor, Edit drivers and keyframe interpolation.</td>
</tr>


<tr>
<td class="org-left">NLA\_EDITOR</td>
<td class="org-left">Nonlinear Animation, Combine and layer Actions.</td>
</tr>


<tr>
<td class="org-left">TEXT\_EDITOR</td>
<td class="org-left">Text Editor, Edit scripts and in-file documentation.</td>
</tr>


<tr>
<td class="org-left">CONSOLE</td>
<td class="org-left">Python Console, Interactive programmatic console for advanced editing and script development.</td>
</tr>


<tr>
<td class="org-left">INFO</td>
<td class="org-left">Info, Log of operations, warnings and error messages.</td>
</tr>


<tr>
<td class="org-left">TOPBAR</td>
<td class="org-left">Top Bar, Global bar at the top of the screen for global per-window settings.</td>
</tr>


<tr>
<td class="org-left">STATUSBAR</td>
<td class="org-left">Status Bar, Global bar at the bottom of the screen for general status information.</td>
</tr>


<tr>
<td class="org-left">OUTLINER</td>
<td class="org-left">Outliner, Overview of scene graph and all available data-blocks.</td>
</tr>


<tr>
<td class="org-left">PROPERTIES</td>
<td class="org-left">Properties, Edit properties of active object and related data-blocks.</td>
</tr>


<tr>
<td class="org-left">FILE\_BROWSER</td>
<td class="org-left">File Browser, Browse for files and assets.</td>
</tr>


<tr>
<td class="org-left">PREFERENCES</td>
<td class="org-left">Preferences, Edit persistent configuration settings.</td>
</tr>
</tbody>
</table>


<a id="orgf567fbf"></a>

### Panel Region

WINDOW’, ‘HEADER’, ‘CHANNELS’, ‘TEMPORARY’, ‘UI’, ‘TOOLS’, ‘TOOL\_PROPS’, ‘PREVIEW’, ‘HUD’, ‘NAVIGATION\_BAR’, ‘EXECUTE’, ‘FOOTER’, ‘TOOL\_HEADER

bpy.types.Panel
bpy.types.Menu
bpy.types.Operator
bpy.types.PropertyGroup
bpy.types.KeyingSet
bpy.types.RenderEngine

    import bpy
    class SimpleOperator(bpy.types.Operator):
        bl_idname = "object.simple_operator"
        bl_label = "Tool Name"
    
        def execute(self, context):
            print("Hello World")
            return {'FINISHED'}
    
    bpy.utils.register_class(SimpleOperator)

    import bpy
    
    class SimpleOperator(bpy.types.Operator):
        """ See example above """
    
    def register():
        bpy.utils.register_class(SimpleOperator)
    
    def unregister():
        bpy.utils.unregister_class(SimpleOperator)
    
    if __name__ == "__main__":
        register()

For more convenient loading/unloading bpy.utils.register\_module (module) and bpy.utils.unregister\_module (module) functions exist.

