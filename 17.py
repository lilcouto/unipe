#Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+)
idade = int(input("Digite a sua idade: "))
if idade < 18 and idade >= 0:
    print("Menor de idade")
elif idade >= 18 and idade <=59:
    print("Adulto")
elif idade > 59 and idade < 126:
    print("Idoso")
else:
    print ("Idade inválida")
               