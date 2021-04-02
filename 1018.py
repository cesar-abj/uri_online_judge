valor = int(input())
op = valor

notas = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0,
}

for nota in notas:
    notas[nota] = (int(op / nota))
    op -= nota * int(op / nota)

print(valor)
print(f'{notas[100]} nota(s) de R$ 100,00')
print(f'{notas[50]} nota(s) de R$ 50,00')
print(f'{notas[20]} nota(s) de R$ 20,00')
print(f'{notas[10]} nota(s) de R$ 10,00')
print(f'{notas[5]} nota(s) de R$ 5,00')
print(f'{notas[2]} nota(s) de R$ 2,00')
print(f'{notas[1]} nota(s) de R$ 1,00')