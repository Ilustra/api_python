class Funcao2Grau:
# ax² + bx + c = 0
    def __init__(self, initA, initB, initC, initX):
        self.a = initA
        self.b = initB
        self.c = initC
        self.x = initX

    def getaX2(self):
        return self.a

    def getBx(self):
        return self.b

    def getC(self):
        return self.c

    def getX(self):
        return self.x
                
    def CalcularFuncao(self): # ax² + bx + c = 0
        v = self.a**2
        y = self.b*self.x
        return "resultado {}".format(v + y + self.c)

    def isolarRaiz(self):
        if self.b < 0: 
            self.b = self.b * (-1) 
        if self.c <0: 
            self.c = self.c * (-1)
        return "resultado {}".format(self.b)


    def distanceFromOrigin(self):
        resultado = self.a + self.b + self.c
        return "resultado {}".format(resultado)



        