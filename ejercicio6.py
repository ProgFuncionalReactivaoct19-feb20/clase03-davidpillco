"""
    file: ejercicio6
    autor: davidpillco
"""
def palindromas(x):
        y = "".join(reversed(x))
        if x == y:
            return True
        else:
            return False    
palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
 
resultado = filter(palindromas, palabras)
print(list(resultado))
