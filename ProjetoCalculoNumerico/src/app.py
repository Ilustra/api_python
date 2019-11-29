from flask import Flask
from flask import request
import math
import json
from funcao2Grau import Funcao2Grau

app = Flask("wtf")

@app.route("/interativo", methods=["GET", "POST"])
def interativoLinear(): # 2x² + 3x + 5 = 
    lista=[]
    listaPonto=[]
    def pontoMedio(xki, xk):#função calcula o ponto médio xk+1 - xk / xk
        return abs((xki - xk) / xk)

    def error(precisaoConstante, valor): #calcular error
        if valor < precisaoConstante:
            return True
        else:
            return False 
# V4+ln(x)=0
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

    def ln(x):
        return math.log(x)

    def Vx(x):              #raiz
        return math.sqrt(x) 

    return format(CalcInteracao(1, 0.01, 250))

app.run(debug=True)
