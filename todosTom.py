def objectselect(objectName):
    bpy.context.scene.objects.active = bpy.data.objects[objectName]
    return f'Active Object: {bpy.context.object.name}'

print(objectselect('Cube'))




def myselector




