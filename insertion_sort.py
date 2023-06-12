import random

def insertion_order(list):

    for indice in range(1, len(list)):
        valor_actual = list[indice]
        posicion_actual = indice

        while posicion_actual > 0 and list[posicion_actual - 1] > valor_actual:
            list[posicion_actual] = list[posicion_actual - 1]
            posicion_actual -= 1

        list[posicion_actual] = valor_actual
        
    return list
        
if __name__ == '__main__':
    list_size = int(input('De que tamaño sera la lista?'))

    list = [random.randint(0, 10) for i in range(list_size)]
    print(list)

    order_list = insertion_order(list)
    print(order_list)