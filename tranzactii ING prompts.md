## Take 2

I need to create a Python script that would detect / extract specific details of financial transactions downloaded from ING Bank Romania Homebank (as xlsx). The results should be saved both as json and xlsx format.

Steps:
1. Read the input Excel file.
2. Parse the 'Detalii tranzactie' column to extract the various details.
3. Export the detected field values, also keep as reference the initial content of 'Detalii tranzactie' column. Both as json and csv files. The json file should not include empty attributes.

### Extracting fields from 'Detalii tranzactie'

#### init

The 'Detalii tranzactie' column stores a series of Transaction details. Data is stored in rows (delimited by new line \n ) but also multiple attributes can be found in the same row.
Attributes/variables have a name (including spaces) and end with ': ' 
Sometimes attribute names can be glued (w no space in between) from the first string which is the type of transaction.
The list of potential available fields is in 'available_fields

First, detect transaction type:
- Check if the cell data starts with any of the strings in 'tip_tranzactie'. If any matches, assign the matched string as 'Tip tranzactie'
- if none matched, 'tip tranzacție' = 'NEW! ' + {first 2 words from the start of the cell - strings separated by a space}

Then split cell data by newline \n, then, for each chunk:
look for the 'available_fields' strings. Split row by this known 'available_fields', and assign value to each found. The value is the characters in between 2 known field labels followed by ': '

available_fields = ["Tip tranzactie", "Autorizare", "Banca", "Beneficiar", "Data", "Data valutei", "Detalii", "Din contul", "In contul", "Nr. card", "Ordonator", "Rata", "Rata ING", "Referinta", "Suma", "Suma transmisa spre decontare", "Terminal", "Cod Fiscal Platitor"]
tip_tranzactie = ["Cumparare POS", "Incasare", "Retragere numerar", "Taxe si comisioane", "Transfer", "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar", "Acoperire sold", "Plata poprire"]

See also the attached
Tranzactii RON 2019+2020 sample input.xlsx
Tranzactii RON 2019+2020 sample output.xlsx 

#### 2 fine tunning

Great, with few errors:
1. 'Data' column adds 00:00:00 at the end of each record. Format should be yyyy/mm/dd
2. add more fields to extract from tip_tranzactie: ["Transfer", "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar", "Acoperire sold", "Plata poprire", "Centralizare solduri"]
updated tip_tranzactie = ["Cumparare POS", "Incasare", "Retragere numerar", "Taxe si comisioane", "Transfer", "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar", "Acoperire sold", "Plata poprire"]

#### 3 - remove cruft from xls

now, my input file is a xls, which also has some extra elements, some embedded images, and some unnecessary top and bottom rows, as in the attached file.
before processing the file, I would first need to remove all rows above 
'Data	Detalii tranzactie	Debit	Credit	Balanta'
and below the last transaction row (last row that has data for Data, Detalii tranzactie and either data for Debit or Credit. 


----

## Take 1

fields
---

## Columns 

- Data
- Detalii tranzactie
    - Tip tranzactie 
        - Cumparare POS
        - Incasare
        - Retragere numerar 
        - Taxe si comisioane
        - Transfer Homebank
    - Autorizare
    - Banca
    - Beneficiar
    - Data
    - Data valutei
    - Detalii
    - Din contul
    - In contul
    - Nr. card
    - Ordonator
    - Rata
    - Rata ING
    - Referinta
    - Suma
    - Suma transmisa spre decontare
    - Terminal
- Debit	
- Credit	
- Balanta
