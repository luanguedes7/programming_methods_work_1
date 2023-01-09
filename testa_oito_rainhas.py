''' Importações de funções'''
import oito_rainhas

tabuleiro = oito_rainhas.tabuleiro #tabuleiro genérico para os testes

def teste_validade_tabuleiro():
    '''Verifica se o tabuleiro dado pelo usuário é de ordem 8'''
    tab = [8 * [0] for i in range(8)]

    ordem_tab = oito_rainhas.verifica_se_ordem_da_matrix_e_8(tab)
    ordem_tabuleiro = oito_rainhas.verifica_se_ordem_da_matrix_e_8(tabuleiro)

    assert ordem_tab == ordem_tabuleiro

def teste_de_verificacao_de_8_rainhas():
    '''Verifica se o tabuleiro dado pelo usuário apresenta somente 8 rainhas'''

    num_rainhas = oito_rainhas.verifica_se_ha_8_rainhas(tabuleiro)

    assert num_rainhas == 8

def teste_se_nao_ha_ataque_horizontal():
    '''Verifica se há rainha em questão será atacada horizontalmente'''

    atacada_horizontal = oito_rainhas.ataque_horizontal(tabuleiro)

    assert atacada_horizontal is False

def teste_se_nao_ha_ataque_vertical():
    '''Verifica se há rainha em questão será atacada verticalmente'''

    atacada_vertical = oito_rainhas.ataque_vertical(tabuleiro)

    assert atacada_vertical is False

def teste_se_nao_ha_ataque_diagonal():
    '''Verifica se alguma rainha está sendo atacada verticalmente'''

    atacada_diagonal = oito_rainhas.ataque_diagonal(tabuleiro)

    assert atacada_diagonal is False

def teste_se_o_tabuleiro_e_solucao():
    '''Verifica se o tabuleiro é a solução'''

    e_solucao = oito_rainhas.e_uma_solucao(tabuleiro)

    assert e_solucao is True