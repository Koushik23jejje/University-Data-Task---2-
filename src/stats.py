"""Module for statistical analysis."""

import pandas as pd

def get_basic_stats(df):
    """Calculate basic statistics."""
    return {
        'total_universities': len(df),
        'universities_by_country': df['Country'].value_counts().to_dict(),
        'avg_students': df['Number of Students'].mean(),
        'avg_student_faculty_ratio': df['Student-to-Faculty Ratio'].mean(),
        'avg_international_students': df['International Students (%)'].mean()
    }

def get_top_universities(df, n=10):
    """Get top N universities by rank."""
    return df.nsmallest(n, 'World Rank')[['University Name', 'World Rank', 'Country']].to_dict('records')

def calculate_correlations(df):
    """Calculate correlations between numerical variables."""
    numerical_columns = df.select_dtypes(include=['number']).columns
    return df[numerical_columns].corr()