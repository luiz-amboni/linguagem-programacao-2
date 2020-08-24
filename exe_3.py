class Calculadora:

    def calcular_soma(self, n1, n2):
        soma = n1 + n2 + 1
        print('({} + {}) + 1 = {}'.format(n1, n2, soma))

    def calcular_subtracao(self, n1, n2):
        subtracao = n1 - n2 + 1
        print('({} - {}) + 1 = {}'.format(n1, n2, subtracao))

    def calcular_multiplicacao(self, n1, n2):
        multiplicacao = (n1 * n2) + 1
        print('({} * {}) + 1 = {}'.format(n1, n2, multiplicacao))

    def calcular_divisao(self, n1, n2):
        divisao = (n1 / n2) + 1
        print('({} / {}) + 1 = {}'.format(n1, n2, divisao))


calcular = Calculadora()
opçao=-1

while opçao!=0:

    opçao=int(input("Digite uma opção para continuar: \n1-SOMA \n2-SUBTRAÇÃO \n3-MULTIPLICAÇÃO \n4-DIVISÃO \n0-SAIR\n"))

    if opçao==0:
        print("Obrigado por utilizar a calculadora!")
        break

    n1=int(input("Digite o primeiro número do cálculo: "))
    n2=int(input("Digite o segundo número do cálculo: "))


    if opçao==1:
        calcular.calcular_soma(n1,n2)

    if opçao==2:
        calcular.calcular_subtracao(n1,n2)

    if opçao==3:
        calcular.calcular_multiplicacao(n1,n2)

    if opçao==4:
        calcular.calcular_divisao(n1,n2)

    if opçao<0 or opçao>4:
        print("Número inválido. Tente novamente.")
        opçao=int(input("Digite uma opção para continuar: \n1- SOMA \n2-SUBTRAÇÃO \n3-MULTIPLICAÇÃO \n4-DIVISÃO \n0-SAIR"))
