"""
    file: ejercicio1
    autor: davidpillco
"""
def suma (a,b):
    return a+b

def producto (a,b):
    return a*b    

def disparador(f,a,b):
    print(f(a,b))

disparador (producto, 1 ,10)
