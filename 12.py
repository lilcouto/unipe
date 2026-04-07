#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if a > b:
    print(f'A soma entre o número {a} e o número {b} é {a + b}')
    print(f'O número {a} é maior que o número {b}')
elif b > a:
    print(f'A soma entre o número {a} e o número {b} é {a + b}')
    print(f'O número {b} é maior que o número {a}')
else:
    print(f'A soma entre o número {a} e o número {b} é {a + b}')
    print(f'O número {b} e o número {a} são iguais')     