#Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário.
a = int(input("Digite um número: "))
if a > 0 and a < 10:
    print(f'O número {a} está dentro do intervalo')
else:
    print(f'O número {a} está fora do intervalo')    
