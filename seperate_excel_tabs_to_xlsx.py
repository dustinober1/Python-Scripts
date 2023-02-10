import pandas as pd

# Load the Excel file into a dictionary of dataframes, where each key is the sheet name
xlsx = pd.read_excel("file.xlsx", sheet_name=None)

# Loop through each sheet in the dictionary
for sheet_name, df in xlsx.items():
    # Save the dataframe to a separate Excel file
    df.to_excel(f"{sheet_name}.xlsx", index=False)
