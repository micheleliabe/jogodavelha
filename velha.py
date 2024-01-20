tabuleiro = [' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ' ]


def exibe_tabuleiro(jogadas):

    print(f' {jogadas[0]} | {jogadas[1]} | {jogadas[2]} ')
    print('-----------')
    print(f' {jogadas[3]} | {jogadas[4]} | {jogadas[5]} ')
    print('-----------')
    print(f' {jogadas[6]} | {jogadas[7]} | {jogadas[8]} ')

    print('')


def nova_jogada(jogadas, posicao, valor):
    jogadas[posicao] = valor
    return jogadas


def turno(jogador):
    print("")
    print(f'Vez do jogador {jogador}: ')
    print('')
    posicao = int(input('Informe a posicao: '))
    print("")
    
    global tabuleiro

    while tabuleiro[posicao] != " ":
        posicao = int(input('Informe uma posição vazia: '))
    
    tabuleiro = nova_jogada(tabuleiro, posicao, jogador)
    

def valida_jogadas(jogadas, jogador):
    if   jogadas[0] == jogador and jogadas[1] == jogador and jogadas[2] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[3] == jogador and jogadas[4] == jogador and jogadas[5] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[7] == jogador and jogadas[8] == jogador and jogadas[0] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[0] == jogador and jogadas[3] == jogador and jogadas[6] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[1] == jogador and jogadas[4] == jogador and jogadas[7] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[2] == jogador and jogadas[5] == jogador and jogadas[8] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[0] == jogador and jogadas[4] == jogador and jogadas[8] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif jogadas[6] == jogador and jogadas[4] == jogador and jogadas[2] == jogador:
        print(f'{jogador} venceu !')
        return jogador
    
    elif tabuleiro.count('X') == 5 or tabuleiro.count('O') == 5:
        return "velha"
    else:
        return None


def novo_jogo():
    print('Novo jogo...')
    print('Cada posição do tabuleiro é definida por um numero')
    exibe_tabuleiro(['0','1','2','3','4','5','6','7','8'])


    vencedor = None
    while vencedor == None:
        if vencedor == None:
            turno('X')
            exibe_tabuleiro(tabuleiro)
            vencedor = valida_jogadas(tabuleiro, 'X')
        
        if vencedor == None:
            turno('O')
            exibe_tabuleiro(tabuleiro)
            vencedor = valida_jogadas(tabuleiro,'O')
    
    if vencedor == 'velha':
        print('Deu velha, fim de jogo')
    else:
        print(f'Vencedor: {vencedor}')

novo_jogo()