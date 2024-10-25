import pdfplumber
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load PDF and Extract Data
pdf_path = 'ELECT_Loans_Database_Table.pdf'
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    table = first_page.extract_table()

# Convert the extracted table to DataFrame
loan_data = pd.DataFrame(table[1:], columns=table[0])

# Debugging: Print the structure of the data
print("Extracted Data from PDF:")
print(loan_data.columns)
print(loan_data.head())

# 2. Load the CSV file
csv_path = 'CSV_of_ELECT_Loan_Data.csv'
csv_data = pd.read_csv(csv_path)

# 3. Data Cleaning
# Check and handle missing values
loan_data = loan_data.ffill()

# Drop duplicates if any
loan_data.drop_duplicates(inplace=True)

# Set LoanID as index (if required)
if 'LoanID' in loan_data.columns:
    loan_data.set_index('LoanID', inplace=True)

# Ensure relevant columns are numeric, check if 'Income' column exists first
if 'LoanAmount' in loan_data.columns:
    loan_data['LoanAmount'] = pd.to_numeric(loan_data['LoanAmount'], errors='coerce')

if 'Income' in loan_data.columns:
    loan_data['Income'] = pd.to_numeric(loan_data['Income'], errors='coerce')

# Proceed with analysis if columns are available
if 'LoanAmount' in loan_data.columns:
    loan_data['LoanAmount'].hist()
    plt.title('Loan Amount Distribution')
    plt.xlabel('Loan Amount')
    plt.ylabel('Frequency')
    plt.show()

if 'Income' in loan_data.columns:
    # 5.1 Income distribution (mean and standard deviation)
    income_mean = loan_data['Income'].mean()
    income_std = loan_data['Income'].std()
    print(f"Income Distribution: Mean = {income_mean}, Standard Deviation = {income_std}")
    
    #
