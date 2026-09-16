from time import sleep
import os

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial 

    def exibir_saldo(self):
        

        return self._saldo

class Depositar(ContaBancaria):
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito sendo realizado...")
            sleep(2)
            print(f"\033[32mDeposito de R${valor:.2f} feito com sucesso!!!\033[0m")
            sleep(2)
            os.system("cls")
        else:
            print("\033[31mValor de depósito inválido. Tente novamente.\033[0m")
            sleep(2)
            os.system("cls")

class Sacar(ContaBancaria):
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print("Saque sendo realizado...")
            sleep(3)
            print(f"\033[32mSaque de R$ {valor:.2f} realizado com sucesso.\033[0m")
            sleep(3)
            os.system("cls")
        else:
            print("\033[31mSaldo insuficiente ou valor de saque inválido. Tente novamente.\033[0m")
            sleep(3)
            os.system("cls")

class Conta(Depositar, Sacar):
       pass 

print("===============================")
print("  Seja bem-vindo(a) a DevBank! ")
print("===============================")
print("Esse é seu primeiro acesso.\nPrecisamos que você preencha as seguintes informações:")
print(" ")
titular = str(input("Insira seu nome: "))
primeiro = titular.split()[0]
saldo_inicial = (0)
cpf = str(input("Confirme seu CPF: "))
os.system("cls")
print("Verificando CPF.")
sleep(1)
os.system("cls")
print("Verificando CPF..")
sleep(1)
os.system("cls")
print("Verificando CPF...")
sleep(1)
print("\033[32mCPF confirmado com sucesso!\033[0m")
sleep(2)
os.system("cls")
print("Agora estamos concluindo seu cadastro.") 
sleep(1)  
os.system("cls")
print("Agora estamos concluindo seu cadastro..") 
sleep(1)  
os.system("cls")
print("Agora estamos concluindo seu cadastro...") 
sleep(1)       
print("\033[32mCadastro realizado com sucesso!!!\033[0m")
sleep(3)
os.system("cls")
print("Abrindo o menu.")
sleep(1)
os.system("cls")
print("Abrindo o menu..")
sleep(1)
os.system("cls")
print("Abrindo o menu...")
sleep(1)
os.system("cls")
conta = Conta(titular, saldo_inicial)

while True:
    print("\033[33m=============\033[0m")
    print("\033[33m   DevBank   \033[0m")
    print("\033[33m=============\033[0m")
    print(f"\33[33mOlá\033[0m {primeiro}!")
    print(f"Seu saldo atual \33[33mR${conta.exibir_saldo():.2f}\033[0m")
    print(" ")
    print("\033[33m[1]\033[0mDEPOSITAR \n\033[33m[2]\033[0mSACAR \n\033[33m[3]\033[0mSAIR")
    print(" ")
    esc = str(input("Digite o que você deseja consultar: ")).strip()
    
    

    if esc == "1":
            os.system("cls")
            print("\033[33m=============\033[0m")
            print("\033[33m  DEPOSITOS  \033[0m")
            print("\033[33m=============\033[0m")
            deposito = float(input("Digite o valor a ser depositado: R$"))
            conta.depositar(deposito)
            

    elif esc == "2":
           os.system("cls")
           print("\033[33m=============\033[0m")
           print("\033[33m    SAQUES   \033[0m")
           print("\033[33m=============\033[0m")
           saque = float(input("Digite o valor a ser sacado: R$"))
           conta.sacar(saque)

    elif esc == "3":
         break

    else:
        print("\033[31mOpção inválida, tente novamente...\033[0m")
        sleep(2)
        os.system("cls")
    
os.system("cls")
print("Obrigado por usar nossos serviços, volte sempre a \033[33mDevBank\033[0m agradece!")
            

            




