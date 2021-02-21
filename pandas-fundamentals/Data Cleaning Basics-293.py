## 1. Reading CSV Files with Encodings ##

laptops = pandas.read_csv("laptops.csv", encoding="Latin-1")
laptops.info()

## 2. Cleaning Column Names ##

new_columns = []

for column in laptops.columns:
    column = column.strip()
    new_columns.append(column)

laptops.columns = new_columns

## 3. Cleaning Column Names Continued ##

import pandas as pd
laptops = pd.read_csv('laptops.csv', encoding='Latin-1')

def clean_extra(value):
    value = value.strip()
    value = value.replace("Operating System", "os")
    value = value.replace(" ", "_")
    value = value.replace("(", "")
    value = value.replace(")", "")
    value = value.lower()
    return value

columns_modified = []

for i in laptops.columns:
    i = clean_extra(i)
    columns_modified.append(i)
    
laptops.columns = columns_modified
    

## 4. Converting String Columns to Numeric ##

unique_ram = laptops["ram"].unique()

## 5. Removing Non-Digit Characters ##

print(unique_ram)

laptops["ram"] = laptops["ram"].str.replace("GB", "")
unique_ram = laptops["ram"].unique()

## 6. Converting Columns to Numeric Dtypes ##

laptops["ram"] = laptops["ram"].str.replace('GB','')

laptops["ram"] = laptops["ram"].astype(int)


dtypes = laptops.dtypes

## 7. Renaming Columns ##

laptops["ram"] = laptops["ram"].str.replace('GB','').astype(int)

laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)

ram_gb_desc = laptops["ram_gb"].describe()

## 8. Extracting Values from Strings ##

laptops["gpu_manufacturer"]= laptops["gpu"].str.split().str[0]
laptops["cpu_manufacturer"] = laptops["cpu"].str.split().str[0]

cpu_manufacturer_counts = cpu_manufacturer.value_counts()





## 9. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

## 10. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna(axis=0)
laptops_no_null_cols = laptops.dropna(axis=1)

## 11. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"


filtered = laptops["os"] == "No OS"
laptops.loc[filtered, "os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()

## 12. Challenge: Clean a String Column ##

def clean_weight(value):
    value = value.replace("kg", "")
    value = value.replace("kgs", "")
    value = value.replace("s", "")
    return value
    
    
weights_modified = []

for w in laptops["weight"]:
    w = clean_weight(w)
    weights_modified.append(w)
    
laptops["weight"] = weights_modified

laptops["weight"] = laptops["weight"].astype(float)


laptops.rename({"weight":"weight_kg"}, axis =1, inplace=True)




laptops.to_csv("laptops_cleaned.csv", index=False)
    
   