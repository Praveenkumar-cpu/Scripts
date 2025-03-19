import pandas as pd
import re

def extract_net_disbursement_amount(excel_file):
    """
    Extracts the 'should match with the net disbursement amount' values from an Excel file.

    Args:
        excel_file (str): Path to the Excel file.

    Returns:
        pandas.DataFrame: A DataFrame with 'Partner Loan ID' and 'Net Disbursement Amount' columns.
    """

    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
    except FileNotFoundError:
        print(f"Error: File '{excel_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        return None

    net_amounts = []
    loan_ids = []

    for index, row in df.iterrows():
        query = row['Query']
        loan_id = row['Partner Loan ID']

        if isinstance(query, str):  # Check if the query is a string
            match = re.search(r"should match with the net disbursement amount:([\d,.]+)", query)
            if match:
                amount_str = match.group(1)
                amount = float(amount_str.replace(",", ""))  # Remove commas and convert to float
                net_amounts.append(amount)
                loan_ids.append(loan_id)
            else:
                net_amounts.append(None)  # Or handle missing values as needed
                loan_ids.append(loan_id)
        else:
            net_amounts.append(None)
            loan_ids.append(loan_id)

    result_df = pd.DataFrame({'Partner Loan ID': loan_ids, 'Net Disbursement Amount': net_amounts})
    return result_df

# Example usage:
excel_file_path = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/MTC .xlsx' # Replace with your excel file name.

extracted_data = extract_net_disbursement_amount(excel_file_path)

if extracted_data is not None:
    print(extracted_data)

    #Optionally, save the extracted data to a new excel file.
    output_excel_path = '/Users/praveenkumarb/IdeaProjects/supportscripts/scripts/partners/ManualApproval/extracted_data.xlsx'
    extracted_data.to_excel(output_excel_path, index=False)
    print(f"Extracted data saved to: {output_excel_path}")