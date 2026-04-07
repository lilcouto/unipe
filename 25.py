"""Leia um valor informado pelo usuário. Exiba o tipo da variável lida. Verifique se é possível
converter o valor para número real (float). Se for possível, exiba o resultado da divisão desse
número por 2. Caso contrário, exiba: “Não numérico”."""
a = input("Digite um valor: ")
for c in a:
    if c < "0" or c > "9":
        print(type(a))
        print("Não numérico")
        break
else:
    if a != "":
        converter = float(a)
        print(converter / 2)  
