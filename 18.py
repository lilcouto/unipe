#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro
a = int(input("Digite um número: "))
if a % 2 == 0 and a > 0:
    print(f'O número {a} é par e positivo')
elif a % 2 == 0 and a < 0:
    print(f'O número {a} é par e negativo')
elif a % 2 == 1 and a > 0:
    print(f'O número {a} é impar e positivo')
elif a % 2 == 1 and a < 0:
    print(f'O número {a} é impar e negativo')
else: 
    print(f'O número {a} é neutro')              
