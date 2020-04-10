def obtener_tuple(nombre = "el elemento actual"):

    coord_string = input("Ingrese un conjunto de coordenadas para " + nombre + ": ")

    coord_tuple = tuple(int(elem) for elem in coord_string.split(','))

    return coord_tuple

imagenes = ['im1','im2','im3']

coord_img = {}

for key in imagenes:

    agregar_coord_tuple = obtener_tuple(str(key))

    while agregar_coord_tuple in coord_img.values():

        print("Esas coordenadas ya fueron ingresadas")

        agregar_coord_tuple = obtener_tuple(str(key))

    coord_img[key] = agregar_coord_tuple

print(coord_img)
