def verifica_se_ordem_da_matrix_e_8(matrix):
    contador_linhas = 0
    contador_colunas = 0

    for i in range(len(matrix)):
            contador_linhas =+ 1
            for j in range(i):
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