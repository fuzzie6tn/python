# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#        if row[1] != "temp":
#            temperature.append(row[1])
#     print(temperature)

# 3 lines vs 8 lines - see the difference between not using pandas and using panadas

#
# # print(data["temp"])
# data_dict = data.to_dict()
# print(f"Converted into dict: \n{data_dict}")
#
# data_list = data["temp"].to_list()
# print(f"Converted into list: \n{data_list}")
#
# # avg = sum(data_list)/len(data_list)   .mean()
# avg = data["temp"].max()
# print(f"Average temperature: {avg}")
import pandas

#Get data from row
data = pandas.read_csv("weather_data.csv")
# print(data[data.day] == "Monday")
print(data[data.temp == data.temp.max()])