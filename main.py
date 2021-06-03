#with open("weather_data.csv") as data_file:
 #   data = data_file.readlines()

#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

# pandas does the same thing as above in fewer lines
#this will print a table/list of temperatures in csv file
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

