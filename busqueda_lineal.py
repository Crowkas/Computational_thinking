import random

def busqueda_lineal(list, target):
    counter = 0
    match = False
    
    if target in list:
        for element in list: #O(n)
            counter +=1 
            print(f'Paso #{counter} = {element}')
            if element == target:
                match = True
                break
            
    return match, counter

def busqueda_binaria_r(list, start, end, target, counter):
    counter +=1
    print(f'Paso #{counter}')
    print(f'buscando {target} entre {list[start]} y {list[end-1]}')
    if start > end:
        return False, counter
    
    middle = (start + end) // 2
    
    if list[middle] == target:
        return True, counter
    elif list[middle] < target:
        return busqueda_binaria_r(list, middle + 1, end, target,counter)
    else:
        return busqueda_binaria_r(list, start, middle - 1, target, counter)



if __name__ == '__main__':
    list_size = int(input('De que tamaño sera la lista?\n'))
    target = int(input('Que numero quieres encontrar?\n'))

    list = [random.randint(0, 10) for i in range(list_size)]

    found, counter_iterations = busqueda_lineal(list, target)
    print(list)
    print(f'\nEl elemento {target} {"esta" if found else "no esta"} en la lista')
    print(f'Se realizaron {counter_iterations} pasos')