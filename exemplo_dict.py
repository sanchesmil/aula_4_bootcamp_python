import json

produto1: dict = {
    'nome':'sapato',
    'quantidade':39,
    'preco':70.98,
    'disponibilidade': True
}

produto2: dict = {
    'nome':'camiseta',
    'quantidade':20,
    'preco':25.55,
    'disponibilidade': False
}

carrinho:list = []

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# convertendo dict p/ json (javascript)
carrinho_json = json.dumps(carrinho)
print(carrinho_json)