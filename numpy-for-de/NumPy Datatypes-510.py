## 1. Introduction ##

import numpy as np
x = np.array([1, 2, 3, 4])

x[0] = 5.5
print(x[0])

## 2. Fixed NumPy Datatypes ##

values = [1, 2, 3, 4]

x = np.array(values, dtype="float64")

x[0] = 5.5
print(x[0])

## 3. Finding the Datatype ##

import numpy as np

boolean_list = [True, False, True, False]
integer_list = [6, -5, -9, 10]
float_list   = [0.5, 10.74, 65.5, 0.2]

boolean_array = np.array(boolean_list, dtype= "bool_")
print(boolean_array.dtype)

float_array = np.array(float_list, dtype="float32")
print(float_array.dtype)

integer_array = np.array(integer_list)
print(integer_array.dtype)

## 4. Ndarray From Mixed Lists ##

import numpy as np
values = [3.14, 6.42, 5.0, 0.5]

x = np.array(values, dtype="int64")

print(x)

## 5. Fixed-Length Bit Representations ##

value_list = [-127, -57, -6, 0, 9, 42, 125]

value_array = np.array(value_list, dtype=np.int8)

## 6. Memory Consumption ##

x = np.array([-127, -57, -6, 0, 9, 42, 125], dtype=np.int8)

print(x-2)

print(x+3)

## 9. Calculating Memory Requirements ##

num_values = 10**9 *8

num_bits = 64*num_values

gb = num_bits / (8 *10**9)
print(gb)