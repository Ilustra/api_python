 teste = {}
    lista=[]
    

    def pontoMedio(xki, xk):#função calcula o ponto médio xk+1 - xk / xk
        return abs((xki - xk) / xk) 

    def error(precisaoConstante, valor): #calcular error
        if valor < precisaoConstante:
            return True
        else:
            return False

    def ListaInteracoes(k, x):#insere as interações em uma lista
        teste['x{}'.format(k)]=x
        lista.insert(0, x)
        return teste

   