linha = input().split(' ')
linha2 = input().split(' ')

codigo, quantidade, valor = linha
codigo2, quantidade2, valor2 = linha2

valor_total = (int(quantidade) * float(valor)) + (int(quantidade2) * float(valor2))

print(f'VALOR A PAGAR: R$ {valor_total:0.2f}')