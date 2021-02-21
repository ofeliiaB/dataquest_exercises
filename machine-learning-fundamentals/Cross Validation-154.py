## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

shuffled_index = np.random.permutation(dc_listings.index)

dc_listings = dc_listings.reindex(shuffled_index)

split_one = dc_listings.iloc[0:1862].copy()
split_two = dc_listings.iloc[1862:].copy()

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn_one = KNeighborsRegressor()
knn_one.fit(train_one[["accommodates"]], train_one["price"])

test_one["predicted_price"] = knn_one.predict(test_one[["accommodates"]])

mse_one = mean_squared_error(test_one["price"], test_one["predicted_price"])
iteration_one_rmse = math.sqrt(mse_one)


knn_two = KNeighborsRegressor()
knn_two.fit(train_two[["accommodates"]], train_two["price"])

test_two["predicted_price"] = knn_two.predict(test_two[["accommodates"]])
mse_two = mean_squared_error(test_two["price"], test_two["predicted_price"])
iteration_two_rmse = math.sqrt(mse_two)

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings.loc[(dc_listings.index[0:745], "fold")] = 1
dc_listings.loc[(dc_listings.index[745:1490], "fold")] = 2
dc_listings.loc[(dc_listings.index[1490:2234], "fold")] = 3
dc_listings.loc[(dc_listings.index[2234:2978], "fold")] = 4
dc_listings.loc[(dc_listings.index[2978:3723], "fold")] = 5

dc_listings["fold"].value_counts()

dc_listings["fold"].isnull().sum()

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
import numpy as np

knn = KNeighborsRegressor()
train_fold = dc_listings[dc_listings["fold"] != 1]
test_fold = dc_listings[dc_listings["fold"]==1].copy()
knn.fit(train_fold[["accommodates"]], train_fold["price"])
labels = knn.predict(test_fold[["accommodates"]])
mse = mean_squared_error(test_fold["price"], labels)
iteration_one_rmse = math.sqrt(mse)

## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
import math
fold_ids = [1,2,3,4,5]

def train_and_validate(df, folds):
    rmse_list = []
    for i in folds:
        knn = KNeighborsRegressor()
        train = df[df["fold"] != i]
        test = df[df["fold"] == i]
        knn.fit(train[["accommodates"]], train["price"])
        predictions = knn.predict(test[["accommodates"]])
        mse  = mean_squared_error(test["price"], predictions)
        rmse = math.sqrt(mse)
        rmse_list.append(rmse)        
    return rmse_list

rmses = train_and_validate(dc_listings, fold_ids)
avg_rmse = np.mean(rmses)
print(rmses)
print(avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold
import math
import numpy as np

kf = KFold(n_splits=5, shuffle=True, random_state=1)

knn = KNeighborsRegressor()
mses = cross_val_score(estimator=knn, X=dc_listings[["accommodates"]], y = dc_listings["price"], scoring="neg_mean_squared_error", cv = kf )

rmses = np.sqrt(np.absolute(mses))
avg_rmse = np.mean(rmses)