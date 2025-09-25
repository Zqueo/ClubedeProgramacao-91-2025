def delta (a, b, c):
    resultado = (b**2) - (4 * a * c)
    return resultado
    
def r_positivo (a, b, d):
    resultado = (-b + d**0.5)/2*a
    return (resultado)
    
def r_negativo (a, b, d):
    resultado = (-b - d**0.5)/2*a
    return (resultado)

def bhaskara():
    val_a = int(input("a:"))
    val_b = int(input("b:"))
    val_c = int(input("c:"))
    
    d = delta(val_a, val_b, val_c)
    
    x1 = r_positivo(val_a, val_b, d)
    x2 = r_negativo(val_a, val_b, d)
    
    if d < 0:
        print("raiz negativa")
    else:
        #print (f'O resultado foi {x1} e {x2}')
        print ('S={'+str(x1)+','+str(x2)+'}')
        
    escolha = input("deseja fazer outra conta?? (s/n)")
    if escolha == 's':
        bhaskara()
        
bhaskara()
