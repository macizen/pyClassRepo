from turtle import *
import random

speed(0)

colors = ["lavender", "DarkOrchid", "BlueViolet", "DarkSlateBlue", "DarkMagenta"]

def draw_flower(x, y):
    penup()
    pensize(15)
    goto(x, (y - 800))
    pendown()
    pencolor("green")
    goto(x, y)
    pensize(5)
    random_petal_size = random.randint(2, 6)
    for i in range(5):
        c = colors[i % 5]
        pencolor(c)
        fillcolor(c)
        left(360/5)
        begin_fill()
        for j in range(3):
            circle((random_petal_size * 10) - j * 10)
        end_fill()

onscreenclick(draw_flower)

mainloop()