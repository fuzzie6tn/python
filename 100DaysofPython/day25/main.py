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

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
