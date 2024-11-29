import pandas as pd
import numpy as np

def calculate_summary_statistics(df):
    """
    Calculate summary statistics for the university dataset.
    
    Args:
        df (pd.DataFrame): University dataset
        
    Returns:
        dict: Dictionary containing various summary statistics
    """
    stats = {
        'total_universities': len(df),
        'universities_by_country': df['Country'].value_counts().to_dict(),
        'avg_students': df['Number of Students'].mean(),
        'avg_student_faculty_ratio': df['Student-to-Faculty Ratio'].mean(),
        'avg_international_students': df['International Students (%)'].mean(),
        'top_10_universities': df.nsmallest(10, 'World Rank')[['University Name', 'World Rank', 'Country']].to_dict('records')
    }
    return stats

def analyze_correlations(df):
    """
    Analyze correlations between numerical variables.
    
    Args:
        df (pd.DataFrame): University dataset
        
    Returns:
        pd.DataFrame: Correlation matrix
    """
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    return df[numerical_columns].corr()