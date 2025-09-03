import random

opcao = ['tesoura','pedra','papel']

while 1:
    comp = opcao[random.randint(0, 2)]
    
    user = input('Jokenpô: ')
    
    print (f'o computador escolheu {comp}')
    
    if (user == 'pedra' and comp == 'tesoura'): print ('Você Ganhou')
    elif (user == 'tesoura' and comp == 'papel'): print ('Você Ganhou')
    elif (user == 'papel' and comp == 'tesoura'): print ('Você Ganhou')
    elif (user == comp) : print('Empate')
    else : print ('Você Perdeu')
    
    sair = input('sair?')
    if sair == 'sim' : break
