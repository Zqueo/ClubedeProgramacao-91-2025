def triangulo ():
    base = int(input("digite o valor da base:"))
    altura = int(input("digite o valor da altura:"))
    resultado = (base*altura)/2
    return resultado

def quadrado ():
    lado = int(input("digite o valor do lado do quadrado:"))
    resultado = lado**2
    return resultado

def retangulo ():
    base = int(input("digite o valor da base:"))
    altura = int(input("digite o valor da altura:"))
    resultado = base*altura
    return resultado

def trapezio ():
    baseMa = int(input("digite o valor da base:"))
    baseMe = int(input("digite o valor da base:"))
    altura = int(input("digite o valor da altura:"))
    resultado = ((baseMa + baseMe)*altura)/2
    return resultado

def circulo ():
    pi = 3.14
    raio = int(input("digite o valor do raio:"))
    resultado = pi*(raio**2)
    resultado = int(resultado)
    return (resultado)

def menu():
    escolha = input('''qual area você quer calcular?
    t - triangulo
    q - quadrado
    r - retangulo
    tr - trapezio
    c - circulo
escolha: ''')
    
    if escolha == 't':
        area = triangulo()
    elif escolha == 'q':
        area = quadrado()
    elif escolha == 'r':
        area = retangulo()
    elif escolha == 'tr':
        area = trapezio()
    elif escolha == 'c':
        area = circulo()
        
    print (f"A área é de {area}")
    
    escolha = input('quer calcular outra área? (s/n)').lower()
    if escolha[0] == 's': 
        menu()
    
menu()
