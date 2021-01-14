#Gennert lensment
#14.01.2021
#Turtle töö


#Kujund 16
import turtle as k
import turtle
def kuju16():

    aken = k.Screen()
    aken.setup(1000,500)
    aken.title("Turtle töö")
    
    
    for i in range(5):
        
        k.lt(90)
        k.fd(100)
        k.color("green")
        k.rt(30)
        k.fd(100)
        k.rt(120)
        k.fd(100)
        k.rt(120)
        k.color("black")
        k.fd(100)
        k.lt(180)
        k.fd(100)
        k.rt(90)
        k.fd(100)
        k.rt(90)
        k.fd(25)
        k.rt(90)
        k.color("red")
        k.fd(50)
        k.lt(90)
        k.fd(50)
        k.lt(90)
        k.fd(50)
        k.color("black")
        k.rt(90)
        k.fd(25)
        k.lt(180)
        k.fd(75)
        k.penup()
        k.fd(50)
        k.pendown()



#Kujund 5
import turtle as k
def kuju5():
    
    aken = k.Screen()
    aken.setup(600,600)
    aken.title("Turtle töö")
    
    for i in range(6):
        k.fd(100)
        k.lt(120)
        k.fd(100)
        k.lt(120)
        k.fd(100)
        k.lt(180)
kuju16()
#kuju5()