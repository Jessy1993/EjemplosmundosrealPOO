# Programa para calcular el área de un rectángulo y convertirla a otras unidades
# Desarrollado por [Tu Nombre]

def calcular_area_rectangulo(longitud, ancho):
    """
    Calcula el área de un rectángulo.

    Args:
    longitud (float): La longitud del rectángulo.
    ancho (float): El ancho del rectángulo.

    Returns:
    float: El área del rectángulo.
    """
    return longitud * ancho

def convertir_a_centimetros_cuadrados(area_metros_cuadrados):
    """
    Convierte un área de metros cuadrados a centímetros cuadrados.

    Args:
    area_metros_cuadrados (float): El área en metros cuadrados.

    Returns:
    float: El área en centímetros cuadrados.
    """
    return area_metros_cuadrados * 10000  # 1 m^2 = 10000 cm^2

def main():
    """
    Función principal del programa. Solicita al usuario las dimensiones del rectángulo,
    calcula el área y realiza la conversión a centímetros cuadrados.
    """
    # Solicitar longitud y ancho del rectángulo al usuario
    longitud = float(input("Ingrese la longitud del rectángulo en metros: "))
    ancho = float(input("Ingrese el ancho del rectángulo en metros: "))

    # Calcular el área del rectángulo
    area_metros_cuadrados = calcular_area_rectangulo(longitud, ancho)
    print(f"El área del rectángulo es: {area_metros_cuadrados} metros cuadrados")

    # Convertir el área a centímetros cuadrados
    area_centimetros_cuadrados = convertir_a_centimetros_cuadrados(area_metros_cuadrados)
    print(f"El área del rectángulo es: {area_centimetros_cuadrados} centímetros cuadrados")

if __name__ == "__main__":
    main()
