## 1. Introduction ##

import numpy as np
table = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

col = table[:, 1]
row = table[2, :]
center = table[1:3, 1:4]

## 2. Adding ndarrays ##

def add_list_values(list1, list2):
    new_list = []
    for i in range(len(list1)):
        element = list1[i] + list2[i]
        new_list.append(element)
    return new_list

## 3. Comparing Ndarrays to Lists ##

import time
import random
import numpy as np
random.seed(0)

# Generate test lists
list1 = [random.randint(0, 1000) for _ in range(100000)]
list2 = [random.randint(0, 1000) for _ in range(100000)]

# Measure the execution time of adding lists
start = time.time()
add_list_values(list1, list2)
end = time.time()
time_list = end - start

x1 = np.array(list1)
x2 = np.array(list2)
start_2 = time.time()
x3 = x1+x2
end_2 = time.time()
time_array = end_2-start_2
ratio = time_list/time_array

## 5. Arithmetic Operations ##

people_data = np.array([
    [27, 67, 1.65],
    [35, 81, 1.84],
    [29, 55, 1.60],
    [41, 73, 1.79]
])

w = people_data[:,1]
h = people_data[:, 2]
BMI = w / (h*h)

## 6. Arithmetic in Higher Dimensions ##

scores = np.array([
    [46, 74, 52, 81],
    [75, 45, 67, 53],
    [67, 80, 73, 63],
    [59, 94, 43, 78]
])

scores_day1 = scores[:,0:2]
scores_day2 = scores[:,2:4]
shape1 = scores_day1.shape
shape2 = scores_day2.shape
print(shape1)
print(shape2)
total_scores = scores_day1+scores_day2

## 7. Minimum and Maximum ##

total_scores = np.array([
 [ 98, 155],
 [142,  98],
 [140, 143],
 [102, 172]
])

scores_game1 = total_scores[:,0]
scores_game2 = total_scores[:,1]
min_game1 = scores_game1.min()
max_game1 = scores_game1.max()
min_game2 = scores_game2.min()
max_game2 = scores_game2.max()

## 8. The Axis Parameter ##

total_scores = np.array([
 [ 98, 155],
 [142,  98],
 [140, 143],
 [102, 172]
])

max_game_scores = total_scores.max(axis=0)
min_game_scores = total_scores.min(axis=0)
max_people_scores = total_scores.max(axis=1)
min_people_scores = total_scores.min(axis=1)

## 9. Sum ##

total_scores = np.array([
 [ 98, 155],
 [142,  98],
 [140, 143],
 [102, 172]
])

total_people_score = total_scores.sum(axis=1)
max_score = total_people_score.max()