import os
from time import strftime as HORA_DATA

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo = 0.0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES= 3




while True:
    limpar_tela = "\n" * os.get_terminal_size().lines
    opcao = input(menu)
    opcao = opcao.lower()
    
    

    if opcao == "d":
            opcao = ""
            print(f"{limpar_tela}DEPÓSITO\n\n")

            deposito = input("Insira o valor do depósito\n =>")
            print(limpar_tela)

            try:
                deposito = float(deposito)
            except ValueError:
                print("O Valor informado {deposito} não é um valor validor\n\n Para valores quebrados inserir ponto final no lugar da virgula\n\n\n")
            else:
                if deposito > 0.0:
                    hoje = HORA_DATA("%d/%m/%Y - %H:%M:%S")
                    extrato += f"\nDepósito;{hoje};{saldo}; {deposito};"
                    saldo += deposito
                    extrato += f"{saldo}"
                    print(f"Deposito de {deposito} realizado com sucesso!\n\n\n")
                else:
                    print("Inserir somente valores possitivos") 

    if opcao == "s":
            opcao = ""
            print(f"{limpar_tela}SAQUE\n\n")

            saque = input("Insira o valor que quer sacar\n =>")     
                   
            try:
                saque = float(saque)
            except ValueError:
                print(f"{limpar_tela}O Valor informado {saque} não é um valor validor\n\n Para valores quebrados inserir ponto final no lugar da virgula\n\n\n")
            else:
                print(limpar_tela)

                if saque <= saldo:
                    if saque > 0.0 and saque <= limite:
                        numero_saque +=1
                        if numero_saque <= LIMITE_SAQUES:
                            
                            hoje = HORA_DATA("%d/%m/%Y - %H:%M:%S")
                            extrato += f"\nSaque;{hoje};{saldo}; {saque};"
                            saldo -= saque
                            extrato += f"{saldo}"
                            print(f"{limpar_tela}saque de {saque} realizado com sucesso!\n\n\n")
                            
                        else:
                            print("Você atingiu a cota de saques de hoje")
                    else:
                        if saque > limite:
                            print("Valor maximo para saque é de R$ 500,00")
                        else:
                            print("Inserir somente valores possitivos")
                else:
                    print(f"Saldo insuficiente para o saque solicitado\n Saldo atual: {saldo}")

    if opcao == "e":
            opcao = ""
            if extrato != "":
                cabecalio = "MOVIMENTAÇÃO,DATA,VALOR".split(",")                
                
                print(limpar_tela)
                linhas= extrato[1:].split("\n")            
                
                cabecalio = f"""{cabecalio[0].center(15, ' ')}|{cabecalio[1].center(23, ' ')}|{cabecalio[2].center(12, ' ')}
    """
                print(" EXTRATO ".center(len(cabecalio),"_"))
                print()
                
                print(cabecalio)
                for cont_linha in linhas:
                    colunas = cont_linha.split(";")                  
                    print(f"""{colunas[0].center(15, ' ')}| {colunas[1]} |{colunas[3].center(12, ' ')}""")
                input("\n\nAperte enter para continuar")
            else:
                print("Não foi encontrada movimentações")

    if opcao == "q":
            break

    if opcao != "":
            print(f'Insira uma opção valida.\n "{opcao}" não é um opção')
    print(f"""

saldo = {saldo}
limite = {limite}
extrato = {extrato}
numero_saque = {numero_saque}
""")