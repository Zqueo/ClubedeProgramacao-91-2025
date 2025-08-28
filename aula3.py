# Exercício 3 - Laços de Repetição

i = 0
while 1:
    i+=1
    if i == 11:
        break
    if i % 2 == 1:
        continue
    print (i)
    
    
# Exercício 4 - Manipulação de Listas

frutas = ['abacaxi','maça','banana','kiwi','morango','kibe','manga','limão','uva','mamão']

frutas.append('mirtilo')
frutas.append('pitaia')
frutas.remove('kibe')

for fruta in frutas:
    print (fruta)
    


# Exercício 5 - Jogo de Adivinhação
import random

numero = random.randint(1,100)
palpite = 0
tentativa = 0

while 1:
    tentativa += 1
    print ('Tentativa ' + str(tentativa))
    palpite = int( input('Digite o seu palpite: '))
    if palpite <= 0 or palpite > 100:
        print ('número inválido')
        continue
    if palpite == numero:
        print ('Você acertou!!')
        break
    elif palpite > numero:
        print ('palpite é maior que o número')
    elif palpite < numero:
        print ('palpite é menor que o número')
