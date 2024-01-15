import openpyxl
from json import dump

file_path = "softwares.xlsx"

output_list = []
workbook = openpyxl.load_workbook(file_path)
sheet = workbook['softwares']

for rowNumber in range(2, sheet.max_row+1):
    rowData = {
        "name" : sheet[f"A{rowNumber}"].value,
        "image" : sheet[f"B{rowNumber}"].value,
        "platforms" : sheet[f"C{rowNumber}"].value,
        "keyW" : sheet[f"D{rowNumber}"].value,
        "keyP" : sheet[f"E{rowNumber}"].value,
        "keyX" : sheet[f"F{rowNumber}"].value
    }
    output_list.append(rowData)

# Writing JSON to a file
with open("softwaresFromExcel.json", "w") as jsonFile:
    dump(output_list, fp=jsonFile, indent=3)
