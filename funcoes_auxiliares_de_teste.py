'''Alguma funções destinadas para o módulo de testes'''

def verifica_se_ordem_da_matrix_e_8(matrix):
    '''Verifica se a ordem de uma dada matrix é 8'''

    contador_linhas = 0
    contador_colunas = 0

    for i in range(len(matrix)):
            contador_linhas =+ 1

            for j in range(len(matrix[i])):
                contador_colunas += 1

                if contador_colunas != 8:
                    break
            if contador_colunas != 8:
                break
            else:
                contador_colunas = 0

    if contador_linhas == 8 and contador_colunas == 0:
        return 8
    else:
        return 0

def verifica_se_ha_8_rainhas(matrix):

    contador_de_rainhas = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                contador_de_rainhas += 1
    
    return contador_de_rainhas