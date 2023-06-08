from aproximacion import aproximacion
from busqueda_binaria import busqueda_binaria
from enumeracion import enumeracion

methods = [
    ("Enumeración", enumeracion),
    ("Aproximación", aproximacion),
    ("Búsqueda Binaria", busqueda_binaria),
    ("Salir", exit)
]

while True:
    print("Bienvenido al menú de métodos:")
    print()
    
    for i, (opcion, _) in enumerate(methods, 1):
        print(f"{i}) {opcion}")
    
    print()
    choice = int(input("Escoge el número del método que deseas utilizar (o ingresa 4 para salir): "))
    print()
        
    if 1 <= choice <= 3:
        method = methods[choice - 1][1]  # Restamos 1 para ajustar el índice de la lista
        print(f"Has seleccionado '{methods[choice - 1][0]}'. Ejecutando el método...")
        method()  # Llamamos al método seleccionado
    elif choice == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

    print()  # Línea en blanco para separar cada ejecución del método

print()
print("¡Hasta luego!")
