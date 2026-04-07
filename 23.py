"""Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da
divisão por 3."""
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
restoA = a % 3
restoB = b % 3
restoC = c % 3
if restoA > restoB and restoB > restoC:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é a={restoA}, b={restoB}, c={restoC} ')
elif restoA > restoB and restoC > restoB:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é a={restoA}, c={restoC}, b={restoB} ')
elif restoB > restoA and restoA > restoC:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é b={restoB}, a={restoA}, c={restoC} ')
elif restoB > restoC and restoC > restoA:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é b={restoB}, c={restoC}, a={restoA} ')
elif restoC > restoA and restoA > restoB:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é c={restoC}, a={restoA}, b={restoB} ')
elif restoC > restoB and restoB > restoA:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é c={restoC}, b={restoB}, a={restoA} ')
else:
    print(f'A ordem descrescente do resto dos números a= {a}, b={b} e c={c} é c={restoC}, b={restoB}, a={restoA} ')                       