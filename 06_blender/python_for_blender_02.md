

# Blender UI

Blender's interface is drawn entirely in OpenGL which allows you to customize your interface to suit your needs. Windows and other interface elements can be panned, zoomed and their content moved around.
info at <http://www.letworyinteractive.com/blendercode/d5/d2e/GHOSTPage.html>
<br/>
<br/>
Blender user interface is based on 3 main principles.

-   **Non Overlapping:** The UI permits you to view all relevant options and tools at a glance without pushing or dragging windows around.
-   **Non Blocking:**  Tools and interface options do not block the user from any other parts of Blender. Blender doesn't pop up requesters that require the user to fill in data before things execute.
-   **Non Modal:** User input should remain as consistent and predictable as possible without changing commonly used methods (mouse, keyboard) on the fly.


## Regions

Every Editor in Blender is divided into Regions. Regions can have smaller structuring elements like tabs and panels with buttons, controls and widgets placed within them.

-   **Main Region -** At least one region is always visible. It is called the Main region and is the most prominent part of the editor.
-   **Header -** A header is a small horizontal strip, which sits either at the top or bottom of an area. 
    -   **Context Menu -** The context menu is available with right click on a header.
-   **Toolbar -** The Toolbar (on the left side of the editor area) contains a set of interactive tools.
-   **Tool Settings -** The Tool Settings (at the top/bottom of the editor area) contains as its name suggests the settings of the active tool. It’s visibility can be toggled with the header’s context menu.
-   **Adjust Last Operation -** The Adjust Last Operation is a region that shows tool options when tools (operators) are run.
-   **Sidebar -** The Sidebar (on the right side of the editor area) contains Panels with settings of objects within the editor and the editor itself.
-   **Footer -** Some editors show a bar (on top/bottom of the editor area) that displays information about for example the active tool.


## Menu

A menu in blender is a list of options in text form. There are a variety of different menus available for accessing options and tools.
Menus reside in blender under different.


## Tabs

Tabs are used to control overlapping sections in the user interface. Contents of only one Tab is visible at a time. Tabs are listed in Tab header, which can be vertical or horizontal.


## Panels

The smallest organizational unit in the user interface is a panel. Panel header is always visible, and it shows the title for the panel. A panel can either be expanded to show its contents, or collapsed to hide its contents.


## Contexts

Designing an UI or Add-on is basically a combination of supplying Properties and the inheritance of built-in Type classes (Panel, Operator, Menu etc.).


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
<td class="org-left">VIEW=\_=3D</td>
<td class="org-left">3D Viewport, Manipulate objects in a 3D environment.</td>
</tr>


<tr>
<td class="org-left">IMAGE=\_=EDITOR</td>
<td class="org-left">UV/Image Editor, View and edit images and UV Maps.</td>
</tr>


<tr>
<td class="org-left">NODE~\_~EDITOR</td>
<td class="org-left">Node Editor, Editor for node-based shading and compositing tools.</td>
</tr>


<tr>
<td class="org-left">SEQUENCE~\_~EDITOR</td>
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

