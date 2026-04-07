#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if a == b:
    print(f'Os números {a} e {b} são iguais')
elif a != b:
    if a > b:
        print(f'a diferença entre os números {a} e {b} é igual a {a - b}')
    elif b > a:
        print(f'a diferença entre os números {b} e {a} é igual a {b - a}')        

