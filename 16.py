#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
a = int(input("Digite um valor: "))
if type(a) == int:
    print(a * a)
