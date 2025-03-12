# with open('weather_data.csv') as data_file:
#     data = data_file.read()
#     split_data = data.split('\n')
#     print(split_data)

# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     data_list = []
#     temps = []
#     for data_row in data:
#         data_list.append(data_row)
#     for row in data_list[1:]:
#         temps.append(int(row[1]))
#
#     print(temps)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data)
# # print(data['temp'])
#
# dic = data.to_dict()
#
# print(dic)
# print(dic['day'][0])
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # sum_total = sum(temp_list)
# # av = average(temp_list)
# # print(sum_total, av)
#
# mean = data['temp'].mean()
#
# max = data['temp'].max()
#
#
# print(mean, max)
#
# print(data.condition)
#
# # row
# print(data[data.day == "Monday"])
# print(data[data.temp == max])
#
# monday = data[data.day == "Monday"]
#
# temp_f = (monday.temp*(9/5)) + 32
#
# print(temp_f)

#create data frame
data_dic = {
    "students": ["Amy", 'James', 'Angela'],
    "scores": [76,56,65]
}

new_data = pandas.DataFrame(data_dic)

print(new_data)
new_data.to_csv("new_data.csv")