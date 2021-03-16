## 2. Processing Chunks ##

import pandas as pd
import matplotlib.pyplot as plt

memory_footprints = []

moma = pd.read_csv("moma.csv", chunksize = 250)

for i in moma:
    mem = i.memory_usage(deep=True).sum() / (1024*1024)
    memory_footprints.append(mem)

plt.hist(memory_footprints)
plt.show()

## 3. Counting Across Chunks ##

num_rows = 0

moma_iter = pd.read_csv("moma.csv", chunksize=250)

for i in moma_iter:
    length = len(i)
    num_rows = num_rows+length
print(num_rows)

## 4. Batch Processing ##

lifespans = []
dtypes = {"ConstituentBeginDate": "float", "ConstituentEndDate":"float"}

iter_moma = pd.read_csv("moma.csv", chunksize = 250, dtype=dtypes)



for i in iter_moma:
    diff = i["ConstituentEndDate"] - i["ConstituentBeginDate"]
    lifespans.append(diff)
lifespans_dist = pd.concat(lifespans)

## 6. Counting Unique Values ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = []
for i in chunk_iter:
    val = i["Gender"].value_counts()
    overall_vc.append(val)
combined_vc = pd.concat(overall_vc)

## 7. Combining Chunks Using GroupBy ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
overall_vc = []
for i in chunk_iter:
    val = i["Gender"].value_counts()
    overall_vc.append(val)

combined_vc = pd.concat(overall_vc)
final_vc = combined_vc.groupby(combined_vc.index).sum()
print(final_vc)

## 8. Working With Intermediate Dataframes ##

chunk_iter = pd.read_csv("moma.csv", chunksize = 1000)
vals = []
for i in chunk_iter:
    val = i["Gender"].groupby(i["ExhibitionID"]).value_counts()
    vals.append(val)
overall = pd.concat(vals)
id_gender_counts = overall.groupby(overall.index).sum()