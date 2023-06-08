def enumeracion():
    print()
    print('Bievenido al Metodo de Enumeracion')
    print()
    
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2<objetivo:
        respuesta+=1
        print(respuesta)

    if respuesta**2==objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        print()
        print('Fin del Metodo de Enumeracion')
    else:
        print('No tiene raiz cuadrada exacta')
        print()
        print('Fin del Metodo de Enumeracion')
        
if __name__ == "__main__":
    enumeracion()
        