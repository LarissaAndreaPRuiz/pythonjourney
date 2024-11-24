
texto = input("Insira um texo: ")

def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador    

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
