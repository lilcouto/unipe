#Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”
a = int(input("Digite um número: "))
if a > 10 and a < 20:
    print(f'O número {a} está dentro do intervalo')
else:
    print(f'O número {a} está fora do intervalo')    