import sys
import os
import pandas as pd

# Direct the Python system path to look inside your src/ folder correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import load_and_process_data

def test_no_duplicates():
    """
    Unit test asserting that duplicate entries are reduced to zero after processing.
    """
    # Execute the processing function to create our output dataset
    df_result = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    
    # Mathematically count the number of duplicate rows left
    duplicate_count = df_result.duplicated().sum()
    
    # Assert that the number of duplicate rows remaining is exactly zero
    assert duplicate_count == 0, f"Validation Failed: Found {duplicate_count} remaining duplicate rows!"
