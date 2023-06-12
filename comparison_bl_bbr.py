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
    
    list_size = int(input('De qué tamaño será la lista?\n'))
    target = int(input('Qué número quieres encontrar?\n'))
    
    while True:
        print(f'\nTamaño de la lista actual: {list_size}\nTarget actual: {target}')
        print('¿Qué deseas hacer?')
        print('1. Cambiar el objetivo')
        print('2. Cambiar el tamaño de la lista')
        print('3. Ejecutar la búsqueda con los datos actuales')
        print('4. Salir')
        choice = int(input('> '))
        
        if choice == 1:
            target = int(input('Escoge un nuevo objetivo:\n'))
            
        elif choice == 2:
            list_size = int(input('Escoge un nuevo tamaño para la lista:\n'))
            
        elif choice == 3:
            while True:
                list_l = [random.randint(0, 1000000) for i in range(list_size)]
                list_b_r = sorted([random.randint(0, 1000000) for i in range(list_size)])
                if target in list_l and target in list_b_r:
                    break

            counter_iterations = 0
            _, counter_iterations_l = busqueda_lineal(list_l, target)
            _, counter_iterations_b_r = busqueda_binaria_r(list_b_r, 0, len(list_b_r), target, 0)
            
            #print(f'\n{list_l}')
            print(f'Usando Búsqueda Lineal\nTarget: {target}\nSe realizaron {counter_iterations_l} pasos')
            #print(f'\n{list_b_r}')
            print(f'Usando Búsqueda Binaria Recursiva\nTarget: {target}\nSe realizaron {counter_iterations_b_r} pasos')
            continue
        
        elif choice == 4:
            print('¡Hasta luego!')
            break
        
        else:
            print('Opción inválida. Inténtalo de nuevo.')
            continue