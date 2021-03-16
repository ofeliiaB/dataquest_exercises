## 1. Introduction ##

import pandas as pd

## 2. Read a CSV with Pandas ##

import pandas as pd

cars = pd.read_csv("cars.csv")

## 3. Dataframes ##

cars_shape = cars.shape

first_six_rows = cars.head(6)

last_four_rows = cars.tail(4)

## 4. Accessing Data With Indexes ##

cars_odd = cars.iloc[1::2, 0:3 ]

fifth_odd_car_name = cars_odd.iat[4,0]

last_four = cars_odd.tail(4)

print(last_four)

## 5. Accessing Data With Names ##

cars.set_index("Name", inplace=True)

weight_torino = cars.loc["Ford Torino", "Weight"]

## 6. Dataframe Indexes ##

honda_civic_hp = cars.loc["Honda Civic","Horsepower"]

print(honda_civic_hp)

cars.reset_index(inplace=True)

## 7. Delving Deeper Into Loc ##

numeric_data = cars.loc[:, "MPG":"Acceleration"]

numeric_data.head()

## 8. Selecting Columns ##

weights = cars["Weight"]

name_origin_0_and_3 = cars.loc[[0,3],["Name", "Origin"]]

## 9. Selecting Rows ##

car_100 = cars.iloc[99, :]

cars_2_to_10 = cars.iloc[1:10, :]

## 10. Index Locations and Label Locations ##

num_rows = cars.shape[0]

one_index = pd.Index([i for i in range(1, num_rows+1)])

cars.set_index(one_index, inplace=True)

car_100 =cars.loc[100]
cars_2_to_10 = cars.loc[2:10, :]