
numeros = [2,5,6,99,13,23,49,76]
print(numeros)

def ordenar_lista_numeros(numeros:list) -> list:
    nova_lista_numeros = numeros.copy()
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1,len(nova_lista_numeros)):
            if nova_lista_numeros[j] < nova_lista_numeros[i]:
                nova_lista_numeros[i],nova_lista_numeros[j] = nova_lista_numeros[j],nova_lista_numeros[i]

    return nova_lista_numeros;

numeros_ordenados = ordenar_lista_numeros(numeros)

print(numeros_ordenados)