import turtle
import random

turtle.title('generative chartes bleu rouge')
t = turtle.Turtle()
turtle.tracer(0)
t.speed(0)
t.color("#121511")
t.pensize(5)

screen = turtle.Screen()

screen_width = screen.window_width()
screen_height = screen.window_height()

left_x = -screen_width / 2 - 5
top_y = screen_height / 2

# i put repeated colors in here to "weight" how often each one will be drawn
colors = ["#D23020", "#D23020", "#D23020","#D23020", "#D23020", "#D23020", "#3272D3", "#3272D3", "#3272D3", "#3272D3", "#4A9076"]

t.penup()
t.goto(left_x, top_y)
t.pendown()

def draw_square():
    for _ in range(4):
        t.forward(screen_width / 30)
        t.right(90)

square_size = screen_width / 30


for y in range(30):
    t.penup()
    t.goto(left_x, top_y - y * square_size)
    t.pendown()
    for x in range(30):
        t.begin_fill()
        t.fillcolor(colors[random.randint(0, 10)])
        draw_square()
        t.forward(square_size)
        t.end_fill()

t.hideturtle()

turtle.update()

turtle.mainloop()