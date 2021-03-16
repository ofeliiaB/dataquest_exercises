## 1. Introduction ##

import pandas as pd

cars = pd.read_csv("cars.csv")
num_rows = cars.shape[0]
new_index = pd.Index([i for i in range(1, num_rows+1)])
cars.set_index(new_index, inplace=True)

## 3. Arithmetic and Summary Statistics ##

max_weight = cars["Weight"].max()
min_weight = cars["Weight"].min()

weight_ratio = max_weight/min_weight

## 4. Value Counts ##

origin_counts = cars["Origin"].value_counts()

origin_counts_dict = origin_counts.to_dict()
print(origin_counts_dict)

## 5. Filtering Rows ##

european_cars = cars[cars["Origin"]=="Europe"]

print(european_cars.shape)

## 6. Logical Operators ##

non_us_cars = cars[cars["Origin"] !="US"]

low_mpg_horsepower = cars[(cars["MPG"]>0) & (cars["MPG"]<10) & (cars["Horsepower"]>=150)]

light_or_fast= cars[(cars["Weight"]<=2000) | (cars["Acceleration"] >=30)]

## 7. Masks with Column Selection ##

mask = (cars["MPG"]>0) & (cars["MPG"]<12) & (cars["Horsepower"]>=200)

name_and_origin = cars.loc[mask, ["Name", "Origin"]]

## 8. Adding Columns ##

PW_ratio = cars["Horsepower"]/cars["Weight"]

max_pw_ratio = PW_ratio.max()

cars["PW_ratio"] = PW_ratio

## 9. Column with Partial Data ##

mpg_l100_constant = 235.214583

mpg_non_zero = cars.loc[cars["MPG"]!=0, "MPG"]

L100 = mpg_l100_constant /mpg_non_zero

cars["L/100"] = L100