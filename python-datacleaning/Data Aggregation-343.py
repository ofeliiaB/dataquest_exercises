## 2. Introduction to the Data ##

import pandas as pd
happiness2015 = pd.read_csv("World_Happiness_2015.csv")

first_5 = happiness2015.iloc[0:5,:]

happiness2015.info()

## 3. Using Loops to Aggregate Data ##

happiness2015['Happiness Score'].plot(kind='bar', title='Happiness Scores', ylim=(0,10))

so_asia = happiness2015[happiness2015['Region'] == 'Southern Asia']
so_asia.plot(x='Country', y='Happiness Score', kind='barh', title='Southern Asia Happiness Scores', xlim=(0,10))

mean_happiness = {}

unique_reg = happiness2015["Region"].unique()

for i in unique_reg:
    region_group =  happiness2015[happiness2015["Region"] == i]
    mean = region_group["Happiness Score"].mean()
    mean_happiness[i] = mean
    

## 5. Creating GroupBy Objects ##

grouped = happiness2015.groupby("Region")

aus_nz = grouped.get_group("Australia and New Zealand")

## 6. Exploring GroupBy Objects ##

grouped = happiness2015.groupby('Region')

grouped.groups
north_america_indexes = []

for key, value in grouped.groups.items():
    if(key == "North America"):
        north_america_indexes = value
        
print(north_america_indexes)

north_america = happiness2015.iloc[[north_america_indexes[0], north_america_indexes[1]]]

na_group = grouped.get_group("North America")

equal = north_america == na_group

## 7. Common Aggregation Methods with Groupby ##

grouped = happiness2015.groupby('Region')

means = grouped.mean()

## 8. Aggregating Specific Columns with Groupby ##

grouped = happiness2015.groupby('Region')

happy_grouped = grouped["Happiness Score"]

happy_mean = happy_grouped.mean()

## 9. Introduction to the Agg() Method ##

import numpy as np
grouped = happiness2015.groupby('Region')
happy_grouped = grouped['Happiness Score']
def dif(group):
    return (group.max() - group.mean())

happy_mean_max = happy_grouped.agg([np.mean, np.max])

mean_max_dif = happy_grouped.agg(dif)

## 11. Aggregation with Pivot Tables ##

pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)

pv_happiness.plot(kind="barh", xlim=(0,10), title="Mean Happiness Scores by Region", legend=False)


world_mean_happiness = happiness2015["Happiness Score"].mean()

## 12. Aggregating Multiple Columns and Functions with Pivot Tables ##

group_obj = happiness2015.groupby("Region")
grouped = group_obj[["Happiness Score", "Family"]]

happy_family_stats = grouped.agg([np.min, np.max, np.mean])

pv_happy_family_stats = happiness2015.pivot_table(["Family", "Happiness Score"], "Region", margins=True, aggfunc=[np.min, np.max, np.mean])