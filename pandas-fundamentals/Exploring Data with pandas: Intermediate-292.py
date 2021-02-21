## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500.loc[:,["rank", "revenues", "revenue_change"]].head(5)

## 2. Reading CSV files with pandas ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500.iloc[0:3]
first_seventh_row_slice = f500.iloc[[0,6], 0:5]

## 5. Using pandas methods to create boolean masks ##

filter_val = f500["previous_rank"].isnull()
null_values = f500[filter_val]
null_previous_rank = null_values.loc[:,["company", "rank", "previous_rank"]]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]

top5_null_prev_rank = null_previous_rank.iloc[0:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
f500["rank_change"] = rank_change

## 8. Using Boolean Operators ##

large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500.loc[combined, :]

## 9. Using Boolean Operators Continued ##

brazil_venezuela = f500.loc[(f500["country"] == "Brazil") | (f500["country"] == "Venezuela"), :]

not_usa  = f500["country"] != "USA"

tech = f500["sector"] == "Technology"
combined = not_usa & tech

tech_outside_usa = f500.loc[combined, :].head(5)

## 10. Sorting Values ##

japan_filter = f500["country"] == "Japan"
selected_rows = f500[japan_filter]

sorted_rows = selected_rows.sort_values("employees", ascending=False)

top = sorted_rows.iloc[0]

top_japanese_employer = top["company"]

## 11. Using Loops with pandas ##

top_employer_by_country  = {}

countries = f500["country"].unique()


for c in countries:
    selected_rows = f500[f500["country"]==c]
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    first_row = sorted_rows.iloc[0,:]
    company_name = first_row["company"]
    top_employer_by_country[c] = company_name 
    
    
    

## 12. Challenge: Calculating Return on Assets by Country ##

profit = f500["profits"]
assets = f500["assets"]
roa = profit / assets
f500["roa"] = roa

top_roa_by_sector = {}
sectors = f500["sector"].unique()

for sector in sectors:
    sector_filter = f500["sector"] == sector
    filtered = f500[sector_filter]
    roa = filtered.sort_values("roa", ascending=False)
    highest_roa = roa.iloc[0]
    company_name = highest_roa["company"]
    top_roa_by_sector[sector] = company_name