"""
    file: ejercicio7
    autor: davidpillco
"""
ciudad = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"] 

resultado = filter(lambda x: len(x)%2 == 0,ciudad)

print(list(resultado))

