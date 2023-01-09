'''Implentação da Verificação de um dado tabuleiro'''

#Tabuleiro a ser usado para verifição do teste. É baseado na imagem dada no pdf do trabalho.
tabuleiro = [[0,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,0], [0,0,0,1,0,0,0,0], [0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

for i in range(8):
    print(tabuleiro[i], end='\n')

