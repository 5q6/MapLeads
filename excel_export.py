
import os
from openpyxl import Workbook


def export_excel(data):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Cafe Leads"

    if data:
        headers = list(data[0].keys())
        sheet.append(headers)
        for row in data:
            sheet.append([row.get(header, "") for header in headers])
    else:
        sheet.append([])

    file_path = os.path.join(output_dir, "cafe_leads.xlsx")
    workbook.save(file_path)
    return file_path
