## 1. Introduction ##

import numpy as np
x = np.array([
 [7., 9., 2., 2.],
 [3., 2., 6., 4.],
 [5., 6., 5., 7.]
])

ones = np.ones((3, 4))
x = x-ones

## 2. Broadcasting With a Single Value ##

x = np.array([3, 2, 4, 5])

r =  1/x

## 3. Broadcasting Mental Model ##

x = np.array([
    [4, 2, 1, 5],
    [6, 7, 3, 8]
])
y = np.array([
    [1],
    [2]
])

z = x+y
print(z)

## 4. Broadcasting Horizontally ##

x = np.array([
    [4, 2, 1, 5],
    [6, 7, 3, 8]
])

y = np.array(
    [1, 2, 3, 4]
)

z = x+y
print(z)

## 5. Broadcasting Vertically ##

x = np.array([
    [1],
    [2],
    [3]
])

y = np.array(
    [1, 2, 3]
)

z = x+y
print(z)

## 6. Broadcasting on Both ##

dice1 = np.array(
    [1, 2, 3, 4, 5, 6]
)

dice2 = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
dice_sums =  dice1+dice2
print(dice_sums)

## 7. Broadcasting Rules ##

x = np.array([1, 2, 3, 4])
y = np.array([
    [1], 
    [2], 
    [3], 
    [4]
])

shape_x = x.shape
shape_y = y.shape
print(shape_x)
print(shape_y)

shape_x_step1 = (1, 4)
shape_y_step1 = (4, 1)
shape_x_step2 = (4, 4)
shape_y_step2 = (4, 4)

error = False

## 8. Reshaping ##

lst = [i for i in range(1,7) ]
dice1 = np.array(lst)

dice2 = dice1.reshape(6,1)

dice_sums = dice1 + dice2

## 9. Compatible Shapes ##

cell_numbers = np.array([i for i in range(1, 37)])

numbering_by_row = cell_numbers.reshape(6,6)

numbering_by_col = cell_numbers.reshape(6,6,order="F")