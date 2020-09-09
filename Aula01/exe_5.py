class Validar:

    def valida_num(self, num):
        if num >= 0:
            print('+{} positivo'.format(num))
        else:
            print('-{} negativo'.format(num))


validar = Validar()
num = int(input("Digite um numero: "))

validar.valida_num(num)
