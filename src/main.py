import pandas as pd
import os

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    """
    Loads a dataset file, counts and removes identical duplicate rows, 
    and saves the cleaned dataset to a target output path.
    """
    # Safety validation check to ensure the file exists in the directory path
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Source file not found at: {filepath}")
        
    # Read the data using pandas
    df = pd.read_csv(filepath)
    print(f"Original dataset structure shape: {df.shape}")
    
    # Remove any overlapping duplicated rows entirely
    df_cleaned = df.drop_duplicates()
    print(f"Dataset structure shape after duplicate removal: {df_cleaned.shape}")
    
    # Save output dataset back to CSV inside the data folder
    df_cleaned.to_csv(output_path, index=False)
    print(f"Processed clean dataset saved successfully to: {output_path}")
    
    return df_cleaned

if __name__ == "__main__":
    # Execute the workflow function locally
    load_and_process_data()
