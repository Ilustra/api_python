from flask import Flask
from flask import request
import math
from flask import request
import json
from funcao2Grau import Funcao2Grau
        #math_express calcula o x da funcção pesquisar
app = Flask("wtf")

@app.route("/interativo", methods=["GET", "POST"])
def interativoLinear(): # 2x² + 3x + 5 = 
        
    def Vx(x):              #raiz
        return math.sqrt(x) 

    def E(x):
        return math.exp(x)

    def pontoMedio(xki, xk):#função calcula o ponto médio xk+1 - xk / xk
        return abs( (xki - xk) / xki   )


    def error(precisaoConstante, xki, xk): #calcular error
        if pontoMedio(xki, xk) < precisaoConstante:
            return True
        else:
            return False 

    def ln(x):   #funcao Ln
        return math.log(x)

    def calExpressao(dados, chute):
        aux_resultado = 0
        j = 0
        k = 1
        print(dados)
        if len(dados) < 2:
            return chute
        else:
            for i in range(len(dados)):
                j = j + 1
                k = k + 1
                if dados[i].isalnum() == False:
                    if dados[i] == '-':
                        if len(dados) >= j:
                            if dados[j] == 'x':
                                if len(dados) > k:
                                    if dados[k].isdigit():
                                        aux_resultado  = aux_resultado + ((-1 *  chute) * dados[k])
                                else: 
                                    aux_resultado = aux_resultado + ((-1 * chute))

                if dados[i].isdigit():
                    if len(dados) > j:
                        if dados[j]=='x':
                            aux_resultado = aux_resultado + (float(dados[i]) * chute  )
                    else: 
                        aux_resultado = aux_resultado + float(dados[i])

                if dados[i].isdigit():

                    if len(dados) > j:
                        if dados[j].isalnum() == False:

                            if dados[j] == '-':
                                aux_resultado = aux_resultado + (float(dados[i]))

                            
                if dados[i].isalpha():
                    if len(dados) > j and k <= len(dados):
                        #print('x({}) - {}.{}'.format(i, chute, dados[j]))
                        if dados[j].isdigit() :
                            aux_resultado = aux_resultado + (chute * float(dados[j]))      
  
            return aux_resultado
                                             
    def reqs():
        print(request.json)
    def sTring():
        lista=[]
        listaPontoMedio=[]
        dados = request.json
        listaJson=[]
        resultado = 0
        constante =0
        k=0
        xk = float(dados['1']) #chute
        lista.insert(0, xk)

        while True:

            for x in range(len(dados)):
                
                if x > 3:

                    if  dados["{}".format(x)].isdigit() == True: # apenas numeros
                        constante = int (dados["{}".format(x)])
           
                    elif dados["{}".format(x)].isalnum() == False and  dados["{}".format(x)][1].isdigit(): #numero negativo
                        if dados["{}".format(x)][0] == "-":
                            xk = constante + (-1* float(dados["{}".format(x)][1]))
                            print("const {}".format(constante))

                    if 'ln' in dados["{}".format(x)]: # ln(x) #||||||||||||||||||||||||||||||||||||||||||||||||
                        print('ln')
                        if dados['0']=='x' and len(dados['0']) < 2:
                            print( dados["{}".format(x)][3:-1])
                            print(calExpressao(  dados["{}".format(x)][3:-1], xk   ))
                            xk =   constante + ln(calExpressao(  dados["{}".format(x)][3:-1], xk   ))

                        else:
                            xk = Vx(  constante +  ln(calExpressao(  dados["{}".format(x)][3:-1], xk   ))       )
                    #-------------------------------------------------------------------------------------------            
                    elif 'e' in dados["{}".format(x)]: # ex ####################################################
                        if  len(dados["{}".format(x)][1:]) < 2: 
                            xk = constante + E(xk)                    
                        else:
                            if dados["{}".format(x)][0]=='-' and dados["{}".format(x)][1]=='e' and len(dados["{}".format(x)][1:]) < 3  :
                                xk = constante - E(calExpressao(dados["{}".format(x)][2:], xk))
                            elif '^' in dados["{}".format(x)]:
                                xk = constante - E(   (xk **  calExpressao( dados["{}".format(x)][2:], xk) )    )
                                print("xk")

                    elif 'x' in dados["{}".format(x)] and dados["{}".format(x)].isalnum(): # (x)
                        if dados['{}'.format(x)][0].isdigit():
                            xk = constante + (float(dados["{}".format(x)][0]) * xk)

            lista.insert(0, xk)
            #     
            listaPontoMedio.insert(0, pontoMedio(lista[0], lista[1]) )
            k=k+1

            if (    k >=  float(   dados['2'], )   ) or error(float(dados['3']), lista[0], lista[1]) ==True:
                break
        listaJson=(lista,listaPontoMedio)
       # lista.append({"PontoMedio":listaPontoMedio})    
        return json.dumps(listaJson)

               
            
    return sTring()

app.run(debug=True)
