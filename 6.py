# Leia dois números e exiba qual é o maior.
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if a < b:
    print(f'o número {a} é menor que o número {b}')
elif a == b:
    print(f'o número {b} são iguais {a}') 
else:
    print(f'o número {b} é menor que o número {a}')       