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
for nota in notas: 
    print(f'{notas[nota]} nota(s) de R$ {nota},00')
