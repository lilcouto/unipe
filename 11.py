#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”
a = int(input("Digite um número: "))
if a % 2 == 0 and a >= 0:
    print(f'O número {a} é par e positivo')
elif a % 2 == 0 and a < 0:
    print(f'O número {a} é par e negativo')
else:
    print(f'O número {a} é impar')    
