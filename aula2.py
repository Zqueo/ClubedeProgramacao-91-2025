# Exercício 1 - Média Escolar
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota:'))

resultado = (nota1 + nota2 + nota3 + nota4) /4

print ('A media é:' + str(resultado))


if (resultado<=10) and (resultado>=6):
    print ('Aprovado')
elif (resultado<6) and (resultado>=5):
    print ('Recuperação')
elif (resultado<5) and (resultado>=0):
    print ('Reprovado')
else :
    print ('Valor Inválido')

# Exercício 2 - Números Primos
indice = 1
limite = 100
controle = 0
indice2 = 1
while (indice <= limite):
    indice2 = indice
    controle = 0
    
    while (indice2 > 0):
        if (indice % indice2 == 0):
            controle = controle + 1
        indice2 = indice2 - 1
    if (controle == 2):
        print (indice)
    indice = indice + 1
