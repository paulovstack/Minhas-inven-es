from time import sleep

class Cliente:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, saldo):
        self.saldo += saldo
        print(f"Depósito de R${saldo} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, saldo):
        self.saldo -= saldo
        print(f"Saque de R${saldo} realizado. Novo saldo: R${self.saldo}")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.nome}: R${self.saldo}")


nome = input(str("Digite o seu nome: "))
saldo = float(input("Digite o seu saldo: R$"))
cliente = Cliente(nome, saldo)


print(f"Olá {nome} seja bem-vindo(a) ao sistema bancário!")
while True:
    print("\n======================")
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir saldo")
    print("4 - Sair")
    print("\n======================")

    opcao = input("Digite o número da opção desejada: ").strip()

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: R$"))
        print("Processando depósito...")
        sleep(1)
        cliente.depositar(valor_deposito)
        sleep(3)
        
        
        
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: R$"))
        print("Processando saque...")
        sleep(1)
        cliente.sacar(valor_saque)
        sleep(3)
        

    elif opcao == "3":
        print("Consultando saldo...")
        sleep(1)
        cliente.exibir_saldo()
        sleep(3)

    elif opcao == "4":
        print("Obrigado por usar o sistema bancário! Até a próxima.")
        break

    else:
        print("Opção inválida. Tente novamente.")
    
