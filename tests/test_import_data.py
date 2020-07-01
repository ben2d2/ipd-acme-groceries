import unittest
from data_importer import DataImporter, InvalidFileExtensionException

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        self._class = DataImporter()

    def test_load_data_with_txt_file(self):
        self.assertEqual(self._class.load("foo.txt"), "Text file")

    def test_load_data_with_xlsx_file(self):
        self.assertEqual(self._class.load("foo.xlsx"), "Excel file")

    def test_raises_exception_with_invalid_file_extension(self):
        self.assertRaises(InvalidFileExtensionException, self._class.load, "foo.md")

if __name__ == '__main__':
    unittest.main()