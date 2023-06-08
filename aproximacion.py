def aproximacion():
    print()
    print('Bienvenido a el Metodo de Aproximación')
    print()
    
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2-objetivo)>=epsilon and respuesta <=objetivo:
        print(abs(respuesta**2))
        respuesta+=paso

    if abs(respuesta**2-objetivo)>=epsilon:
        print('No se encontro la raiz cuadrada')
        print()
        print('Fin del Metodo de Aproximación')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        print()
        print('Fin del Metodo de Aproximación')
        
if __name__ == "__main__":
    aproximacion()
    