
const availableFields = ["Tip tranzactie", "Autorizare", "Banca", "Beneficiar", "Data", "Data valutei", "Detalii",
"Din contul", "In contul", "Nr. card", "Ordonator", "Rata", "Rata ING", "Referinta",
"Suma", "Suma transmisa spre decontare", "Terminal", "Cod Fiscal Platitor", "Impozit pe dobanda"];

const tipTranzactie = ["Cumparare POS", "Incasare", "Retragere numerar", "Taxe si comisioane", "Transfer",
    "Transfer Home'Bank", "Depunere numerar", "Comision pe operatiune", "Schimb valutar",
    "Acoperire sold", "Plata poprire", "Centralizare solduri", "Actualizare dobanda"];

document.getElementById('drop-area').addEventListener('click', () => document.getElementById('fileInput').click());
document.getElementById('fileInput').addEventListener('change', handleFileSelect);
document.getElementById('convertButton').addEventListener('click', processFile);

// Add event listeners for drag and drop
document.getElementById('drop-area').addEventListener('dragover', (event) => {
event.stopPropagation();
event.preventDefault();
event.dataTransfer.dropEffect = 'copy';
});
document.getElementById('drop-area').addEventListener('drop', (event) => {
event.stopPropagation();
event.preventDefault();
handleFileSelect(event);
});

let selectedFile;

function handleFileSelect(event) {
// Check if files were dropped or selected via input
selectedFile = (event.dataTransfer) ? event.dataTransfer.files[0] : event.target.files[0];
document.getElementById('file-name').textContent = ' ' + selectedFile.name;
// hide splash image
var iimgDiv = document.getElementById('iimg');
if (iimgDiv) {
    iimgDiv.style.display = 'none';
}
 
}

function processFile() {
if (!selectedFile) {
    alert("Please select a file first!");
    return;
}

const reader = new FileReader();
reader.onload = function (event) {
    const data = event.target.result;
    const workbook = XLSX.read(data, { type: 'binary' });
    const firstSheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[firstSheetName];
    const jsonData = XLSX.utils.sheet_to_json(worksheet);

    // Data extraction logic
    const extractedData = extractData(jsonData);

    // Output format logic
    const outputFormat = document.getElementById('outputFormat').value;
    switch (outputFormat) {
        case 'json':
            downloadFile(JSON.stringify(extractedData), 'output.json', 'application/json');
            break;
        case 'csv':
            const csvOutput = arrayToCSV(extractedData);
            downloadFile(csvOutput, 'output.csv', 'text/csv');
            break;
        case 'xlsx':
            const newWorkbook = XLSX.utils.book_new();
            const newWorksheet = XLSX.utils.json_to_sheet(extractedData);
            XLSX.utils.book_append_sheet(newWorkbook, newWorksheet, 'Extracted Data');
            XLSX.writeFile(newWorkbook, 'output.xlsx');
            break;
    }
};

reader.readAsBinaryString(selectedFile);
}

function extractData(jsonData) {


return jsonData.map(row => {

    let extractedRow = {
        'Data': row['Data'],
        'Detalii tranzactie': row['Detalii tranzactie'],
        'Debit': row['Debit'],
        'Credit': row['Credit'],
        'Balanta': row['Balanta'],
        'Tip tranzactie': detectTransactionType(row['Detalii tranzactie'], tipTranzactie)
    };

    let details = row['Detalii tranzactie'] || '';
    availableFields.forEach(field => {
        extractedRow[field] = extractField(details, field);
    });

    return extractedRow;
});
}
function detectTransactionType(detailText, transactionTypes) {
return transactionTypes.find(tt => detailText && detailText.startsWith(tt)) ||
    'NEW! ' + detailText.split(' ').slice(0, 2).join(' ');
}
function extractField(detailText, fieldName) {
let fieldRegex = new RegExp(fieldName + ':\\s*([^\\n]*)', 'i');
let match = fieldRegex.exec(detailText);
return match ? match[1].trim() : '';
}


function arrayToCSV(data) {
const csvRows = [];
const headers = Object.keys(data[0]);
csvRows.push(headers.join(','));

data.forEach(row => {
    const values = headers.map(header => JSON.stringify(row[header] || ''));
    csvRows.push(values.join(','));
});

return csvRows.join('\n');
}

function downloadFile(content, fileName, mimeType) {
const a = document.createElement('a');
const blob = new Blob([content], { type: mimeType });
a.href = URL.createObjectURL(blob);
a.download = fileName;
a.click();
}
