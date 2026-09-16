import os
from time import sleep

class Correio:
    def enviar(self, taxa1 = 15):

        return taxa1+(2*kg)

class Transporadora_expressa:
    def enviar(self, taxa2 = 30):

        return taxa2+(5*kg)

class Drone:
    def enviar(self, taxa3=50):

        return taxa3


class Uber_flash:
    def enviar(self, taxa4=10):

        return taxa4+(3*km)


co = Correio()
exp = Transporadora_expressa()
dro = Drone()
ubf = Uber_flash()
tot = totc = tote = totd = totu = qtd1 = qtd2 = qtd3 = qtd4 = qtdtot = 0

print("Bem vindo ao LogiExpress, aqui você pode enviar suas mercadorias de forma rápida e segura.")
nome = str(input("Digite seu nome: ")).strip().upper()
cpf = str(input("Digite seu CPF: ")).strip()
os.system('cls')
while True:
    print("=== LogiExpress ===")
    print("[1] - CORREIOS ")
    print("[2] - TRANSPORTADORA EXPRESSA ")
    print("[3] - DRONE (até 200g)")
    print("[4] - UBER FLASH")
    escolha = str(input("Qual opção você deseja? ")).strip()


    if escolha == "1":
        os.system('cls')
        print("==========CORREIOS==========")
        print("Taxa fixa R$15 + R$2 por kg.")
        print("=============================")
        kg = float(input("Digite o peso da mercadoria: kg "))
        va = co.enviar()
        totc += co.enviar()
        qtd1 += 1
        
        print(f"O valor ficará em R${va:.2f}")
        sleep(2)
        

    elif escolha == "2":
        os.system('cls')
        print("==TRANSPORTADORA EXPRESSA==")
        print("Taxa fixa R$30 + R$5 por kg.")
        print("=============================")
        kg = float(input("Digite o peso da mercadoria: kg "))
        va = exp.enviar() 
        tote += exp.enviar()
        qtd2 += 1
        
        print(f"O valor ficará em R${va:.2f}")
        sleep(2)
        

    elif escolha == "3":
        os.system('cls')
        print("===================DRONE================")
        print("Taxa fixa R$50,00 (até 200g).")
        g = float(input("Digite a peso da mercadoria: g "))
        print("==========================================")
        if g <= 200:
          va = dro.enviar()
          totd += dro.enviar()
          qtd3 += 1
          print(f"O valor é fixo de R${va:.2f}.")
          sleep(2)
        else:
            print("Esse peso excede o máximo, procure outra forma de envio: ")
            sleep(2)

    elif escolha == "4":
        os.system('cls')
        km = float(input("Digite quantos KM tem esta entrega: "))
        va = ubf.enviar()
        totu += ubf.enviar()
        qtd4 += 1
        
        print(f"O valor dá entrega ficou R${va:.2f}")
        sleep(2)

    

    else:
        
        print("Você digitou um opção inválida, tente novamente.")
        sleep(2)

    tot = totc + tote + totd + totu
    qtdtot = qtd1 + qtd2 + qtd3 + qtd4
    print(" ")
    cont = str(input("Deseja enviar outra mercadoria? [S/N] ")).strip().upper()
    if cont == "N":
        os.system('cls')
        break
    
    elif cont == "S":
        os.system('cls')
        continue
    else:
        print("Você digitou uma opção inválida, tente novamente.")
        sleep(2)
        os.system('cls')
        continue
      


if tot == 0:
    os.system('cls')
    print("Você não realizou nenhuma compra.")
    print("Obrigado por utilizar o LogiExpress, volte sempre!")
else:
    while True:
        print(f"O valor total da sua compra ficou em R${tot:.2f}")
        print("[1] - PIX \n[2] - CARTÃO DE CRÉDITO \n[3] - CARTÃO DE DÉBITO")
        pg = str(input("Escolha a forma de pagamento: ")).strip()
        if pg == "1":
            os.system('cls')
            print("Você escolheu PIX")
            print("Gerando QR Code...")
            sleep(2)
            print("Pagamento realizado com sucesso!")
            sleep(3)
            break

        elif pg == "2":
            os.system('cls')
            print("Você escolheu CARTÃO DE CRÉDITO, o pagamento será parcelado em até 12x.")
            print("Quantas parcelas deseja? (1 a 12)")
            parcelas = int(input("Digite o número de parcelas: "))
            print("Confirmando pagamento...")
            sleep(2)
            print("O pagamento foi realizado com sucesso!")
            sleep(3)
            break
        elif pg == "3":
            os.system('cls')
            print("Você escolheu CARTÃO DE DÉBITO")
            print("Confirmando pagamento...")
            sleep(2)
            print("O pagamento foi realizado com sucesso!")
            sleep(3)
            break
        print("Você digitou uma opção inválida, tente novamente.")
        sleep(2)
        os.system('cls')
    
    if pg == "1":
        os.system('cls')
        print("Gerando a nota fiscal...")
        sleep(2)
        os.system('cls')
        print("=========== NOTA FISCAL =============")
        print(f"CLIENTE:{nome}")
        print(f"CPF:{cpf}")
        print(" ")
        print("ITENS DE ENVIO")
        print(f"{qtd1}x CORREIOS:                  R${totc:.2f}")
        print(f"{qtd2}x TRANSPORTADORA EXPRESSA:   R${tote:.2f}")
        print(f"{qtd3}x DRONE:                     R${totd:.2f}")
        print(f"{qtd4}x UBER FLASH:                R${totu:.2f}")
        print("Forma de pagamento:           PIX")   
        print("")
        print(f"TOTAL ITENS:                  {qtdtot}x")
        print(f"TOTAL:                        R${tot:.2f} ")
        print("========================================")

    elif pg == "2":
        os.system('cls')
        print("Gerando a nota fiscal...")
        sleep(2)
        os.system('cls')
        print("=========== NOTA FISCAL =============")
        print(f"CLIENTE:{nome}")
        print(f"CPF:{cpf}")
        print(" ")
        print("ITENS DE ENVIO")
        print(f"{qtd1}x CORREIOS:                 R${totc:.2f}")
        print(f"{qtd2}x TRANSPORTADORA EXPRESSA:  R${tote:.2f}")
        print(f"{qtd3}x DRONE:                    R${totd:.2f}")
        print(f"{qtd4}x UBER FLASH:               R${totu:.2f}")
        print(f"Forma de pagamento:          {parcelas}x Crédito")
        print(" ")
        print(f"TOTAL ITENS:                 {qtdtot}x")
        print(f"TOTAL:                       R${tot:.2f} ")
        print("========================================")

    elif pg == "3":
        os.system('cls')
        print("Gerando a nota fiscal...")
        sleep(2)
        os.system('cls')
        print("=========== NOTA FISCAL =============")
        print(f"CLIENTE:{nome}")
        print(f"CPF:{cpf}")
        print(" ")
        print("ITENS DE ENVIO")
        print(f"{qtd1}x CORREIOS:                 R${totc:.2f}")
        print(f"{qtd2}x TRANSPORTADORA EXPRESSA:  R${tote:.2f}")
        print(f"{qtd3}x DRONE:                    R${totd:.2f}")
        print(f"{qtd4}x UBER FLASH:               R${totu:.2f}")
        print("Forma de pagamento:          DÉBITO")
        print(" ")
        print(f"TOTAL ITENS:                {qtdtot}x")
        print(f"TOTAL:                      R${tot:.2f} ")
        print("========================================")

    
