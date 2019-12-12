    def CalcInteracao(x, precisao, interacao):
        k=0
        lista.insert(0, x)
        while True:
           # x = ln(2-x) # chama a função que calcula o valor
            x = Vx(4+ln(x))
            lista.insert(0, x) # insere o valor
            xk = pontoMedio(lista[0], lista[1])
            listaPonto.insert(0, xk)
            k +=1
            if (k >= interacao) or (error(precisao, xk)==True):
                break
        return listaPonto






                print('olá')
                while True: # repete até que seja encontrado o fim do ()
                    j=j+1# contador começa no parentese e vai até o final do mesmo
                    if dados["{}".format(x)].isalnum() == False:
                        if dados["{}".format(x)] == '-':
                            aux_resultado  = aux_resultado + (-1 * chute)
                                
                    if dados["{}".format(x)][j].isalpha() and dados["{}".format(x)][j] == 'x':
                        aux_resultado = aux_resultado + chute # vonverte a variavel x para o chute inicial
                        print('primeiro valor de x {}'.format(aux_resultado))
                            
                    if dados["{}".format(x)][j] == "+": # verifica se é soma
                        if dados["{}".format(x)][j+1].isdigit(): # verifica se o proximo após a soma é um digito 
                             aux_resultado = aux_resultado + int(dados["{}".format(x)][j+1])

                    if dados["{}".format(x)][j]=='-':
                        if dados["{}".format(x)][j+1].isdigit():
                            aux_resultado = aux_resultado + (-1 * int(dados["{}".format(x)][j+1])) # converte para valor negativo
                            print('converte para numero negativo {}'.format((-1 * int(dados["{}".format(x)][j+1]))))  

                    if dados["{}".format(x)][j] ==')':
                        return ln(aux_resultado) 
                        break  