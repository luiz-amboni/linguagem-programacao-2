class Validar:

    def valida_num(self, num):
        if num>0 and num%2==0:
            print("O número", num,"é positivo e par.")

        if num<0 and num%2==0:
            print("O número", num, "é negativo e par.")

        if num<0 and num%2!=0:
            print("O número", num, "é negativo e ímpar.")

        if num>0 and num%2!=0:
            print("O número", num, "é positivo e ímpar.")

determinar=Validar()
num=int(input("Digite um número: "))
determinar.valida_num(num)
