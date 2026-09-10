list =  []
listm = []
maiorsal = []
menorsal = []
cont = soma = media = media = maior = menor = 0



print("="*10)
print("    RH   ")
print("="*10)
for c in range(1,6):
    nome = str(input((f"Digite o nome do {c} funcionário: "))).strip()
    list.append(nome)
    sal = float(input("Digite o salário do funcionário: R$"))
    if sal > 3000:
        cont += 1
        listm.append(nome)
    if c == 1:
        maior = sal
        menor = sal
        maiorsal.append(nome)
        menorsal.append(nome)

    elif sal > maior:
        maior = sal
        maiorsal.clear()
        maiorsal.append(nome)

    elif sal < menor:
        menor = sal
        menorsal.clear()
        menorsal.append(nome)


    soma += sal
    print("="*30)


print("="*30)
print("       RESULTADO        ")
print("="*30)
media = soma/c
list.sort()
listm.sort()
print(f"Os funcionários regristados foram {list}")
print(f"A média salarial dos funcionários é de R${media}")
if cont >= 1:
  print(f"Esses são os funcionários que recebem mais de R$3.000 {listm}")
else:
  print("Nenhum funcionário recebe mais de R$3.000")

print(f"O maior salário regristado foi de {maiorsal} com R${maior}")
print(f"O menor salário registrado foi de {menorsal} com R${menor}")