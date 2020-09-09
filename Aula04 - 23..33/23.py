
lista = []
contador = 5

for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista: ")))


print ("a. Maior elemento: ", max(lista))
print ("b. Soma dos elementos: ", sum(lista))
print ("c. Número de ocorrências do primeiro elemento: ", lista.count(lista[0]))
print ("d. Média dos elementos: ", sum(lista)/contador)
