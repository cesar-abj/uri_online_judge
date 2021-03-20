nome = input()
salario = float(input().strip())
vendas = float(input())
comissao = vendas * 15 / 100
salario_total = salario + comissao
print(f'TOTAL = R$ {salario_total:0.2f}')