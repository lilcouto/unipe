""" Leia um valor informado pelo usuário. Verifique o tipo da variável; Caso seja possível interpretá-lo
como um valor numérico: Se for um número inteiro, exiba o dobro; Caso seja um número real, exiba a
metade; Caso não seja possível interpretar como número, exiba: “Tipo inválido”."""
a = (input("Digite um valor: "))
pontos = 0
for c in a:
    if (c < "0" or c > "9") and c != ".":
        print("Tipo inválido")
        break
    if c == ".":
        pontos += 1
else:
    if a != "":
        if pontos == 0:
            inteiro = int(a)
            dobro = print(inteiro + inteiro)
        elif pontos == 1:
            real = float(a)
            metade = print(real/2)    
        
