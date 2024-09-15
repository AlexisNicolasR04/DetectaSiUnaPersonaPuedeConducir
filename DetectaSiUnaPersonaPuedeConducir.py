def puede_conducir(edad, tiene_licencia):
    """Determina si una persona puede conducir basado en su edad y licencia."""
    if edad >= 18 and tiene_licencia:
        return True
    else:
        return False

def main():
    print("Verificador de permiso para conducir (ingresa 'salir' en cualquier momento para terminar)")

    while True:
        # Solicitar la edad de la persona
        edad_input = input("Ingresa tu edad (o 'salir' para terminar): ")
        if edad_input.lower() == 'salir':
            print("Saliendo del programa...")
            break

        try:
            edad = int(edad_input)
        except ValueError:
            print("Por favor, ingresa un número válido para la edad.")
            continue

        # Preguntar si tiene licencia de conducir
        licencia_input = input("¿Tienes licencia de conducir? (sí/no o 'salir' para terminar): ").lower()
        if licencia_input == 'salir':
            print("Saliendo del programa...")
            break

        if licencia_input == "sí" or licencia_input == "si":
            tiene_licencia = True
        elif licencia_input == "no":
            tiene_licencia = False
        else:
            print("Entrada inválida para licencia. Por favor, responde con 'sí' o 'no'.")
            continue

        # Determinar si la persona puede conducir
        if puede_conducir(edad, tiene_licencia):
            print("Puedes conducir.")
        else:
            print("No puedes conducir.")

if __name__ == "__main__":
    main()
