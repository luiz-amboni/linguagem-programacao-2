

lista=[]
contador=5


for n in range(contador):
    lista.append(int(input("Digite um número: ")))

media= sum(lista)/contador
diffs = {value: abs(value - media) for value in lista}

print ("Média da lista: ", media)
print ("Valor mais próximo: ", diffs)
