'''Alguma funções destinadas para o módulo de testes e a implementação das oito rainhas'''

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
