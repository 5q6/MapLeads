import os
import tempfile
import unittest
from openpyxl import load_workbook

from excel_export import export_excel


class ExportExcelTests(unittest.TestCase):
    def test_export_creates_workbook_with_rows(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            original_cwd = os.getcwd()
            try:
                os.chdir(tmp_dir)
                rows = [
                    {"name": "Cafe A", "phone": "123", "address": "Test Street"},
                    {"name": "Cafe B", "phone": "456", "address": "Second Street"},
                ]

                export_excel(rows)

                output_file = os.path.join(tmp_dir, "output", "cafe_leads.xlsx")
                self.assertTrue(os.path.exists(output_file))

                workbook = load_workbook(output_file)
                sheet = workbook.active
                self.assertEqual(sheet.max_row, 3)
                self.assertEqual(sheet["A1"].value, "name")
                self.assertEqual(sheet["B1"].value, "phone")
                self.assertEqual(sheet["C1"].value, "address")
                self.assertEqual(sheet["A2"].value, "Cafe A")
            finally:
                os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
