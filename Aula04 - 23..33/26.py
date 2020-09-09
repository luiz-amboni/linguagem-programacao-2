
lista1=[]
lista2=[]

for n in range(6):
    lista1.append(int(input("Digite um número para a lista 1: ")))

for n in range(6):
    lista2.append(int(input("Digite um número para a lista 2: ")))

if lista1==lista2:
    print(True)
else:
    print(False)

print ("Número de ocorrências do primeiro elemento na lista 1: ", lista1.count(lista1[0]))
print ("Número de ocorrências do primeiro elemento na lista 2: ", lista2.count(lista2[0]))
