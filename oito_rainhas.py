'''Implentação das funções usadas nos testes'''

def verifica_se_ordem_da_matrix_e_8(matrix):
    '''Verifica se a ordem de uma dada matrix é 8'''

    contador_colunas = 0

    contador_linhas = len(matrix)

    if contador_linhas == 8:
        for i in range(contador_linhas):
            contador_colunas = len(matrix[i])

            if contador_colunas != 8:
                break

    if contador_linhas == 8 and contador_colunas == 8:
        return 8
    return 0


def verifica_se_ha_8_rainhas(matrix):
    '''Retorna o número de rainhas'''

    contador_de_rainhas = 0
    tamanho_matrix = len(matrix)

    for i in range(tamanho_matrix):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                contador_de_rainhas += 1

    return contador_de_rainhas


def ataque_horizontal(matrix):
    '''Retorna se True se há mais de uma rainha em cada linha'''

    tamanho_matrix = len(matrix)

    for i in range(tamanho_matrix):
        rainhas_na_linha = matrix[i].count(1)

        if rainhas_na_linha > 1:
            break

    if rainhas_na_linha > 1:
        return True
    return False


def ataque_vertical(matrix):
    '''Retorna se True se há mais de uma rainha em cada coluna'''

    tamanho_matrix = len(matrix)
    coluna = 0
    rainhas_na_coluna = 0

    for i in range(8):
        for i in range(tamanho_matrix):
            if matrix[i][coluna] == 1:
                rainhas_na_coluna += 1

        coluna += 1

        if rainhas_na_coluna > 1:
            break
        rainhas_na_coluna = 0

    if rainhas_na_coluna > 1:
        return True
    return False


def ataque_diagonal_principal(matrix):
    '''Retorna se há ataque na diagonal principal'''

    tem_ataque = False
    flag = False

    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                coluna = j
                flag = True
                break

        if flag is True and i <= 6 and coluna <= 6:
            flag = False

            for k in range(i+1, 8):
                for _ in range(coluna + 1, coluna + 2):
                    coluna += 1
                    if matrix[k][_] == 1:
                        tem_ataque = True
                        break
                if tem_ataque is True or coluna == 7:
                    break

    return tem_ataque


def ataque_diagonal_secundaria(matrix):
    '''Retorna se há ataque na diagonal secundária'''

    tem_ataque = False
    flag = False

    for i in range(7, -1, -1):
        for j in range(7, -1, -1):
            if matrix[i][j] == 1:
                coluna = j
                flag = True
                break

        if flag is True and i >= 1 and coluna >= 1:
            flag = False

            for k in range(i-1, 0, -1):
                for _ in range(coluna - 1, coluna - 2, -1):
                    coluna -= 1
                    if matrix[k][_] == 1:
                        tem_ataque = True
                        break
                if tem_ataque is True or coluna == 0:
                    break

    return tem_ataque

def ataque_diagonal(matrix):
    '''Retorna se ha ataque na diagonal principal ou diagonal secundária'''

    if ataque_diagonal_principal(matrix) or ataque_diagonal_secundaria(matrix):
        return True
    return False

def e_uma_solucao(matrix):
    '''Retorna um valor indicando se é a solução para o desafio ou não'''

    if verifica_se_ha_8_rainhas(matrix) != 8 or verifica_se_ordem_da_matrix_e_8(matrix) != 8:
        return -1
    if ataque_horizontal(matrix) is True or ataque_vertical(matrix) is True:
        return 0
    if ataque_diagonal(matrix) is True:
        return 0
    return 1

tabuleiro = [[0,0,0,0,1,0,0,0],[0,1,0,0,0,0,0,0], [0,0,0,1,0,0,0,0], [0,0,0,0,0,0,1,0],
[0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
