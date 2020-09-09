

def lista_trocada(list):
    lista=[]
    metade=len(lista)/2
    invertida=lista[metade:] + lista[:metade]
    print ("Lista com as metades trocadas: ", invertida)
