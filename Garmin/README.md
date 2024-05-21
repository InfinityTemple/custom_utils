# Garmin Fit File Processor

## Description
This Python script automatically finds the most recent Garmin `.zip` file in a specified directory, unzips it to extract the `.fit` file, and then processes the `.fit` file to extract specific workout data. The extracted data is saved as a CSV file, and both the `.fit` and `.zip` files are deleted after processing.

## Requirements
- Python 3.x
- fitparse library (`pip install fitparse`)

## Usage
1. Place your Garmin `.zip` files in a directory.
2. Update the `directory` variable in the script to point to this directory.
3. Run the script.

## Output
A CSV file named based on the sport and date will be generated in the same directory. The original `.zip` and `.fit` files will be deleted.

## Data Fields Extracted
- Timestamp
- Altitude
- Heart Rate
- Cadence
- Distance
- Speed
- Power
- Accumulated Power
- Sport
