import os
from random import randint
from pyfiglet import Figlet


def menu():
    limpatela()
    print(linha(60))
    print()
    print(f.renderText("TIC TAC TOE"))
    print(linha(60))
    print('[1] PLAYER Vs COM \n[2] PLAYER Vs PLAYER\n[3] REGRAS \n[4] EXIT')


def escolhamenu():
    GameType = validaresposta('Opção: ', 4, 1)
    return GameType


def regras():
    print("""
        ____________________________________________________________
        ____________________JOGO DA VELHA___________________________
        _______________________REGRAS_______________________________
        - O tabuleiro  é uma matriz  de três linhas por três colunas.
        - Dois jogadores escolhem uma marcação cada um, geralmente um 
        - círculo (O) e um xis (X).
        - Os jogadores jogam alternadamente, uma marcação por vez, 
        - numa lacuna que esteja vazia.
        - O objectivo é conseguir três círculos ou três xis em linha, 
        - quer horizontal, vertical ou diagonal , e ao mesmo tempo, 
        - quando possível, impedir o adversário de ganhar na próxima 
        - jogada.
        - Se os dois jogadores jogarem sempre da melhor forma, o 
        - jogo terminará sempre em empate.
        
        CAIO OLIVEIRA, 2020
        TIC TAC TOE - VERSÃO 1.0 BETA
        """)


def entitulador(msg):
    print(linha(len(msg) + 4))
    print(f'  {msg}   ')
    print(linha(len(msg) + 4))


def linha(tam=30):
    return '-' * tam


def validaresposta(msg, lastN=3, FirstN=1):
    """
    ------> Valida um range de resposta do usuário (apenas inteiro)
    :param msg: Mensagem que o usuário vai ver
    :param lastN: Ultimo número da lista de opções (3 por padrão)
    :param FirstN: Primeiro número da lista de oções (1 por padrão)
    :return: retorna a opção validada
    """
    while True:
        try:
            opc = int(input(msg))
        except (ValueError, TypeError):
            print('Apenas números inteiros!!!')
            continue
        except KeyboardInterrupt:
            print('Operação cancelada pelo usuário!!')
            break
        else:
            if lastN >= opc >= FirstN:
                return opc
            else:
                print('Opção inválida')
                continue


def showboard(matriz):
    """
   --------> FUNÇÃO QUE MOSTRA MATRIZ
   :param board:Matriz a ser printada 
   """""
    entitulador('  TIC TAC TOE   ')
    for l in range(len(matriz)):
        print(linha(25))
        print('|', end='')
        for c in range(len(matriz)):
            print(f'   {matriz[l][c]}   |', end='')
        print()
    print(linha(25))


def escolhejogador():
    print('O primeiro a jogar escolhe: ')
    entitulador('Escolha [1] para X e [2] para O')
    j1 = validaresposta('OPÇÃO: ', 2, 1)
    if j1 == 1:
        j1 = 'X'
    else:
        j1 = 'O'
    return j1


def joga(matrix, player):
    while True:
        try:
            jogada = validaresposta(f'Vai jogar {player} aonde?: ', 9, 1)
        except:
            print('Já jogaram ai!')
        else:
            for l in range(len(matrix)):
                for c in range(len(matrix)):
                    if jogada == matrix[l][c]:
                        matrix[l][c] = player
                        return matrix
                    else:
                        continue


def computador(matrix, computer):
    while True:
        try:
            insert = randint(1, 9)
        except:
            print('Já jogaram ai!!')
        else:
            for l in range(len(matrix)):
                for c in range(len(matrix)):
                    if insert == matrix[l][c]:
                        matrix[l][c] = computer
                        return matrix
                    else:
                        continue


