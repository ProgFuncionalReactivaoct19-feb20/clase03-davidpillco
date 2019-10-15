"""
    file: ejercicio7
    autor: davidpillco
"""
def eval_placas(x):
    iniciales = ["l", "p", "e", "a", "i"]
    if x[0] in iniciales:
        return True
    else:
        return False

placas = ["lba-001", "gma-002", "azx-003", "ess-004",  "oro-100", "mab-001", "iaj-002"] 
resultado = filter(eval_placas, placas)
print(list(resultado))
