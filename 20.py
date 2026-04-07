#Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo,mostre na tela o valor
a = int(input("Digite um número: "))
if a > 0 and a < 100:
    print(f'O número {a} está dentro do intervalo')
else:
    print(f'O número {a} está fora do intervalo')    
