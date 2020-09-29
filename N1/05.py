letras = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def translate(frase):
    nova_frase = []
    lista_frase = frase.split(',')
    for letra in lista_frase:
        nova_frase.append(letras[int(letra)])
    return ''.join(nova_frase)

while True:
    frase = input("Digite a mensagem codificada, separando os elementos com vírgulas:\n")
    print(translate(frase))