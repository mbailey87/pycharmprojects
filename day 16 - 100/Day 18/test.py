# from turtle import Turtle, Screen
import colorgram
import turtle as t
import random
timmy = t.Turtle()
timmy.shape('turtle')
timmy.color("coral", "green")
t.colormode(255)

# for i in range(10):
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)
#     timmy.pd()

# sides = 3

# def ran_num():
#     num = float(random.randint(1, 256))
#     return num
# while sides < 11:
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)
#     timmy.pencolor(random.choice(colors))
#     sides += 1

def ran_num():
    num = random.randint(0,255)
    return num

def ran_color():
    r = ran_num()
    g = ran_num()
    b = ran_num()
    ran_color = (r,g,b)
    return ran_color

# timmy.pensize(5)
colors = colorgram.extract("hirst.jpg", 20)
# movement = 25
# heading = [0, 90, 180,270,]
# for _ in range(200):
#     timmy.pencolor(ran_color())
#     timmy.setheading(random.choice(heading))
#     timmy.forward(movement)
#



color_list = []

for color in colors:
    color_list.append(color.rgb)
# angle = 0
timmy.speed('fast')
# while angle <= 360:
#     timmy.pencolor(ran_color())
#     timmy.circle(100)
#     angle += 10
#     timmy.seth(angle)
for _ in range(4):
    color_list.pop(0)
print(color_list)
timmy.penup()
x = -250
y = -250
timmy.setpos(x,y)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))

        timmy.forward(50)
    y += 50
    timmy.setpos(x, y)

timmy.hideturtle()
screen = t.Screen()
screen.exitonclick()

