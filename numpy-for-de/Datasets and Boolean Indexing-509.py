## 1. Introduction ##

import numpy as np
x = np.array([
    [44, 70, 49,  2, 19],
    [62, 68, 64, 18, 12],
    [91, 90, 63, 98, 69],
    [22,  9, 98, 16, 58],
    [47, 92, 39,  8, 19],
    [ 1, 41,  3, 15, 71],
    [92, 18, 37, 42,  5]
])

first_four = x[0:4, :]

last_column = x[:, -1]

## 2. Loading CSV Data ##

import numpy as np

sars = np.genfromtxt("sars.csv", delimiter = ",")

first_five = sars[0:5, :]

## 3. Removing Invalid Data ##

np.set_printoptions(suppress=True)

sars = sars[1:, 1:]
print(sars[:5, :])

## 4. NumPy Limitations ##

total = sars[:, 2]
max_dead = total.max()

## 5. Comparing Column Values ##

female = sars[:, 0]

male = sars[:, 1]

more_female_deaths = female > male

equal_deaths = female==male

num_more_female = more_female_deaths.sum()
num_equal = equal_deaths.sum()
num_more_male = female.size - (num_equal + num_more_female)

## 6. Comparing With a Single Value ##

any_less_1 = (sars[:,4]<1).any()

all_less_50 = (sars[:,4] <=50).all()

## 7. Logical Connectors ##

deaths = sars[:,3]
fatality_ratio = sars[:, 4]

death_gt_100_ratio_lt_10 = (deaths >=100)&(fatality_ratio <=10)

count = death_gt_100_ratio_lt_10.sum()

## 8. Boolean Masks ##

mask = fatality_ratio >=10
num_deaths = deaths[mask]

## 9. Boolean Masks in Higher Dimensions ##

mask_zeros = sars == 0

zeros = sars[mask_zeros]

num_zeros = len(zeros)

## 10. 1D Mask on 2D Array ##

non_zero_deaths = sars[:,3] !=0
sars_subtable = sars[non_zero_deaths, 2:]