Makes sens of ING Bank Home'Bank transactions → one variable per column csv

    python ingparser.py <path/to/input/xls/x> -o <output_file> -f <xlsx|csv|json>

optional arguments

- `-f` format [xlsx, csv, json] default/implicit: xlsx
- `-o` output filename

## Features / Roadmap

- [x] extract fields
- [x] save as xlsx / json / csv
- [x] add params
- [x] enhance xlsx, freeze 1st row, add filters – use openpyxl 
- [x] clean-up original ING xls 
- [ ] treat exceptions
- [ ] batch files
- [ ] consolidate to db
- [ ] browser / github.io version? 
- [ ] sync external data
    - [ ] trezorerie, known accounts db?
    - [ ] link to registrul comertului, termene by CUI?
- [ ] stats
- [ ] remove empty columns?

----

    available_fields = ["Tip tranzactie", "Autorizare", "Banca", "Beneficiar", "Data", "Data valutei", "Detalii", "Din contul", "In contul", "Nr. card", "Ordonator", "Rata", "Rata ING", "Referinta", "Suma", "Suma transmisa spre decontare", "Terminal", "Cod Fiscal Platitor", "Impozit pe dobanda"]

    tip_tranzactie = ["Cumparare POS", "Incasare", "Retragere numerar", "Taxe si comisioane", "Transfer", "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar", "Acoperire sold", "Plata poprire", "Actualizare dobanda"]


## Câmpuri 

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

vezi și: [Tranzactii ING prompts](tranzactii ING prompts.md) 

-----

prev notes 

### Curent

    Retragere numerarNr. card: 
    Cumparare POSNr. card: 
    Terminal: 
    IncasareOrdonator: 
    Din contul: 
    Detalii:
    Data:
    Referinta: 
    Suma: 
    Suma transmisa spre decontare: 

### EUR Account

    Incoming fundsReference number:  
    Ordering party:   
    From account:  
    Details:  
    Amount:  
    Rate:  
    Value date:  
    Message:  