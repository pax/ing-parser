
""" 
# TODO
- [x] extract fields
- [x] save as xlsx / json
- [x] add params
- [x] enhance xlsx, freeze 1st row, add filters – use openpyxl 
- [x] clean-up original ING xls 
- [ ] treat exceptions 
    - [ ] check file structure before processing?
- [ ] batch files
- [ ] FIXME: BUG? sometimes doesn't detect tip transaction? after NEW! situation?

 """

# input_file = 'sample-data/Tranzactii RON 2019+2020 sample input.xlsx'
# input_file_path = 'sample-data/ING Curent 2018 Tranzactii_11-05-2022_15-53-36.xls'
input_file_path = 'sample-data/Tranzactii EUR 2 ani 211207-231113.xlsx'
output_excel_file = 'sample-data/ssample-outX2eur.xlsx'
output_json_file = 'sample-data/ssample-outJ2eur.json'

available_fields = ["Tip tranzactie", "Autorizare", "Banca", "Beneficiar", "Data", "Data valutei", "Detalii", 
                        "Din contul", "In contul", "Nr. card", "Ordonator", "Rata", "Rata ING", "Referinta", 
                        "Suma", "Suma transmisa spre decontare", "Terminal", "Cod Fiscal Platitor", "Impozit pe dobanda"]
tip_tranzactie = ["Cumparare POS", "Incasare", "Retragere numerar", "Taxe si comisioane", "Transfer", 
                    "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar", 
                    "Acoperire sold", "Plata poprire", "Centralizare solduri", "Actualizare dobanda"]

import argparse
import os
import pandas as pd
import json
import openpyxl
from openpyxl.styles import Alignment, Font
import xlrd

def read_and_clean_xls(file_path):
    # Read the entire xls file
    full_df = pd.read_excel(file_path, header=None)

    # Find the header row
    header_row = full_df[full_df.apply(lambda x: x.str.contains('Data').any() and x.str.contains('Detalii tranzactie').any(), axis=1)].index[0]

    # Find the last transaction row
    last_row = full_df[full_df[0].notna() & full_df[1].notna() & (full_df[2].notna() | full_df[3].notna())].index[-1]

    # Filter the dataframe
    cleaned_df = full_df.iloc[header_row:last_row + 1]
    cleaned_df.columns = cleaned_df.iloc[0]  # Set the first row as header
    cleaned_df = cleaned_df.drop(cleaned_df.index[0])  # Drop the original header row

    return cleaned_df

def extract_transaction_details(row, available_fields, tip_tranzactie):
    """
    Extract transaction details from a given transaction detail text.
    """
    details = {}
    details_text = row['Detalii tranzactie']
    details_text_split = details_text.split('\n')

    # First, detect transaction type
    details['Tip tranzactie'] = next((tt for tt in tip_tranzactie if details_text.startswith(tt)), 
                                      'NEW! ' + ' '.join(details_text.split()[:2]))
    # Extract other details
    for chunk in details_text_split:
        for field in available_fields:
            if field + ':' in chunk:
                # Extract the value between the current and next field
                start_pos = chunk.find(field + ':') + len(field) + 2
                end_pos = len(chunk)
                for next_field in available_fields:
                    if next_field + ':' in chunk and chunk.find(next_field + ':') > chunk.find(field + ':'):
                        end_pos = min(end_pos, chunk.find(next_field + ':'))
                value = chunk[start_pos:end_pos].strip()
                details[field] = value

    return details

def main(input_file_path, output, output_format):

    # Read the input Excel file

    input_df = read_and_clean_xls(input_file_path) if input_file_path.endswith('.xls') else pd.read_excel(input_file_path)
    base_path, _ = os.path.splitext(input_file_path)
    output_path = base_path + '_parsed' if output is None else output

    extracted_details = input_df.apply(lambda row: extract_transaction_details(row, available_fields, tip_tranzactie), axis=1)
    details_df = pd.DataFrame(extracted_details.tolist())

    # Renaming overlapping columns in the details dataframe
    details_df = details_df.rename(columns=lambda x: x + "_extracted" if x in input_df.columns else x)

    # Merging the extracted details with the original dataframe
    output_df = input_df.join(details_df)

    # Convert 'Data' column to datetime and format it
    output_df['Data'] = pd.to_datetime(output_df['Data']).dt.strftime('%Y/%m/%d')

    base_path, _ = os.path.splitext(input_file_path)
    output_path = base_path + '_parsed' if output is None else output

    output_excel_path = output_path + '.xlsx'
    output_json_path = output_path + '.json'
    output_csv_path = output_path + '.csv'

 
    if output_format == 'json':

        # Preparing and saving the JSON output
        output_json = output_df.apply(lambda row: row.dropna().to_dict(), axis=1).tolist()
        output_json_str = json.dumps(output_json, indent=4, ensure_ascii=False)
        with open(output_json_path, 'w', encoding='utf-8') as file:
            file.write(output_json_str)
    elif output_format == 'csv':
        # input_df.to_csv(output_csv_path, index=False)
        output_df.to_csv(output_csv_path, index=False)
    else:
        # fancy xlsx - freeze 1st row, add filters
        with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
            output_df.to_excel(writer, index=False, sheet_name='Transactions')

            # Freeze the first row and add filters to the header columns
            workbook = writer.book
            worksheet = writer.sheets['Transactions']

            for row in worksheet.iter_rows():
                for cell in row:
                    cell.font = Font(name='Arial Narrow', size=10)
                    cell.alignment = Alignment(wrap_text=True, vertical='top')

            worksheet.freeze_panes = 'A2'  # Freeze the first row
            worksheet.auto_filter.ref = worksheet.dimensions  # Add filters to the header columns

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process ING Bank transactions.')
    parser.add_argument('input', type=str, help='Input file path (xls or xlsx)')
    parser.add_argument('-o', '--output', type=str, help='Output file base name or path (without extension)', default=None)
    parser.add_argument('-f', '--format', type=str, help='Output format (json, xlsx, or csv)', choices=['json', 'xlsx', 'csv'], default='xlsx')

    args = parser.parse_args()
    main(args.input, args.output, args.format)
