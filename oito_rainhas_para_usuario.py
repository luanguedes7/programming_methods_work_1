'''Implentação da Verificação de um dado tabuleiro pelo usuário'''

import oito_rainhas

VERIFICAR = True

def tabuleiro_e_solucao(matrix):
    '''Retorna se o tabuleiro é uma solução'''

    if oito_rainhas.verifica_se_ha_8_rainhas(matrix) != 8:
        return -1
    if oito_rainhas.verifica_se_ha_8_rainhas(matrix) != 8:
        return -1
    if oito_rainhas.ataque_horizontal(matrix) is True:
        return 0
    if oito_rainhas.ataque_vertical(matrix) is True:
        return 0
    if oito_rainhas.ataque_diagonal(matrix) is True:
        return 0
    return 1

while VERIFICAR is True:
    tabuleiro = []
    print('Digite 8 vetores contendo uma rainha em cada:')

    for i in range(8):
        tabuleiro.append(list(map(int, input(f'Digite o vetor {i+1} do tabuleiro: \n').split())))

    print(tabuleiro_e_solucao(tabuleiro))

    continuar = input('Deseja continuar? (S/N) ')

    if continuar.upper() == 'N':
        VERIFICAR = False
