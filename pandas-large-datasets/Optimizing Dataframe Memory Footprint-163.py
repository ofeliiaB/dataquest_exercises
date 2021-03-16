## 2. Estimating Memory Consumption ##

import pandas as pd

moma = pd.read_csv("moma.csv")
moma.info()

## 3. How Pandas Represents Values in a Dataframe ##

print(moma._data)

## 5. Estimating The Memory Manually ##

moma.size

num_entries = moma.size

total_bytes = num_entries*8
total_megabytes = total_bytes / (2**20)

print(total_megabytes)

## 7. Memory Footprint of Non-numerical Data ##

obj_cols = moma.select_dtypes(include=["object"])
obj_cols_mem = obj_cols.memory_usage(deep= True)


obj_cols_sum = obj_cols_mem.sum()

obj_cols_sum = obj_cols_sum / (2**20)
print(obj_cols_sum)

## 9. Optimizing Integer Columns With Subtypes ##

def change_to_int(df, col_name):
    # Get the minimum and maximum values
    col_max = df[col_name].max()
    col_min = df[col_name].min()
    # Find the datatype
    for dtype_name in ['int8', 'int16', 'int32', 'int64']:
        # Check if this datatype can hold all values
        if col_max <  np.iinfo(dtype_name).max and col_min > np.iinfo(dtype_name).min:
            df[col_name] = df[col_name].astype(dtype_name)
            break

float_moma = moma.select_dtypes(include=["float64"])
float_moma.isnull().sum()

change_to_int(moma, "ExhibitionSortOrder")

## 10. Optimizing Float Columns With Subtypes ##

float_cols = moma.select_dtypes(include=['float']).columns

for col in float_cols:
    moma[col] = pd.to_numeric(moma[col], downcast="float")

## 12. Converting To DateTime ##

moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])

moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])

moma.memory_usage()

## 14. Converting to Categorical to Save Memory ##

object_cols = moma.select_dtypes(include=['object']).columns


for i in object_cols:
    length = len(moma[i].unique())
    size = moma[i].size
    if length < (size/2):
        moma[i] = moma[i].astype("category")
print(moma.info(memory_usage = "deep"))

## 15. Selecting Types While Reading the Data In ##

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']


moma = pd.read_csv("moma.csv", usecols = keep_cols, parse_dates=["ExhibitionBeginDate", "ExhibitionEndDate"])

moma.memory_usage(deep = True).sum() / (1024*1024)

