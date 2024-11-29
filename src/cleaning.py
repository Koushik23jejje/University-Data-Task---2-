"""Module for data cleaning operations."""

import pandas as pd
import numpy as np

def fill_missing_values(df):
    """Fill missing values in the dataset."""
    df_cleaned = df.copy()
    
    # Fill missing numerical values with median
    numerical_cols = df_cleaned.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
    
    # Fill missing categorical values with mode
    categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0])
    
    return df_cleaned