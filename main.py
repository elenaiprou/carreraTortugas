import turtle


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
     
         
     
     
     
     
     
if __name__ == '__main__':    
    circuito = Circuito(640, 480)