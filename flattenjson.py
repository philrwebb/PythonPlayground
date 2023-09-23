# Importing required libraries
# tkinter for file dialog
import tkinter as tk
from tkinter import filedialog
# pandas to flatten the JSON data
import pandas as pd
from pandas import json_normalize
# json to deal with JSON data
import json

# initialize tkinter
root = tk.Tk()
root.withdraw()

# ask user to select the JSON file - start in current directory
file_path = filedialog.askopenfilename(filetypes=[("JSON files","*.json")], initialdir=".")

# if they pick a file, process it
if file_path:

    # Reading the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Flattening the JSON data
    flattened_data = json_normalize(data['value'], sep='_')

    # Converting the flattened data to a pandas DataFrame
    df = pd.DataFrame(flattened_data)

    # Saving the DataFrame to a CSV file in the same directory as the JSON file.
    csv_file_path = file_path.replace(".json", ".csv")
    df.to_csv(csv_file_path, index=False)
else:
    print("No file selected")
