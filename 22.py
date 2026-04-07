"""Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja
possível realizar a conversão, exiba: “Entrada inválida”. Caso a conversão seja bem-sucedida: Se
o número for maior que 10, exiba: “Alto”. Caso contrário, exiba: “Baixo”
"""
a = input("Digite um valor: ")
for c in a:
    if c < "0" or c > "9":
        print("Entrada inválida")
        break
else: 
    if a != "":
        inteiro = int(a)
        if inteiro > 10:
            print("Alto")
        else:
            print("Baixo")        
