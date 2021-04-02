linha = input().split(' ')
A, B, C = linha
area_triangulo_retangulo = (float(A) * float(C)) / 2
area_circulo = 3.14159 * pow(float(C), 2)
area_trapezio = ((float(A) + float(B)) / 2) * float(C)
area_quadrado = pow(float(B), 2)
area_retangulo = float(A) * float(B)

print(f"TRIANGULO: {area_triangulo_retangulo:0.3f}")
print(f"CIRCULO: {area_circulo:0.3f}")
print(f"TRAPEZIO: {area_trapezio:0.3f}")
print(f"QUADRADO: {area_quadrado:0.3f}")
print(f"RETANGULO: {area_retangulo:0.3f}")