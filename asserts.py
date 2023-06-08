def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        
        primeras_letras.append(palabra[0])
        
    return primeras_letras

print(primera_letra(['Hola', 'Mundo', 1, '']))


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