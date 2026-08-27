import pandas as pd

# Load dataset into a DataFrame
df = pd.read_csv("marks1.csv")      # Replace with your file name

# Display first and last few rows
print("First 5 rows:\n")
print(df.head())

print("\nLast 5 rows:\n")
print(df.tail())

# Check data types and general information
print("\nData Information:")
df.info()

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Handle missing values (only numeric columns)
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Create a new column (Total Marks)
df["Total"] = (
    df["Maths"] +
    df["Science"] +
    df["physics"] +
    df["English"] +
    df["Social"]
)

# Create another new column (Average Marks)
df["Average"] = df["Total"] / 5

# Create a Series and perform operations
series = df["Maths"]
print("\nMaths Marks + 10:")
print(series + 10)

# Filter rows based on conditions
filtered_df = df[(df["Maths"] > 80) & (df["Science"] > 80)]
print("\nStudents scoring above 80 in Maths and Science:")
print(filtered_df)

# Grouping and aggregation
grouped = df.groupby("Science")["Maths"].mean()
print("\nAverage Maths Marks grouped by Science Marks:")
print(grouped)

# Sorting based on Total Marks
df_sorted = df.sort_values(by="Total", ascending=False)
print("\nSorted by Total Marks:")
print(df_sorted)

# Boolean masking (Students above median total marks)
masked_df = df[df["Total"] > df["Total"].median()]
print("\nStudents Above Median Total:")
print(masked_df)

# Remove duplicates and missing values
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Create a new DataFrame with selected columns
subset_df = df[["Roll. No.", "Name", "Total", "Average"]]

# Save the new DataFrame to a CSV file
subset_df.to_csv("filtered_data.csv", index=False)

# Compute summary statistics
print("\nSummary Calculations")
print("Total Marks Sum:", df["Total"].sum())
print("Average Total Marks:", df["Total"].mean())
print("Standard Deviation:", df["Total"].std())
