capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

#nested lists

# travel_log = {
#     "France": ['Paris', "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#
# print(travel_log["France"][1])

nested_list = ["a", 'b', ['c', 'd']]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "Cities Visited": ['Paris', "Lille", "Dijon"],
    },
    "Germany":  {
        "num_times_visited": 7,
        "cities_visited": ["Stuttgart", "Berlin"],
    }
}

print(travel_log["Germany"]["cities_visited"][1])