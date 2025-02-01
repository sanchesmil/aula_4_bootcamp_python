# Adicionando Type Hint ao código para especificar o tipo de dados esperados por funções e variáveis

""" 
1 O programa deve começar solicitando ao usuário que insira seu nome.
2 Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3 Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4 O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
5 Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
    Exemplo de Saída:
    Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

    Olá Luciano, o seu bônus foi de 8500
"""

CONSTANTE_BONUS:int = 1000

nome_valido:bool = False
salario_valido: bool= False
bonus_valido: bool = False

# Solicita ao usuário que digite seu nome
while not nome_valido: 

    try:
        
        nome:str = input('Digite seu nome: ')        

        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")

        elif any(char.isdigit() for char in nome):
            raise ValueError('Seu nome não pode conter dígitos numéricos.')

        elif nome.isspace():
            raise ValueError('Seu nome não pode ser formado somente por espaços vazios.')

        else:
            nome_valido = True

    except ValueError as e:
        print('Entrada inválida: ', e)

# Solicita ao usuário que digite seu salário
while not salario_valido:
    try:
        salario:float = float(input('Informe seu salário: '))

        if salario <= 0:
            raise ValueError('Salário deve ser maior que zero')
        else:
            salario_valido = True

    except ValueError as e:
        print('Entrada inválida para o salário.', e)


# Solicita ao usuário que digite seu bonus
while not bonus_valido:
    try:
        bonus:float = float(input('Informe o valor da porcentagem de bonus recebido (Ex. 10% = 10): '))

        if bonus <= 0:
            raise ValueError('Bônus deve ser maior que zero.')
        else:
            bonus_valido = True

    except ValueError as e:
        print('Entrada inválida para o bônus.', e)

# realiza o cálculo do bônus final
bonus_recebido:float = CONSTANTE_BONUS + salario * (1 + bonus/100)

# Imprime as informações para o usuário
print(f"{nome.capitalize()}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")