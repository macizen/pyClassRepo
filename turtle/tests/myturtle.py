import turtle
from turtle import *

title("my second* sketch")
bgcolor("black")
pensize(10)

def mac_dancing1():
    for i in range(100):
        mac.right(1)
        mac.forward(2)

def obama_dancing1():
    for i in range(100):
        obama.left(1)
        obama.forward(2)

def mac_dancing2():
    for i in range(100):
        mac.left(2)
        mac.forward(3)

def obama_dancing2():
    for i in range(100):
        obama.left(3)
        obama.forward(3)


mac = turtle.Turtle()
mac.shape("turtle")
mac.color("lavender")
mac.speed(1)

obama = turtle.Turtle()
obama.shape("turtle")
obama.color("tan")
obama.speed(1)

mac.penup()
mac.goto(-200, 200)
mac.pendown()

obama.penup()
obama.goto(-200, -200)
obama.pendown()

mac.forward(200)
obama.forward(200)

mac.right(90)
obama.left(90)

mac.forward(180)
obama.forward(180)

mac.write("hi obama")
obama.write("hi mac")

mac.right(180)
mac.forward(20)
mac.right(180)
mac.write("lets dance")

mac_dancing1()
obama_dancing1()
mac_dancing2()
obama_dancing2()


mainloop()