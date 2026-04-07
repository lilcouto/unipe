"""Leia um número inteiro. Verifique se ele está no intervalo de 1 a 100 (inclusive). Se estiver:
Verifique se o número é par ou ímpar; Exiba: “Par no intervalo” ou “Ímpar no intervalo”. Caso não
esteja no intervalo, exiba: “Fora do intervalo”"""
a = int(input("Digite um número: "))
if a > 0 and a < 101:
    if a % 2 == 0:
        print(f'O número {a} é par e está dentro do intervalo')
    elif a % 2 == 1:
        print(f'O número {a} é ímpar e está dentro do intervalo')
else:
    print("O número está fora do intervalo")            