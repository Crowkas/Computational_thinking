import random

def busqueda_lineal(list, target):
    counter = 0
    match = False
    
    if target in list:
        for element in list: #O(n)
            counter +=1 
            #print(f'Paso #{counter} = {element}')
            if element == target:
                match = True
                break
            
    return match, counter

def busqueda_binaria_r(list, start, end, target, counter):
    if target in list:
        counter +=1
        #print(f'Paso #{counter}')
        #print(f'buscando {target} entre {list[start]} y {list[end-1]}')
        if start > end:
            return False, counter
        
        middle = (start + end) // 2
        
        if list[middle] == target:
            return True, counter
        
        elif list[middle] < target:
            return busqueda_binaria_r(list, middle + 1, end, target,counter)
        
        else:
            return busqueda_binaria_r(list, start, middle - 1, target, counter)
        
    return False, counter



if __name__ == '__main__':
    list_size = int(input('De que tamaño sera la lista?\n'))
    target = int(input('Que numero quieres encontrar?\n'))

    list_l = [random.randint(0, 10) for i in range(list_size)]
    list_b_r = sorted([random.randint(0, 10) for i in range(list_size)])
    
    if target in list_l and target in list_b_r:

        counter_iterations = 0
        found_l, counter_iterations_l = busqueda_lineal(list_l, target)
        found_b_r, counter_iterations_b_r = busqueda_binaria_r(list_b_r, 0, len(list_b_r), target, counter_iterations)

        print(f'{list_l}\n {list_b_r}')
        
        print(f'\nUsando Busqueda Lineal\nEl elemento {target} {"esta" if found_l else "no esta"} en la lista')
        print(f'Se realizaron {counter_iterations_l} pasos')

        print(f'\nUsando Busqueda Binaria Recursiva\nEl elemento {target} {"esta" if found_b_r else "no esta"} en la lista')
        print(f'Se realizaron {counter_iterations_b_r} pasos')
    
    else:
        print('\nEl objetivo no se encuentra en las dos listas\nReintentelo de nuevo')
        target = int(input('\nQue numero quieres encontrar?\n'))
        counter_iterations = 0
        found_l, counter_iterations_l = busqueda_lineal(list_l, target)
        found_b_r, counter_iterations_b_r = busqueda_binaria_r(list_b_r, 0, len(list_b_r), target, counter_iterations)

        print(f'{list_l}\n{list_b_r}')
        
        print(f'\nUsando Busqueda Lineal\nEl elemento {target} {"esta" if found_l else "no esta"} en la lista')
        print(f'Se realizaron {counter_iterations_l} pasos')

        print(f'\nUsando Busqueda Binaria Recursiva\nEl elemento {target} {"esta" if found_b_r else "no esta"} en la lista')
        print(f'Se realizaron {counter_iterations_b_r} pasos')
    