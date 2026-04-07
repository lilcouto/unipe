"""Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja possível,
exiba: “Entrada inválida”; Caso seja possível: Verifique se o número é par: Se for par e maior que 100 →
exiba: “Par alto”; Se for par e menor ou igual a 100 → exiba: “Par baixo”; Caso não seja par, exiba:
“Ímpar”"""
a = input("Digite um valor: ")
for c in a:
    if c < "0" or c > "9":
        print("Entrada inválida")
        break
else:
    if a != "":
        inteiro = int(a)
        if inteiro % 2 == 0 and inteiro <= 100:
            print("Par baixo")
        elif inteiro % 2 == 0 and inteiro > 100:
            print("Par alto")
        else:
            print("Ímpar")        

