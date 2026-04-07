# Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”.
a = int(input("Digite um número: "))
if a % 3 == 0:
    print(f'O número {a} é múltiplo de 3')
else:    
    print(f'O número {a} não é múltiplo de 3')