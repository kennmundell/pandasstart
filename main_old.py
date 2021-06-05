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
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

#average = sum(temp_list) / len(temp_list)
#print(average)

# code above can be simplified by below:
print(data["temp"].mean())
print(data["temp"].max())

#Get data in columns
print(data["condition"])
print(data.day)   # to print days column = dont need square brackets using pandas

#Get data in row
print(data[data.day == "Monday"])

#Print row with highest temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#To covert temp
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_new = pandas.DataFrame(data_dict)
print(data_new)
# to create new csv
data_new.to_csv("new_data.csv")
