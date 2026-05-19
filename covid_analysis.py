from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, desc

spark = SparkSession.builder \
    .appName("COVID Analysis") \
    .getOrCreate()

# 1.Load your csv dataset
df = spark.read.csv(
    "owid-covid-data.csv",
    header=True,
    inferSchema=True
)

#2.Filter country specefic data
country_df = df.filter(col("location") == "China")

print("\nChina COVID Data")
country_df.select(
    "date",
    "total_cases",
    "total_deaths"
).show(20)

#3.Find totalcases and deaths
total_data = df.select(
    sum("new_cases").alias("Total_Cases"),
    sum("new_deaths").alias("Total_Deaths")
)

print("\nTotal cases and deaths")

total_data.show()


#4.Sort by highest cases
top_cases = df.groupBy("location").agg(
    sum("new_cases").alias("Total_Cases")
)
sorted_cases = top_cases.orderBy(
    desc("Total_Cases")
)
print("\nCountries Sorted by Highest Cases")
sorted_cases.show(15, truncate=False)



