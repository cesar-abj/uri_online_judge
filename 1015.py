from math import sqrt
linha = input().split(' ')
linha2 = input().split(' ')

x1, y1 = linha 
x2, y2 = linha2

res = pow((float(x2) - float(x1)), 2) + pow((float(y2) - float(y1)), 2)
distancia = sqrt(res)
print(f'{distancia:0.4f}')