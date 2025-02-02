#Resoluções de Listas e Dicionários

"""1. Lista de números ao quadrado"""

# lista: list = list(range(1,11))

# for i in lista:
#     print(i**2)

"""2. Modificar lista de linguagens"""

# linguagens = ['Python','PHP','Java','SQL']
# print(linguagens)
# linguagens.pop()
# linguagens.append('Ruby')
# print(linguagens)

"""3. Informações de um livro"""

# livro = {'titulo':'Senhor dos Anéis','ano':2010,'autor':'J. R. R. Tolkien'}
# print(livro)
# print(livro['titulo'])
# print(livro['autor'])
# livro['disponibilidade'] = True
# print(livro)

# for chave,valor in livro.items():
#     print(f'{chave}:{valor}')

"""4. Contar ocorrências de caracteres"""

# def calcula_caracteres(palavra):
#     caracteres = {}
#     for letra in palavra:
#         if letra in caracteres:
#             caracteres[letra] += 1
#         else:
#             caracteres[letra] = 1
#     return caracteres
# print(calcula_caracteres('engenharia de dados')) 

"""5. Preço total da lista de compras"""
# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# total = sum(precos[item] for item in lista_compras)
# print(total)

"""6. Eliminação de Duplicatas
Objetivo: Dada uma lista de emails, remover todos os duplicados.
"""

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# print(emails)
# emails_unicos = list(set(emails))
# print(emails_unicos)

"""7. Filtragem de Dados
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18."""

# idades = [22, 15, 30, 17, 18]
# idades_selecionadas = [idade for idade in idades if idade >= 18 ]
# print(idades_selecionadas)

"""8. Ordenação Personalizada
Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome."""

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)

"""9. Agregação de Dados
Objetivo: Dado um conjunto de números, calcular a média.
"""
# numeros = [10, 20, 30, 40, 50]
# print(numeros)
# media = sum(numeros)/len(numeros)
# print(media)

"""10. Divisão de Dados em Grupos
Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
"""
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(valores)
# valores_pares = [valor for valor in valores if valor % 2 == 0]
# valores_impares = [valor for valor in valores if valor % 2 != 0]
# print(valores_pares)
# print(valores_impares)

"""11. Atualização de Dados
Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
"""

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# print(produtos)
# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto['id'] == 2:
#         produto['preço'] = 90
# print(produtos)

"""12. Fusão de Dicionários
Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
"""
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}
# dicionario_fundido1 = {**dicionario1,**dicionario2}
# print(dicionario_fundido1)
# dicionario_fundido2 = dicionario1 | dicionario2
# print(dicionario_fundido2)

"""13. Filtragem de Dados em Dicionário
Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
"""

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# produtos_em_estoque = {produto:quantidade for produto,quantidade in estoque.items() if quantidade > 0}
# print(produtos_em_estoque)

"""14. Extração de Chaves e Valores
Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
"""
# dicionario = {"a": 1, "b": 2, "c": 3}
# chaves = list(dicionario.keys())
# valores = list(dicionario.values())
# print("Chaves:", chaves)
# print("Valores:", valores)

"""15. Contagem de Frequência de Itens
Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
"""

texto = "engenharia de dados"

contagem = {}

for letra in texto:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1
print(contagem)