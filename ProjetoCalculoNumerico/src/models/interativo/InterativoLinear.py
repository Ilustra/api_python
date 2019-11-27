#transforma em um List
def convertLista(listaSting):
    lista=[]
    for aux in listaSting:
        lista.append(aux)
    return lista
#converte string em numero e substitui o valor de chute
def convertString(lista):
    listaint = []
    count = 0
    while count < len(lista):
        if lista[count].isalnum() == False:
            listaint.append(lista[count])
        elif lista[count].isdigit() == True:
            if count-1 < 0:
                listaint.append(int(lista[count]))
            elif (lista[count-1].isalpha()==False):
                listaint.append(int(lista[count]))
            elif lista[count].isalpha() == True:
                listaint.append(lista[count])
                if count+1 < len(lista): 
                    if (lista[count+1].isdigit() ) == True:
                        for x in range(int(lista[count+1])):
                            listaint.append('*')         
            count=count+1
    return listaint