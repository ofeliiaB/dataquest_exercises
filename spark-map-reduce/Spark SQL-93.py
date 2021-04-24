## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable("census2010")
tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

query = "SELECT age FROM census2010;"

sqlCtx.sql(query).show()

## 4. Filtering ##

query = "SELECT males, females FROM census2010 WHERE age >5 AND age < 15;"

sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query = "SELECT males, females FROM census2010;"

sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

df_1980 = sqlCtx.read.json("census_1980.json")
df_1980.registerTempTable("census1980")

df_1990 = sqlCtx.read.json("census_1990.json")
df_1990.registerTempTable("census1990")

df_2000 = sqlCtx.read.json("census_2000.json")
df_2000.registerTempTable("census2000")

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = """
    SELECT c21.total, c20.total
    FROM census2000 as c20
    INNER JOIN census2010 as c21 ON c20.age = c21.age;
"""

sqlCtx.sql(query).show()

## 8. SQL Functions ##

query = """
    SELECT SUM(c21.total), SUM(c20.total), SUM(c19.total)
    FROM census2000 AS c20
    INNER JOIN census1990 c19 ON c19.age = c20.age
    INNER JOIN census2010 c21 ON c21.age = c20.age;
"""

sqlCtx.sql(query).show()