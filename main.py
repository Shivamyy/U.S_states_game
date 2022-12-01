# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         # print(row)   # print the data of the days row by row
#         # print(row[1]) 
#         if row[1] != "temp":  # list ko temp vanne title lai xodera aru sabai print garxa
#             temperature.append(int(row[1]))  # 
            
#     print(temperature)
        

import pandas
data=pandas.read_csv("weather_data.csv")  # print the data of "weather_data" file  in tabulated form
# print(data)
# print(data["temp"])  # print the datas only in the "temp" column in the tabulated form
# print(data.temp)   # this is similar to (data["temp"])


''' The two primary data structures of pandas,
Series (1-dimensional) or (single column) and DataFrame (2-dimensional), '''
# import pandas
# data=pandas.read_csv("weather_data.csv") 
# print(type(data))  # type of (data) is Dataframe
# print(type(data["temp"]))   # type of (data["temp"]) is Series

# data_dict= data.to_dict()
# print(data_dict)  # convert each column of the above table into dictionary
# temp_list=(data["temp"]).to_list()  # convert the "temp" column into list
# print(temp_list)
# average_temp=(sum(temp_list))/len(temp_list)
# print(average_temp)

# print(data["temp"].mean())  # this line also print the average of the temp column

# print(data["temp"].max())  # print the maximum value of the "temp" column

# print(data["temp"].min())   # print the minimum value of the "temp" column

# print(data[data.day=="Monday"])  # this print the row that contain Monday's details

# print(data[data.temp==data.temp.max()])  # print the row that has the maximum temperature
# print(data[data.temp==data.temp.min()])  # print the row that has the minimun temperature

monday=data[data.day=="Monday"]
# print(monday.condition)  # this print the condition of monday

# print(monday.temp)  # this print the temperature of monday
temperature_f=  1.8 * int(monday.temp) + 32
print(temperature_f) 


####################
# Create dataframe from scratch
data_dict={
    "students" : ["shivam", "hari", "gopal", "ram"],
    "scores" : [90, 67, 78, 23]
}
created_data=pandas.DataFrame(data_dict)  # create the above data_dict's data to tabulated form
print(created_data)
created_data.to_csv("new_data.csv")  # create new_data csv file (convert created_data into csv file)