def verificadorDeVencedor(matriz, player):
    return (matriz[0][0] == matriz[0][1] == matriz[0][2] == player) or \
           (matriz[1][0] == matriz[1][1] == matriz[1][2] == player) or \
           (matriz[2][0] == matriz[2][1] == matriz[2][2] == player) or \
           (matriz[0][0] == matriz[1][0] == matriz[2][0] == player) or \
           (matriz[0][1] == matriz[1][1] == matriz[2][1] == player) or \
           (matriz[0][2] == matriz[1][2] == matriz[2][2] == player) or \
           (matriz[0][0] == matriz[1][1] == matriz[2][2] == player) or \
           (matriz[0][2] == matriz[1][1] == matriz[2][0] == player)


def verificadorDeEmpate(matriz):
    counter = 0
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[l][c] == 'X':
                counter += 1
            if matriz[l][c] == 'O':
                counter += 1
    if counter == 9:
        return True
    else:
        return False


def limpatela():
    os.system('cls')


# limpa o terminal
limpatela()
# aplicação
f = Figlet(font='slant')
while True:
    menu()
    opc = escolhamenu()
    if opc == 1:
        limpatela()
        jogador1 = escolhejogador()
        if jogador1 == 'X':
            jogador2 = 'O'
        else:
            jogador2 = 'X'
        player = jogador1
        com = jogador2
        jogadorAtual = jogador1
        board = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        limpatela()
        while True:
            if jogadorAtual == player:
                showboard(board)
                joga(board, jogadorAtual)
                venceu = verificadorDeVencedor(board, jogadorAtual)
                empate = verificadorDeEmpate(board)
                if venceu:
                    limpatela()
                    showboard(board)
                    entitulador(f'Parabéns jogador {jogadorAtual}, você ganhou!!!')
                    sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                    if sair_do_jogo == 1:
                        break
                else:
                    if empate:
                        limpatela()
                        showboard(board)
                        entitulador(f'Infelizmente nenhum jogador ganhou!')
                        sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                        if sair_do_jogo == 1:
                            break
                    else:
                        if jogadorAtual == jogador1:
                            jogadorAtual = jogador2
                        else:
                            jogadorAtual = jogador1
            elif jogadorAtual == com:
                limpatela()
                computador(board, jogadorAtual)
                venceu = verificadorDeVencedor(board, jogadorAtual)
                empate = verificadorDeEmpate(board)
                if venceu:
                    limpatela()
                    showboard(board)
                    entitulador(f'O computador venceu tente novamente!')
                    sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                    if sair_do_jogo == 1:
                        break
                else:
                    if empate:
                        limpatela()
                        showboard(board)
                        entitulador(f'Infelizmente nenhum jogador ganhou!')
                        sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                        if sair_do_jogo == 1:
                            break
                    else:
                        if jogadorAtual == jogador1:
                            jogadorAtual = jogador2
                        else:
                            jogadorAtual = jogador1
    elif opc == 2:
        limpatela()
        jogador1 = escolhejogador()
        if jogador1 == 'X':
            jogador2 = 'O'
        else:
            jogador2 = 'X'
        jogadorAtual = jogador1
        board = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        limpatela()
        while True:
            showboard(board)
            joga(board, jogadorAtual)
            venceu = verificadorDeVencedor(board, jogadorAtual)
            empate = verificadorDeEmpate(board)
            if venceu:
                limpatela()
                showboard(board)
                entitulador(f'Parabéns jogador {jogadorAtual}, você ganhou!!!')
                sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                if sair_do_jogo == 1:
                    break
            else:
                if empate:
                    limpatela()
                    showboard(board)
                    entitulador(f'Infelizmente nenhum jogador ganhou!')
                    sair_do_jogo = validaresposta('Digite 1 para voltar ao menu: ', 1, 1)
                    if sair_do_jogo == 1:
                        break
                else:
                    if jogadorAtual == jogador1:
                        jogadorAtual = jogador2
                    else:
                        jogadorAtual = jogador1
            limpatela()
    elif opc == 3:
        while True:
            limpatela()
            regras()
            rule = validaresposta('Digite 1 para voltar para o menu: ', 1, 1)
            if rule == 1:
                break
    elif opc == 4:
        limpatela()
        print(f.renderText("ATE LOGO!!!!!"))
        break
