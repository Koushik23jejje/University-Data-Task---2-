import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load university data from CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded university dataset
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the university dataset by handling missing values.
    
    Args:
        df (pd.DataFrame): Input university dataset
        
    Returns:
        pd.DataFrame: Cleaned university dataset
    """
    # Make a copy to avoid modifying the original dataframe
    df_cleaned = df.copy()
    
    # Fill missing numerical values with median
    numerical_columns = df_cleaned.select_dtypes(include=[np.number]).columns
    for col in numerical_columns:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
    
    # Fill missing categorical values with mode
    categorical_columns = df_cleaned.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])
    
    return df_cleaned