linha = input().split(' ')
A, B, C = linha
# maior = (A + B + abs(A - B)) / 2 essa é a formula do exercicio, mas sou programador e nao matematico
maior = max(int(A), int(B), int(C))
print(f'{maior} eh o maior')