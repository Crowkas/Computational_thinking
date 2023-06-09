def primera_letra2(lista_de_palabras):
    try:
        primeras_letras = []
        
        for palabra in lista_de_palabras:     
            primeras_letras.append(palabra[0])
            
    except TypeError as e:
        print(e)       
        return primeras_letras
    
    except IndexError as e:
        print(e)       
        return primeras_letras

print(primera_letra2(['Hola', 'Mundo', '', 1]))

if __name__ == '__main__':
    primera_letra2()