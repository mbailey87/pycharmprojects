import pandas



data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

# for color in colors:
#     if color == "Gray":
#         gray += 1
#     if color == "Cinnamon":
#         red += 1
#     if color == "Black":
#         black += 1
#
#
# print(gray, red, black)

squirrel_count = {
    "fur_color": ['gray', 'red', 'black'],
    'count': [gray,red,black]
}
new_data = pandas.DataFrame(squirrel_count)

print(new_data)
new_data.to_csv("color_count.csv")