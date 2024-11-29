from data.generate_data import generate_university_data
from src.data_processing import clean_data
from src.analysis import calculate_summary_statistics, analyze_correlations
from src.utils import format_summary_stats

def main():
    # Generate synthetic data
    print("Generating university dataset...")
    df = generate_university_data()
    
    # Clean the data
    print("Cleaning dataset...")
    df_cleaned = clean_data(df)
    
    # Perform analysis
    print("Analyzing data...")
    summary_stats = calculate_summary_statistics(df_cleaned)
    correlations = analyze_correlations(df_cleaned)
    
    # Display results
    print("\n" + format_summary_stats(summary_stats))
    
    print("\nCorrelation Matrix:")
    print(correlations.round(2))
    
    # Save results
    df_cleaned.to_csv("data/universities_cleaned.csv", index=False)
    correlations.to_csv("data/correlations.csv")
    
    print("\nAnalysis complete! Results saved to CSV files.")

if __name__ == "__main__":
    main()