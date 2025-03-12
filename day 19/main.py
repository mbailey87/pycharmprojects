from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)

bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? enter a color:").lower()
# print(bet)
timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
jonny = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")
ronny = Turtle(shape="turtle")
bob = Turtle(shape="turtle")

turtles = [
    {
        "turtle": timmy,
        "position":0,
        "color": "coral"
    },{
        "turtle": tommy,
        "position":0,
        "color": "green"
    },{
        "turtle": jonny,
        "position":0,
        "color": "blue"
    },{
        "turtle": jimmy,
        "position":0,
        "color": "red"
    },{
        "turtle": ronny,
        "position":0,
        "color": "yellow"
    },{
        "turtle": bob,
        "position":0,
        "color": "black"
    },]

for turtle in turtles:
    turtle["turtle"].color(turtle["color"])

winner = ''
y = 0
x = -235
finished = False
for turtle in turtles:
    turtle["turtle"].penup()
    turtle["turtle"].goto(x, y)
    y += 20

while not finished:

    for turtle in turtles:

        ran_int = random.randint(10,20)
        turtle["turtle"].forward(ran_int)
        turtle["position"] += ran_int


        if turtle["position"] > 460:
            winner = turtle["color"]
            finished = True

if winner == bet:
    print("Congrats Your Turtle Won!")
else:
    print(f"Your turtle: {bet} lost the winner was {winner}")

screen.exitonclick()
