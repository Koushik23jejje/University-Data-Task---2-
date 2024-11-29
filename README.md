# University Data Analysis

A Python project for generating and analyzing synthetic university data.

## Project Structure

```
├── data/
│   ├── constants.py      # Configuration constants
│   └── generate_data.py  # Data generation module
├── src/
│   ├── cleaning.py       # Data cleaning operations
│   ├── stats.py          # Statistical analysis
│   └── reporting.py      # Report generation
├── analyze.py            # Main analysis script
└── requirements.txt      # Project dependencies
```

## Features

- Synthetic university data generation
- Data cleaning and preprocessing
- Statistical analysis:
  - Basic statistics by country
  - Student population metrics
  - Faculty ratios
  - International student percentages
  - University rankings
  - Correlation analysis

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run analysis:
   ```bash
   python analyze.py
   ```

## Output Files

- `data/universities_cleaned.csv`: Cleaned dataset
- `data/correlations.csv`: Correlation matrix

## Data Fields

- University Name
- Country
- World Rank
- Number of Students
- Student-to-Faculty Ratio
- International Students (%)
- Academic Reputation Score