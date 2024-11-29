"""Main script for university data analysis."""

from data.generate_data import generate_university_data
from src.cleaning import fill_missing_values
from src.stats import get_basic_stats, get_top_universities, calculate_correlations
from src.reporting import create_summary_report

def main():
    # Generate and clean data
    print("Generating and cleaning data...")
    df = generate_university_data()
    df_cleaned = fill_missing_values(df)
    
    # Calculate statistics
    print("Calculating statistics...")
    basic_stats = get_basic_stats(df_cleaned)
    top_unis = get_top_universities(df_cleaned)
    correlations = calculate_correlations(df_cleaned)
    
    # Generate and display report
    print("\n" + create_summary_report(basic_stats, top_unis))
    print("\nCorrelation Matrix:")
    print(correlations.round(2))
    
    # Save results
    print("\nSaving results...")
    df_cleaned.to_csv("data/universities_cleaned.csv", index=False)
    correlations.to_csv("data/correlations.csv")
    print("Analysis complete!")

if __name__ == "__main__":
    main()