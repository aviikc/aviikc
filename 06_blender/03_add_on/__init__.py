# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "first tool",
    "author" : "aviikc",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}
from bpy.types import Operator
from bpy.utils import register_class, unregister_class

class Mover_OT_operator(Operator):
    """This is a move by a unit tool."""
    bl_idname  = "mover.operator"
    bl_label   = "Simple Create Cube"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        self.report({'INFO'}, "Hello World!")
        return {'FINISHED'}

def register():
    register_class(Mover_OT_operator)

def unregister():
    unregister_class(Mover_OT_operator)

if __name__ == "__main__":
    register()