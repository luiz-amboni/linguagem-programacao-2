class Atividade07():

    def input(self):
        listNum = []
        for i in range(10):
            num = float(input("Informe um numero"))
            listNum.append(num)

        listNum.sort(reverse=True)
        Atividade07().result(listNum)

    def calc(self, list):
        aux = 0
        for i in range(10):
            total = aux + list[i]
            aux = total

        print("Soma:", total)
        media = total / 10
        print("Media:", media)

    def result(self, list):

        print("Maior numero:", list[0])
        print("Menor numero:", list[9])
        Atividade07().calc(list)



validator = Atividade07()
validator.input()