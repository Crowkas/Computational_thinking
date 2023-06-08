#Solo funciona con conjuntos ordenados
def busqueda_binaria():
    print()
    print('Bievenido al Metodo de Busqueda Binaria')
    print()
    
    objetivo = int(input('Escoge un entero: '))
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo)/2

    while abs(respuesta**2-objetivo)>=epsilon:
        print(f'*******\nbajo = {bajo}\nalto = {alto}\nrespuesta = {respuesta}\nrespuesta² = {respuesta**2}\nobjetivo = {objetivo}\nepsilon = {epsilon}\n{respuesta**2} - {objetivo} = {respuesta**2-objetivo}\n*******')
        if respuesta**2<objetivo:
            bajo = respuesta
        else: 
            alto = respuesta
            
        respuesta = (alto+bajo)/2
        
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print()
    print('Fin del Metodo de Busqueda Binaria')
    
if __name__ == "__main__":
    busqueda_binaria()
    