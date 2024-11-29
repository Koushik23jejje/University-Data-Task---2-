"""Module for generating synthetic university data."""

import pandas as pd
import numpy as np
from .constants import *

def generate_university_data(num_universities=100, random_seed=42):
    """Generate synthetic university dataset."""
    np.random.seed(random_seed)
    
    data = {
        "University Name": [f"University {i+1}" for i in range(num_universities)],
        "Country": np.random.choice(COUNTRIES, size=num_universities),
        "World Rank": np.random.randint(MIN_RANK, MAX_RANK, num_universities),
        "Number of Students": np.random.randint(MIN_STUDENTS, MAX_STUDENTS, num_universities),
        "Student-to-Faculty Ratio": np.round(np.random.uniform(MIN_FACULTY_RATIO, MAX_FACULTY_RATIO, num_universities), 2),
        "International Students (%)": np.random.randint(MIN_INTERNATIONAL, MAX_INTERNATIONAL, num_universities),
        "Academic Reputation Score": np.round(np.random.uniform(MIN_REPUTATION, MAX_REPUTATION, num_universities), 2),
    }
    
    df = pd.DataFrame(data)
    mask = np.random.choice([True, False], size=df.shape, p=[MISSING_RATE, 1-MISSING_RATE])
    return df.mask(mask)