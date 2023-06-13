counter = 0
"""Complejidad algoritmica O(nW) donde n es el numero de elementos y W el tamano del morral"""

def bag_pack(bag_pack_size, weights, values, n, message):
    
    print('-'*50)
    print(message)
    global counter
    counter += 1
    
    print(f'   * Analizamos Elemento {n} *')
    print(f'   - Espacio en morral = {bag_pack_size}')
    print(f'   - Peso = {weights[n - 1]}, valor = {values[n - 1]} ')
    
    if n == 0 or bag_pack_size == 0:
        if bag_pack_size == 0:
            print('   Espacio en morral lleno!')
        elif n == 0:
            print('   Indice final alcanzado!') 
        return 0
    
    if weights[n-1] > bag_pack_size:
        print('   peso del elemento > espacio morral...')
        return bag_pack(bag_pack_size, weights, values, n-1, '')
    
    return max(values[n - 1] + bag_pack(bag_pack_size - weights[n - 1], weights, values, n - 1, f'--> SI Robo el elemento {n} y sumo a mi morral {values[n - 1]} en valor!'),
                bag_pack(bag_pack_size, weights, values, n - 1, f'--> NO robo el elemento {n}!'))
        

if __name__ =='__main__':
    item_values = int(input('Indique la cantidad de objeos que desea llevar: '))
    values = []
    weights = []
    bag_pack_size = 30
    
    for i in range(item_values):
        value = int(input(f'Indique el valor del objeto #{i+1}: '))
        weight = int(input(f'Indique el peso del objeto #{i+1}: '))
        values.append(value)
        weights.append(weight)
    print(item_values, values, weights)
    
    n = len(values)
    
    result = bag_pack(bag_pack_size, weights, values, n, 'Calculo del problema del moral de forma recursiva')
    
    print(f'\n* El metodo se llamo {counter} veces para calcular {n} elementos')
    print(f'El valor maximo que podemos robar es {result}')
    print('La complejidad del algoritmo es O(nW) donde n es el numero de elementos y W el tamano del morral')