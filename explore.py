import pandas as pd

# Exercise 1: Load data
df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2: Filter by region
south = df[df["region"] == "South"]

print(len(south))
print(south.head())

# Exercise 3: Top 5 by revenue
print(df.sort_values("revenue", ascending=False).head(5))

# Exercise 4: Two-condition filter
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print(len(big_south))
print(big_south.head())

# Exercise 5: A new column
df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print(df["per_unit"].mean())

# Exercise 6: Unique values
print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 6: Unique values
print(df["region"].unique())
print(df["region"].value_counts())

# Exercise 7: Select columns
subset = df[["region", "product", "revenue"]]

print(subset.shape)

# Exercise 8: Save
df.to_csv("data/explored.csv", index=False)

# Self-Assessment

# 1. A boolean filter selects rows based on a condition.
# Rows that meet the condition are kept.

# 2. df["revenue"] returns a Series, while
# df[["revenue"]] returns a DataFrame. This matters
# when an operation requires a two-dimensional table.

# 3. Pandas allows me to automate repetitive data
# analysis tasks instead of performing them manually
# in Excel.