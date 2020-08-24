class ValidaIdade:

    def verifica_idade(self, nome, idade):
        if idade >= 18:
            print("Maior idade !")
        else:
            print("Menor idade !")


class MediaAlunos:
    def media_final(self,nota1, nota2, nota3):
        media_aluno=(nota1 + nota2 + nota3)/3
        if media_aluno>=7:
            print("Média: ", media_aluno, " | " , "Aprovado!")
        else:
            print("Média: ", media_aluno, " | ", "Reprovado :(")


qt_alunos=4
while qt_alunos!=-1:

    nome_aluno=input("Digite o nome do aluno: ")
    idade=int (input("Digite a idade do aluno: "))
    nota1=float(input("Digite a primeira nota do aluno: "))
    nota2=float(input("Digite a segunda nota do aluno: "))
    nota3=float(input("Digite a terceira nota do aluno: "))
    qt_alunos-=1

    ver_idade = ValidaIdade()
    ver_idade.verifica_idade(nome_aluno,idade)

    Media_Alunos=MediaAlunos()
    Media_Alunos.media_final(nota1,nota2,nota3)
