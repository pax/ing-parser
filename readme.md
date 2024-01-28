Makes sens of ING Bank Home'Bank transactions → one variable per column csv


### ing-parser.py

    python ing-parser.py <path/to/input/xls/x> -o <output_file> -f <xlsx|csv|json>

optional arguments

- `-f` format [xlsx, csv, json] default/implicit: xlsx
- `-o` output filename

---

### ing-parser.html

js / browser based (buggy, WIP)

![js/html version](assets/drop-ing.png "Browser version")


## Features / Roadmap

- [x] extract fields
- [x] save as xlsx / json / csv
- [x] add params
- [x] enhance xlsx, freeze 1st row, add filters – use openpyxl 
- [x] clean-up original ING xls 
- [ ] extract currency
- [ ] extract businesses names from Terminal (before RO?)
    - [ ] business list francizes (with ID in name). Regex? – Ex: OMV, KAUFLAND, LIDL, Glovo, LUCA etc     
- [ ] extract adress info (country, county, internet)
- [ ] treat exceptions
    - [ ] check input file type
    - [ ] check input file structure before processing?
- [ ] batch convert
- [ ] save - detect account number?
- [ ] consolidate to db / csv?
    - [ ] stats / dashboard
- [x] browser / client-side (buggy)
    - [ ] FIXME: detect all properties
    - [ ] minimal stats
    - [ ] ingparser.github.io (with inline vendor js) / PWA
    - [ ] local csv repository
    - [ ] overall stats / dashboard
- [ ] sync external data
    - [ ] trezorerie, known accounts db?
    - [ ] link to registrul comertului, termene by CUI?
    - [ ] interbank exchange rate
- [ ] remove empty columns?
- [ ] extend to other banks?
    - [x] ING

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

vezi și: [Tranzactii ING prompts](assets/tranzactii ING prompts.md), GPT chats: [1](https://chat.openai.com/share/fe3ce803-2c4e-4c74-9426-e1447899384a), [2](https://chat.openai.com/share/f4c7ddb8-dfc4-40c2-a235-0f3414f7e3d3)  

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