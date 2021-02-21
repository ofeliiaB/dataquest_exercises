## 2. Introduction to the data ##

import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings.iloc[0:])

## 4. Euclidean distance ##

import numpy as np

first_living_space_value = dc_listings.iloc[0]['accommodates']

first_distance = np.abs(first_living_space_value-3)

## 5. Calculate distance for all observations ##

import numpy as np

def difference(n):
    return np.abs(n-3)

distance = dc_listings['accommodates'].apply(difference)

dc_listings["distance"] = distance
print(dc_listings["distance"].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)

dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

dc_listings = dc_listings.sort_values('distance')

print(dc_listings.iloc[0:10]['price'])

## 7. Average price ##

dc_listings["price"] = dc_listings["price"].str.replace(",", "").str.replace("$", "")

dc_listings["price"] = dc_listings["price"].astype(float)

mean_price = dc_listings["price"][0:5].mean()

print(mean_price)

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    temp_df["distance"]= np.abs(temp_df["accommodates"] - new_listing)
    temp_df = temp_df.sort_values("distance")
    first_5 = temp_df.iloc[0:5]["price"]
    mean_5 = first_5.mean()
    return(mean_5)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)