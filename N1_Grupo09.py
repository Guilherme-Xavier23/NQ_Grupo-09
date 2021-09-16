# BIBLIOTECA PARA A FUNÇÃO 'portal()'

import random

# SALA 1 ===================================================================================================================================
def sala_1():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\n\t_____________________________\n\n\t     Bem vindo ao Jogo!\n\t_____________________________\n\n\t *** Você esta na Sala 1 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    
        if(resposta_do_usuario == '1'):
            sala_2()
        elif(resposta_do_usuario == '2'):
            sala_3()
    
    return interaçoes

# SALA 2 ====================================================================================================================================
def sala_2():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\t *** Você esta na Sala 2 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    
        if(resposta_do_usuario == '1'):
            sala_3()
        elif(resposta_do_usuario == '2'):
            sala_4()
    
    return interaçoes

# SALA 3 =====================================================================================================================================
def sala_3():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\t *** Você esta na Sala 3 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')

        if(resposta_do_usuario == '1'):
            sala_4()
        elif(resposta_do_usuario == '2'):
            sala_5()
    
    return interaçoes

# SALA 4 =====================================================================================================================================
def sala_4():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\t *** Você esta na Sala 4 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    
        if(resposta_do_usuario == '1'):
            sala_5()
        elif(resposta_do_usuario == '2'):
            sala_6()
    
    return interaçoes

# SALA 5 ======================================================================================================================================
def sala_5():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\t *** Você esta na Sala 5 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    
        if(resposta_do_usuario == '1'):
            sala_6()
        elif(resposta_do_usuario == '2'):
            sala_7()
    
    return interaçoes

# SALA 7 =======================================================================================================================================
def sala_7():

    global interaçoes

    if interaçoes >= 7:
        print('\n\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1

        resposta_do_usuario = input ('\t *** Você esta na Sala 7 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    
        if(resposta_do_usuario == '1'):
            sala_8()
        elif(resposta_do_usuario == '2'):
            sala_9()
    
    return interaçoes

# SALA 6 =======================================================================================================================================
def sala_6():
    
    global interaçoes

    if interaçoes >= 7:
       print('\n\t  Limite de ações atingido!\n\t\tTente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1
    
        resposta_do_usuario = input ('\t *** Você esta na Sala 6 ***\n\n\tHá apenas um caminho a seguir.\n\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________')

        while(resposta_do_usuario != '2'):
            if interaçoes >= 7:
                print('\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
                break
            else:
                interaçoes = interaçoes + 1
    
                resposta_do_usuario = input ('\n\t       Valor incorreto!\n\t       Tente novamente\n\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

                print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')
    if interaçoes < 7:        
        sala_8()

    return interaçoes

# SALA 8 ========================================================================================================================================
def sala_8():
    
    global interaçoes
    
    if interaçoes >= 7:
        print('\t  Limite de ações atingido!\n\t      Tente novamente.\n\t_____________________________\n')
    else:
        interaçoes = interaçoes + 1
    
        resposta_do_usuario = input ('\t *** Você esta na Sala 8 ***\n\n\tQual caminho deseja seguir?\n\n\t[1] Caminho vermelho\n\t[2] Caminho preto\n\n\tVocê escolheu: ')

        print(f'\t_____________________________\n\n\t   Tentativas restantes: {7-interaçoes}\n\t_____________________________\n')

        if (resposta_do_usuario == '1'):
            sala_9()

        elif(resposta_do_usuario == '2'):
            portal()

    return interaçoes
    
def sala_9():
    print('\t *** Você esta na Sala 9 ***\n\n\t    Você concluiu o jogo!')

    print(f'\t_____________________________\n\n\t    Tentativas totais: {interaçoes}\n\t_____________________________\n')

# FUNÇÃO PARA O PORTAL (SALA 8) ==================================================================================================================
def portal():
    
    lista_de_salas = ['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4', 'Sala 5']

    sala_sorteada = random.choice(lista_de_salas)

    input (f'\tVocê caiu em um portal mágico\n\t que o teletransportou para:\n\n\t           [{sala_sorteada}]\n\t_____________________________')

    if sala_sorteada == 'Sala 1':
        sala_1()
    elif sala_sorteada == 'Sala 2':
        sala_2()
    elif sala_sorteada == 'Sala 3':
        sala_3()
    elif sala_sorteada == 'Sala 4':
        sala_4()
    elif sala_sorteada == 'Sala 5':
        sala_5()

# PROGRAMA PRINCIPAL =============================================================================================================================
interaçoes = 0
sala_1()
