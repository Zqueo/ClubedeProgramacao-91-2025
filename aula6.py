def soma(val1, val2):
    resultado = val1 + val2
    print (resultado)
    
def subtracao(val1, val2):
    resultado = val1 - val2
    print (resultado)
    
def multiplicacao(val1, val2):
    resultado = val1 * val2
    print (resultado)
    
def divisao(val1, val2):
    if val2 == 0:
        print('erro')
    else:
        resultado = val1 / val2
        print (resultado)
 

while 1:
    operacao = input("qual operação você quer realizar?").lower()
        
    num1 = int(input("digite o primeiro valor"))
    num2 = int(input("digite o segundo valor"))
        
    if operacao == 'soma' or operacao == '+' :
        soma(num1 , num2)
    elif operacao == 'subtracao' or operacao == '-' :
        subtracao(num1 , num2)
    elif operacao == 'multiplicacao' or operacao == '*' :
        multiplicacao(num1 , num2)
    elif operacao == 'divisao' or operacao == '/' :
        divisao(num1 , num2)
    
    continuar = input("deseja fazer outro calculo").lower()
    
    if continuar == 'nao': break
    

'''
1- Pedir dois valores pro usuário
2- Pedir pro usuário informar qual a operação desejada
3- Imprimir o resultado da operação

Bonus:
4- Pergunte pro usuário se ele quer fazer outra operação
5- Tratem o problema da divisão por 0
'''