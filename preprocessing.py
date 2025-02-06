import pandas as pd
import numpy as np

# hello
def preprocess_data(input_path: str, output_path: str):
    """Loads data, cleans it, and saves the processed version."""
    df = pd.read_csv(input_path)

    # Handling missing values
    df.fillna(value={'education': df['education'].mode()[0], 'job': df['job'].mode()[0]}, inplace=True)

    # Handling categorical variables
    job_mappings = {'management':0, 'technician':1, 'entrepreneur':2, 'blue-collar':3, 'retired':4, 
                    'admin.':5, 'services':6, 'self-employed':7, 'unemployed':8, 'housemaid':9, 'student':10}

    marital_mappings = {'divorced':0, 'single':1, 'married':2}

    education_mappings = {'primary':1, 'secondary':2, 'tertiary':3}

    default_mappings = {'no':0, 'yes':1}

    housing_mappings = {'no':0, 'yes':1}

    loan_mappings = {'no':0, 'yes':1}

    month_mappings = {'jan':0, 'feb':1, 'mar':2, 'apr':3, 'may':4, 'jun':5, 'jul':6, 'aug':7, 'sep':8, 'oct':9, 'nov':10, 'dec':11}

    df['job'] = df['job'].apply(lambda x: job_mappings[x])
    df['marital'] = df['marital'].apply(lambda x: marital_mappings[x])
    df['education'] = df['education'].apply(lambda x: education_mappings[x])
    df['default'] = df['default'].apply(lambda x: default_mappings[x])
    df['housing'] = df['housing'].apply(lambda x: housing_mappings[x])
    df['loan'] = df['loan'].apply(lambda x: loan_mappings[x])
    df['month'] = df['month'].apply(lambda x: month_mappings[x])

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data("data/bank_marketing.csv", "data/processed_data.csv")
