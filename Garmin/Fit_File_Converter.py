#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# Rest of your Python code
from fitparse import FitFile
import csv
import os
import zipfile

# Function to get the most recent .zip file in a directory
def get_most_recent_zip_file(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.zip')]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    return os.path.join(directory, files[0]) if files else None

# Directory containing your .zip files
directory = '/Users/tytemple/Documents/GARMIN DATA/'

# Get the most recent .zip file
zip_file_path = get_most_recent_zip_file(directory)
if not zip_file_path:
    print("No .zip files found.")
    exit()

# Unzip the .fit file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(directory)
    fit_file_path = os.path.join(directory, zip_ref.namelist()[0])

# Initialize variables
accumulated_power = 0
sport = ''
timestamp = ''

# Loop through each data message in the .fit file
fitfile = FitFile(fit_file_path)
for record in fitfile.get_messages('session'):
    for record_data in record:
        if record_data.name == 'sport':
            sport = record_data.value
        if record_data.name == 'start_time':
            timestamp = record_data.value.strftime('%Y-%m-%d')

# Create a CSV file to store the extracted data
csv_file_name = os.path.join(directory, f"{sport}_{timestamp}.csv")
with open(csv_file_name, 'w', newline='') as csvfile:
    fieldnames = ['timestamp', 'altitude', 'heart_rate', 'cadence', 'distance', 'speed', 'power', 'accumulated_power', 'sport']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for record in fitfile.get_messages('record'):
        data = {}
        for record_data in record:
            if record_data.name in fieldnames:
                data[record_data.name] = record_data.value

        # Calculate accumulated power
        if 'power' in data:
            accumulated_power += data['power']
            data['accumulated_power'] = accumulated_power

        # Write to CSV
        writer.writerow(data)

# Delete the .fit and .zip files
os.remove(fit_file_path)
os.remove(zip_file_path)

print(f"Data extracted to {csv_file_name} and .fit and .zip files deleted.")
