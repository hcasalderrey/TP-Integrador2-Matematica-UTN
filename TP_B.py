def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def contar_pares_impares(anios):
    pares = 0
    impares = 0
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def todos_despues_2000(anios):
    return all(anio > 2000 for anio in anios)

def alguno_bisiesto(anios):
    return any(es_bisiesto(anio) for anio in anios)

def producto_cartesiano(anios, edades):
    return [(anio, edad) for anio in anios for edad in edades]

def principal():
    anios = list(map(int, input("Ingrese los años de nacimiento separados por espacios: ").split()))

    pares, impares = contar_pares_impares(anios)
    print(f"Cantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")

    if todos_despues_2000(anios):
        print("Grupo Z")

    if alguno_bisiesto(anios):
        print("Tenemos un año especial")

    anio_actual = 2025
    edades = [anio_actual - anio for anio in anios]

    print("Producto cartesiano entre años y edades:")
    for par in producto_cartesiano(anios, edades):
        print(par)

if __name__ == "__main__":
    principal()
