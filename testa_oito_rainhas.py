''' Importações de funções'''
from oito_rainhas import tabuleiro
from funcoes_auxiliares_de_teste import verifica_se_ordem_da_matrix_e_8, verifica_se_ha_8_rainhas

def teste_validade_tabuleiro():
    '''Verifica se o tabuleiro dado pelo usuário é de ordem 8'''
    tab = [8 * [0] for i in range(8)]
    print(tab)

    ordem_tab = verifica_se_ordem_da_matrix_e_8(tab)
    ordem_tabuleiro = verifica_se_ordem_da_matrix_e_8(tabuleiro)

    assert ordem_tab == ordem_tabuleiro

def teste_de_verificacao_de_8_rainhas():
    '''Verifica se o tabuleiro dado pelo usuário apresenta somente 8 rainhas'''

    num_rainhas = verifica_se_ha_8_rainhas(tabuleiro)

    assert num_rainhas == 8

def teste_ataque_horizontal():
    '''Verifica se há rainha em questão será atacada horizontalmente'''

    atacada = ataque_horizontal()

    assert atacada == True
