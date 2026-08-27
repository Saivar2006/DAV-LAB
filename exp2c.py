import pandas as pd

# Read data
text_df = pd.read_csv("Googledata.csv")
excel_df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Read data from a web link
web_df = pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

# Display data
print(text_df.head())
print("\n", excel_df.head())
print("\n", web_df.head())

# Handle missing values
text_df.ffill(inplace=True)
excel_df.bfill(inplace=True)
web_df.dropna(inplace=True)

# Save processed data
text_df.to_csv("processed_text.csv", index=False)
excel_df.to_excel("processed_excel.xlsx", index=False)
