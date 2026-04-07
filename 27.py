"""Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre
eles Caso contrário, calcule e exiba o produto entre eles."""
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
if a > 0 and b > 0:
    soma = a + b
    print(soma)
else:
    produto = a * b
    print(produto)    