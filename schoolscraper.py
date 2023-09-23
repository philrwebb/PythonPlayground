import requests
import re
import json
import csv

url = "https://www.det.wa.edu.au/schoolsonline/school_list.do"  # Replace with your URL

response = requests.get(url)
html_content = response.text

# Use regex to find the script tag containing the JSON data
pattern = r'var jqSchoolList = \[(.*?)\];'
match = re.search(pattern, html_content, re.DOTALL)

if match:
    json_data_str = match.group(1)
    json_data_str = json_data_str.replace("label", "\"label\"").replace("pageurl", "\"pageurl\"").replace("newSch", "\"newSch\"").replace("value", "\"value\"")
    json_data = json.loads("[" + json_data_str + "]")

    with open("schools.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["school", "id"])  # Write header row
        for item in json_data:
            writer.writerow([item["label"], item["value"]])  # Write data rows

    print("CSV data written to schools.csv")
else:
    print("JSON data not found in the script tag.")
