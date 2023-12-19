''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
- "dict{}": dicionários possuem uma relação de chave - valor. Para cada chave haverá um valor.

Desafio
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser 
apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

'''
def instrucoes():
    print("O valor informado não está no padrão necessário!\n Tente novamente e insira um numero entre 1 e 12.")

month = input("Digite o numero do Mês: ")
tamanho = len(month)
if tamanho > 2:
    instrucoes()
    quit()
for caracteres in month:
    for verificar in "1234567890":
        if verificar == caracteres:           
            break
        elif verificar == "0":
            instrucoes()
            quit()
months_dict = {
 "Mes1": "January",
"Mes2": "February",
"Mes3": "March",
"Mes4": "April",
"Mes5": "May",
"Mes6": "June",
"Mes7": "July",
"Mes8": "August",
"Mes9": "September",
"Mes10": "October",
"Mes11": "November",
"Mes12": "December"
}
month = "Mes"+ month

#print(f"""
#         Você inseriu o número {month[3:]} que corresponde ao mes {months_dict[month]} em inglês.""")

print(months_dict[month])
