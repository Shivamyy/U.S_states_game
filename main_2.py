import pandas
data=pandas.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel=data[data["Primary Fur Color"]=="Gray"]
print(gray_squirrel)
print(len(gray_squirrel))
Black_squirrel=data[data["Primary Fur Color"]=="Black"]
cinnamon_squirrel=data[data["Primary Fur Color"]=="Cinnamon"]
print(len(Black_squirrel))
print(len(cinnamon_squirrel))

data_dict={
    "Fur color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [len(gray_squirrel), len(Black_squirrel), len(cinnamon_squirrel)]
}
new_created_data=pandas.DataFrame(data_dict)
print(new_created_data)
new_created_data.to_csv("new_created_csv_file.csv")

