import unittest
from data_importer import DataImporter, InvalidFileExtensionException

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        self._class = DataImporter()

    def test_load_as_dataframe_with_txt_file(self):
        df = self._class.load_as_dataframe("tests/fixtures/test-201905.txt")
        # given files with 4 rows and 6 unique dates in multiple columns
        self.assertEqual(len(df.values), 24)

    def test_load_as_dataframe_with_xlsx_file(self):
        df = self._class.load_as_dataframe("tests/fixtures/test-201904.xlsx")
        # given files with 4 rows and 6 unique dates in multiple columns
        self.assertEqual(len(df.values), 24)

    def test_raises_exception_with_invalid_file_extension(self):
        self.assertRaises(InvalidFileExtensionException, self._class.load_as_dataframe, "foo.md")

if __name__ == '__main__':
    unittest.main()