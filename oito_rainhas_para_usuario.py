'''Implentação da Verificação de um dado tabuleiro pelo usuário'''

import oito_rainhas

verificar = True

def tabuleiro_e_solucao(matrix):
    '''Retorna se o tabuleiro é uma solução'''

    if oito_rainhas.verifica_se_ha_8_rainhas(matrix) is not 8:
        return -1
    elif oito_rainhas.verifica_se_ha_8_rainhas(matrix) is not 8:
        return -1
    elif oito_rainhas.ataque_horizontal(matrix) is True:
        return 0
    elif oito_rainhas.ataque_vertical(matrix) is True:
        return 0
    elif oito_rainhas.ataque_diagonal(matrix) is True:
        return 0
    else:
        return 1

while verificar:
    tabuleiro = list()
    print('Digite 8 vetores contendo uma rainha em cada:')

    for i in range(8):
        tabuleiro.append(list(map(int, input(f'Digite o vetor {i+1} do tabuleiro: \n').split())))

    print(tabuleiro_e_solucao(tabuleiro))
        
    continuar = input('Deseja continuar? (S/N) ')
    
    if continuar.upper() == 'N':
        verificar = False
        
