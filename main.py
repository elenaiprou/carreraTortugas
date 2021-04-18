import turtle
import random #modulo para general numeros aletariros


class Circuito():
    corredores = [] #lista
    __posStartY = (-30, -10, 10, 30) #tupla
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):     
        self.__screen = turtle.Screen() #poner dos barras bajas hace que el modulo sea privado. para que el usuario no lo toque
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()
       
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup() #metodo de "turtle" que levanta el boli, y no pinta
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
                        
            self.corredores.append(new_turtle)     
     
         
    def competir(self): #simular carrera, se utiliza un bucle while
        
        winner = False
        
        while not winner:
            for tortuga in self.corredores:
                avance = random.randint(1, 16)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    winner = True
                    print("la tortuga de color {} ha ganado".format(tortuga.color()[0]))
               
          
if __name__ == '__main__':    
    circuito = Circuito(640, 480)
    circuito.competir()