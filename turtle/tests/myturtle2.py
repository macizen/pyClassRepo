from turtle import *
import random

title('my third sketch')
shape('turtle')
speed(0)
fillcolor("lavender")

count = 8
angle = 360 / count
size = 100

colors = ["lavender", "DarkOrchid", "BlueViolet", "DarkSlateBlue", "DarkMagenta", "DeepPink4" ]

begin_fill()
for i in range(36):
    # c = color[i % 3]
    c = random.choice(colors)
    fillcolor(c)
    pencolor(c)
    left(10)
    begin_fill()
    for j in range(6):
        left(60)
        forward(100) 
    end_fill()



# my cool flower
# pencolor("lavender")
# begin_fill()
# for i in range(5):
#     left(360 / 5)
#     for j in range(count):
#         circle((size - 10) + j * 8)
# end_fill()

# pencolor("DarkOrchid1")
# pensize(1)
# for i in range(count):
#     left(angle)
#     for j in range(count):
#         circle(size - j * 10)

# pencolor("yellow")
# pensize(3)
# fillcolor("yellow")
# begin_fill()
# for i in range(3):
#     left(360 / 3)
#     circle(size - 80)
# end_fill()
        

# my cool thing
# begin_fill()
# for i in range(count):
#     left(angle)
#     circle(size - i * size / (size / 2))
#     this_color = 
# end_fill()

mainloop()