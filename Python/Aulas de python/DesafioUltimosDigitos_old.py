''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''

N = '''4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554'''

#N = int(input())
N = N.split("\n")
n = int(N[0])
cont = 0
while(n > 0):
    cont+=1
    A = N[cont].split(" ")
    B = A[1]
    A = A[0]
    tamanho_B = len(B)
    tamanho_A = len(B)
    if tamanho_B <= tamanho_A:
        if A[-1*tamanho_B:] == B:
            print("encaixa")
        else:
            print("nao encaixa")
    #print(n)
    
    n-=1
    
''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
'''