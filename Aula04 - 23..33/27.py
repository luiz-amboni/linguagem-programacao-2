

letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numeros = []
traduzidos = []
digitar = True


while digitar == True:
    try:
        msg = int(input("Para enviar, utilize o comando 'Enviar'.\nDigite um número: "))
        numeros.append(msg)

        if msg == -1:
            digitar = False
        else:
            digitar = True
    except(ValueError):
        print("Por favor, digite números.")


for n in range(len(numeros)):
    x = numeros[n]
    y = letras[x]
    traduzidos.append(y)

print("A mensagem, em forma de lista, é a seguinte:", traduzidos)
