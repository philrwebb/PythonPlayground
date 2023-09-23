# Importing required libraries
# tkinter for file dialog
# pandas to flatten the JSON data
import pandas as pd
from pandas import json_normalize
# json to deal with JSON data
import json
from Cocoa import NSOpenPanel, NSFileHandlingPanelOKButton
from Foundation import NSURL

def choose_file():
    dialog = NSOpenPanel.alloc().init()
    dialog.setAllowedFileTypes_(["json"])
    dialog.setDirectoryURL_(NSURL.fileURLWithPath_("./"))
    dialog.setCanChooseFiles_(True)
    dialog.setCanChooseDirectories_(False)
    dialog.setAllowsMultipleSelection_(False)
    dialog.setTitle_("Choose a file")

    if dialog.runModal() == NSFileHandlingPanelOKButton:
        result = dialog.URLs()[0]
        return result.fileSystemRepresentation()
    return None

file_path = choose_file()

print(f"Selected file: {file_path.decode('utf-8')}")

# if they pick a file, process it
if file_path:

    # Reading the JSON file
    with open(file_path.decode('utf-8'), 'r') as f:
        data = json.load(f)

    # Flattening the JSON data
    flattened_data = json_normalize(data['value'], sep='_')

    # Converting the flattened data to a pandas DataFrame
    df = pd.DataFrame(flattened_data)

    # Saving the DataFrame to a CSV file in the same directory as the JSON file.
    csv_file_path = file_path.decode('utf-8').replace(".json", ".csv")
    df.to_csv(csv_file_path, index=False)
else:
    print("No file selected")
