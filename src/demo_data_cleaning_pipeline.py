# TSD-ID: SSD-1
# Filename: demo_data_cleaning_pipeline.py
# Purpose: To provide a clear, simplified demonstration of a multi-stage data cleaning
#          and transformation pipeline. This script serves as the technical appendix for the
#          "Case-Study-Cleaning-Legacy-Data" portfolio piece.

import csv
import io
from datetime import datetime
from pprint import pprint

# --- INPUT DATA ---
# In a real-world scenario, this data would be read from an external file (e.g., a .csv or .xlsx).
# For this self-contained demo, it's a hard-coded multi-line string representing
# messy, inconsistent, and incomplete legacy data.
MESSY_CSV_DATA = """
Internal ID,Full Name,Signup Date,Region,Notes
1001,john doe,01/05/2023,New York,First contact
1002,Jane Smith,May 2, 2023,N YC,Met at conference
1003,peter jones,03-05-2023,Chicago,
,Emily White,June 15, 2023,Los Angeles,Missing ID
1005,MICHAEL BROWN,,California,No signup date
1006,Sarah Green,20th of April 2023,chicago,
"""

# --- CONFIGURATION ---
# This dictionary represents the "business rules" for standardizing inconsistent data.
LOCATION_CORRECTIONS = {
    "N YC": "New York",
    "chicago": "Chicago",
    "California": "Los Angeles" # Assuming business rule is to map state to main city
}

def clean_and_structure_data(csv_data):
    """
    Orchestrates the full data cleaning pipeline.

    This function represents the core methodology of the case study: a sequential
    process of extracting raw data, applying a series of cleaning and standardization
    rules, and structuring the result for downstream use.

    Args:
        csv_data (str): A string containing raw, messy CSV data.

    Returns:
        list: A list of dictionaries, where each dictionary is a clean record.
    """
    
    # --- STEP 1: EXTRACTION ---
    # The first step is to parse the raw data and safely extract only the columns
    # we need. We use Python's built-in CSV reader for robustness and a try-except
    # block to gracefully handle malformed rows that don't have the expected number
    # of columns. This prevents the entire script from failing due to a single bad entry.
    print("Step 1: Extracting relevant columns from raw data...")
    
    # Use io.StringIO to treat the string as a file for the csv reader
    f = io.StringIO(csv_data)
    reader = csv.reader(f)
    
    # Skip the header row
    header = next(reader)
    
    extracted_records = []
    for row in reader:
        try:
            # We only care about the Full Name, Signup Date, and Region
            name = row[1]
            date_str = row[2]
            location = row[3]
            
            # Ignore rows with essential missing data
            if name and date_str:
                extracted_records.append({'name': name, 'date_str': date_str, 'location': location})
        except IndexError:
            # This catches rows that are too short or malformed.
            print(f"  - Skipping malformed row: {row}")
            continue

    print(f"  -> Successfully extracted {len(extracted_records)} valid records.\n")


    # --- STEP 2: CLEANSING & STANDARDIZATION ---
    # This is the core transformation phase. We apply a series of simple,
    # single-purpose functions to standardize each piece of data according to
    # our defined business rules.
    print("Step 2: Applying cleaning and standardization rules...")
    
    clean_records = []
    for record in extracted_records:
        
        # Apply each cleaning function sequentially.
        clean_name = _format_name(record['name'])
        standardized_date = _standardize_date(record['date_str'])
        standardized_location = _standardize_location(record['location'])
        
        # If a date could not be standardized, we skip the record. This is a
        # quality gate to ensure data integrity.
        if standardized_date:
            clean_records.append({
                'name': clean_name,
                'signup_date': standardized_date,
                'location': standardized_location
            })

    print(f"  -> Successfully cleaned {len(clean_records)} records.\n")
    return clean_records

def _format_name(name_str):
    """Capitalizes names correctly (e.g., 'john doe' -> 'John Doe')."""
    return name_str.strip().title()

def _standardize_date(date_str):
    """
    Parses common non-standard date formats and converts to 'YYYY-MM-DD'.
    Returns None if the format is unrecognized.
    """
    date_str = date_str.strip()
    # Try parsing format: "01/05/2023"
    try:
        return datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        pass
    # Try parsing format: "May 2, 2023"
    try:
        return datetime.strptime(date_str, '%B %d, %Y').strftime('%Y-%m-%d')
    except ValueError:
        pass
    # If all attempts fail, return None to signal an un-parsable date.
    print(f"  - Warning: Could not parse date '{date_str}'. Skipping record.")
    return None

def _standardize_location(location_str):
    """Corrects common misspellings or variations using the defined dictionary."""
    return LOCATION_CORRECTIONS.get(location_str.strip(), location_str.strip())


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- Starting Simplified Data Cleaning Pipeline ---\n")
    
    # --- STEP 3: STRUCTURING ---
    # The final step of the pipeline is to produce a clean, structured output.
    # In this case, a list of dictionaries, which is a standard, easy-to-use
    # format for any downstream application or database.
    final_clean_data = clean_and_structure_data(MESSY_CSV_DATA)
    
    print("Step 3: Final structured output ready for use.")
    print("--- Pipeline Complete ---\n")
    
    # Use pprint for a more readable printout of the final data structure.
    print("Final Clean Data:")
    pprint(final_clean_data)
