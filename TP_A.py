def convert_to_set(numero):
    return set(str(numero))

def union(conjuntoA, conjuntoB):
    return conjuntoA.union(conjuntoB)

def interseccion(conjuntoA, conjuntoB):
    return conjuntoA.intersection(conjuntoB)

def diferencia(conjuntoA, conjuntoB):
    return conjuntoA.difference(conjuntoB)

def frecuencia_cada_digito(numero):
    frecuencia = {}
    for digito in str(numero):
        frecuencia[digito] = frecuencia.get(digito, 0) + 1
    return frecuencia

def suma_de_digitos(numero):
    return sum(int(digito) for digito in str(numero))

def evaluar_expresion(conjuntoA, conjuntoB):
    resultado = {}
    resultado['Diversidad numérica'] = len(conjuntoA) >= 5 and len(conjuntoB) >= 5
    resultado['Combinación amplia'] = len(conjuntoA) > len(conjuntoB) and any(int(d) % 2 != 0 for d in conjuntoB)
    resultado['Grupo sin ceros'] = '0' not in conjuntoA and '0' not in conjuntoB
    resultado['Dígito común'] = len(interseccion(conjuntoA, conjuntoB)) > 0
    resultado['Grupo par'] = (len(conjuntoA) % 2 == 0) and (len(conjuntoB) % 2 == 0)
    resultado['Dígito representativo'] = len(interseccion(conjuntoA, conjuntoB)) == 1
    resultado['Dígito compartido'] = "Dígito compartido" if len(interseccion(conjuntoA, conjuntoB)) > 0 else "No hay dígito compartido"
    resultado['Diversidad numérica alta'] = "Diversidad numérica alta" if len(conjuntoA) > 6 or len(conjuntoB) > 6 else "Diversidad numérica baja"
    return resultado

def expresion_lenguaje_natural(conjuntoA, conjuntoB):
    expresion = {}
    expresion['Los dígitos que están en A y no están en B'] = diferencia(conjuntoA, conjuntoB)
    expresion['Los dígitos que están en B y no están en A'] = diferencia(conjuntoB, conjuntoA)
    expresion['Los dígitos que están en ambos conjuntos'] = interseccion(conjuntoA, conjuntoB)
    expresion['Los dígitos que están en al menos uno de los conjuntos'] = union(conjuntoA, conjuntoB)
    expresion['Los dígitos que no se repiten entre A y B'] = union(diferencia(conjuntoA, conjuntoB), diferencia(conjuntoB, conjuntoA))
    return expresion

def main():
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    conjuntoA = convert_to_set(num1)
    conjuntoB = convert_to_set(num2)

    print(f"\nConjunto A: {conjuntoA}")
    print(f"Conjunto B: {conjuntoB}")
    print(f"Unión: {union(conjuntoA, conjuntoB)}")
    print(f"Intersección: {interseccion(conjuntoA, conjuntoB)}")
    print(f"Diferencia A - B: {diferencia(conjuntoA, conjuntoB)}")
    print(f"Diferencia B - A: {diferencia(conjuntoB, conjuntoA)}")

    print(f"\nFrecuencia de dígitos en el primer número: {frecuencia_cada_digito(num1)}")
    print(f"Frecuencia de dígitos en el segundo número: {frecuencia_cada_digito(num2)}")

    print(f"\nSuma de los dígitos del primer número: {suma_de_digitos(num1)}")
    print(f"Suma de los dígitos del segundo número: {suma_de_digitos(num2)}")

    print("\nEvaluación de expresiones lógicas:")
    for key, value in evaluar_expresion(conjuntoA, conjuntoB).items():
        print(f"{key}: {value if isinstance(value, str) else ('Sí' if value else 'No')}")

    print("\nExpresiones lógicas en lenguaje natural:")
    for key, value in expresion_lenguaje_natural(conjuntoA, conjuntoB).items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
