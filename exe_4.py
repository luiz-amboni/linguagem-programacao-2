print('Digite uma valor')
valor = int(input())

print('Digite o preço')
preco = int(input())

desc=preco*0.2

calc = valor - (preco-desc)

print('O valor final é R${}'.format(calc))
