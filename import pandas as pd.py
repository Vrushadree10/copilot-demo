import pandas as pd

# Use raw string (r"") or double backslashes for Windows file paths
df = pd.read_excel(r"C:\Users\Akshitha\Downloads\Example.xlsx")

# Replace 'Logical ID' with the actual column name in your sheet
duplicates = df[df.duplicated('Logical ID', keep=False)]

print("Duplicate Logical IDs:")
print(duplicates[['Logical ID']])