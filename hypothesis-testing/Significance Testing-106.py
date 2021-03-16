## 3. Statistical Significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

## 4. Test Statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation Test ##

mean_difference = 2.52
print(all_values)

mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        random_value = np.random.rand()
        if(random_value >= 0.5):
            group_a.append(value)
        else:
            group_b.append(value)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()
        

## 7. Dictionary Representation of a Distribution ##

sampling_distribution = {}

for mean_difference in mean_differences:
    if(sampling_distribution.get(mean_difference, False)):
        val = sampling_distribution.get(mean_difference)
        val = val+1
        sampling_distribution[mean_difference] = val
    else:
        sampling_distribution[mean_difference] = 1

## 8. P Value ##

frequencies = []

for key in sampling_distribution.keys():
    if key >= 2.52:
        frequencies.append(key)

sum_freq = np.sum(frequencies)
p_value = sum_freq/1000