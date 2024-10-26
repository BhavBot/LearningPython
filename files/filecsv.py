import os

current_dir = os.path.dirname(__file__)  # Get the directory of the current script
os.chdir(current_dir)

import csv

# Writing to a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('./data/data.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print("CSV data written to 'data.csv' successfully!")

# Reading from a CSV file
with open('./data/data.csv', 'r',encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)