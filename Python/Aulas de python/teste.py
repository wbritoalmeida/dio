''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 


N = int(input())
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
    n-=1'''
A = "123"
B = "1234"
C = "12"
print(f"{A.center(4,' ')}|{B.center(4,' ')}|{C.center(4,' ')}")


print(len(A))