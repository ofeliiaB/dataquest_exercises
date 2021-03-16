## 2. Calculating Differences ##

female_diff = (10771 - 16280.5) / 16280.5

male_diff = (21790- 16280.5) / 16280.5

## 3. Updating the Formula ##

female_diff = (10771 - 16280.5)**2/ 16280.5

male_diff = (21790- 16280.5)**2/ 16280.5

gender_chisq = female_diff + male_diff

## 4. Generating a Distribution ##

from numpy.random import random
import matplotlib.pyplot as plt
chi_squared_values = []
for i in range(1000):
    seq = random((32561,))
    print(seq)
    seq[seq < 0.5] = 0
    seq[seq >= 0.5] = 1
    male_count = len(seq[seq == 0])
    female_count = len(seq[seq == 1])
    male_diff = (male_count-16280.5)**2 / 16280.5
    female_diff = (female_count-16280.5)**2 / 16280.5
    chi_squared = male_diff+female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)


    
    

## 6. Smaller Samples ##

female_diff = (107.71 - 162.805)**2/162.805
male_diff = (217.90 - 162.805)**2/162.805
gender_chisq = female_diff + male_diff

## 7. Sampling Distribution Equality ##

chi_squared_values = []
from numpy.random import random
from matplotlib import pyplot as plt

for i in range(1000):
    sequence = random((300,))
    sequence[sequence < 0.5] = 0
    sequence[sequence >= 0.5] = 1
    male_count = len(sequence[sequence ==0])
    female_count = len(sequence[sequence ==1])
    male_diff = (male_count - 150)**2/150
    female_diff = (female_count - 150)**2/150
    chi_squared = male_diff+female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)

## 9. Increasing Degrees of Freedom ##

white_dif = (27816-26146.5)**2 / 26146.5
black_dif = (3124-3939.9)**2 / 3939.9
asian_dif = (1039-944.3)**2 / 944.3
indian_dif = (311-260.5)**2 / 260.5
other_dif = (271-1269.8)**2 / 1269.8

print(all_list)

all_list = [white_dif, black_dif, asian_dif, indian_dif, other_dif]
race_chisq = sum(all_list)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed  = [27816, 3124, 1039, 311, 271, 32561]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8, 32561]

chisquare_value, race_pvalue = chisquare(observed, expected)