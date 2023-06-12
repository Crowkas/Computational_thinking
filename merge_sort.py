import random

def merge_order(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        print(left, '*' * 5, right)
        #llamada recursiva en cada mitad
        merge_order(left)
        merge_order(right)
        
        #iteradores para recorrer las dos sublistas
        i=0
        j=0
        #iterador para recorrer la lista principal
        k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i +=1
            else: 
                list[k] = right[j]
                j +=1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i +=1
            k +=1
            
        while j < len(right):
            list[k] = right[j]
            j +=1
            k +=1
        
        print(f'left {left}, derecha {right}')
        print(list)
        print('-'*50)
    return list
        
if __name__ == '__main__':
    list_size = int(input('De que tamaño sera la lista?\n'))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)
    print('-' * 50)

    order_list = merge_order(list)
    print(order_list)