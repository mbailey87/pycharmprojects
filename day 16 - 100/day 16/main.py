# import turtle
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral", "green")
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Bulbasaur", "Grass/Poison"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])

table.align = "l"

print(table)
