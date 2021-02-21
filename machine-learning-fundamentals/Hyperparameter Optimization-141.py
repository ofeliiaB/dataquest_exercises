## 1. Recap ##

import pandas as pd

train_df = pd.read_csv("dc_airbnb_train.csv") 
test_df = pd.read_csv("dc_airbnb_test.csv") 

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params= [1,2,3,4,5]
mse_values = []

for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = i, algorithm="brute")
    knn.fit(train_df[["accommodates", "bedrooms", "bathrooms", "number_of_reviews"]], train_df["price"])
    predictions = knn.predict(test_df[["accommodates", "bedrooms", "bathrooms", "number_of_reviews"]])
    mse_value = mean_squared_error(test_df["price"], predictions)
    mse_values.append(mse_value)

print(mse_values)

## 3. Expanding grid search ##

hyper_params = [x for x in range(1, 21)]
print(hyper_params)
mse_values = []
features = ["accommodates", "bedrooms", "bathrooms", "number_of_reviews"]

for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm="brute")
    knn.fit(train_df[features], train_df["price"])
    predictions = knn.predict(test_df[features])
    mse_value = mean_squared_error(test_df["price"], predictions)
    mse_values.append(mse_value)
print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
plt.scatter(hyper_params, mse_values)
plt.show()

## 5. Varying Hyperparameters ##

hyper_params = [x for x in range(1,21)]
mse_values = list()
features = train_df.columns.tolist()
features.remove('price')
print(features)

for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm="brute")
    knn.fit(train_df[features], train_df["price"])
    predictions = knn.predict(test_df[features])
    mse_value = mean_squared_error(test_df["price"], predictions)
    mse_values.append(mse_value)
plt.scatter(hyper_params, mse_values)
plt.show()

## 6. Practice the workflow ##

import sys
two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()

for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm="brute")
    knn.fit(train_df[two_features], train_df["price"])
    predictions = knn.predict(test_df[two_features])
    
    two_mse_value = mean_squared_error(test_df["price"], predictions)
    
    two_mse_values.append(two_mse_value)

param_with_error = zip(hyper_params, two_mse_values)
key_1, value_1  = min(param_with_error, key=lambda t: t[1])
two_hyp_mse[key_1] = value_1
        

for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm="brute")
    knn.fit(train_df[three_features], train_df["price"])
    predictions = knn.predict(test_df[three_features])
    three_mse_value = mean_squared_error(test_df["price"], predictions)
    three_mse_values.append(three_mse_value)

param_with_error_2 = zip(hyper_params, three_mse_values)
key_2, value_2  = min(param_with_error_2, key=lambda t: t[1])
three_hyp_mse[key_2] = value_2