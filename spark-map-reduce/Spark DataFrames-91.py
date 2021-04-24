## 1. The Spark DataFrame: An Introduction ##

with open("census_2010.json", "r") as f:
    for i in range(0,4):
        print(f.readline())
        

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show(5)

## 5. Row Objects ##

first_five = df.head(5)

for i in first_five:
    print(i.age)

## 6. Selecting Columns ##

df[['age']].show()

s = df.select('age', 'males', 'females')
s.show()

## 7. Filtering Rows ##

five_plus = df[df["age"] > 5]
five_plus.show()

## 8. Using Column Comparisons as Filters ##

r = df[df["females"] < df["males"]]
r.show(20)

## 9. Converting Spark DataFrames to pandas DataFrames ##

pandas_df = df.toPandas()
pandas_df["total"].hist()