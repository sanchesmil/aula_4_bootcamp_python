import csv

caminho_arquivo_csv: str = 'exemplo.csv'

arquivo_csv: list = []

with open(caminho_arquivo_csv,mode="r",encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)