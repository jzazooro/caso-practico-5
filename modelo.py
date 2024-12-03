import pandas as pd

# Load the uploaded dataset
file_path = 'client_seg_telco.csv'
# Inspect the raw file to identify potential formatting issues
with open(file_path, 'r') as file:
    lines = file.readlines()

# Display the first few lines to understand the issue
lines[:15]
