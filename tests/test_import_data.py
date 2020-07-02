import unittest
from data_importer import DataImporter, InvalidFileExtensionException, InvalidHeaderWithDateFormatException, InvalidDataFormatException
from xlrd import XLRDError
from pandas.errors import ParserError

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        self._class = DataImporter()

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_load_as_dataframe_with_schema_using_txt_file(self):
        df = self._class.load_as_dataframe_with_schema('tests/fixtures/test-201905.txt')
        # given files with 4 rows and 6 unique dates in multiple columns
        self.assertEqual(len(df.values), 24)

    def test_load_as_dataframe_with_schema_using_xlsx_file(self):
        df = self._class.load_as_dataframe_with_schema('tests/fixtures/test-201904.xlsx')
        # given files with 4 rows and 6 unique dates in multiple columns
        self.assertEqual(len(df.values), 24)

    def test_raises_exception_with_invalid_file_extension(self):
        self.assertRaises(InvalidFileExtensionException, self._class.load_as_dataframe_with_schema, 'foo.md')

    def test_raises_exception_with_invalid_data_format(self):
        self.assertRaises(InvalidDataFormatException, self._class.load_as_dataframe_with_schema, 'tests/fixtures/test-201905-invalid-data.txt')

    # TESTS GET FILE AS DATAFRAME
    def test_get_file_as_dataframe_with_txt_file(self):
        df = self._class.get_file_as_dataframe('tests/fixtures/test-201905.txt')
        # given files with 4 rows
        self.assertEqual(len(df.values), 4)

    def test_get_file_as_dataframe_with_xlsx_file(self):
        df = self._class.get_file_as_dataframe('tests/fixtures/test-201904.xlsx')
        # given files with 4 rows
        self.assertEqual(len(df.values), 4)

    def test_raises_exception_with_invalid_file_format_get_file_as_dataframe_xlsx(self):
        self.assertRaises(XLRDError, self._class.get_file_as_dataframe, 'tests/fixtures/test-201905-bad-format.xlsx')

    def test_raises_exception_with_invalid_file_format_get_file_as_dataframe_txt(self):
        self.assertRaises(ParserError, self._class.get_file_as_dataframe, 'tests/fixtures/test-201904-bad-format.txt')

    # TESTS GET DATE AND KEY TUPLE
    def test_get_date_and_key_tuple(self):
        date_and_key_tuple = self._class.get_date_and_key_tuple('2020-1 Units')
        self.assertEqual(date_and_key_tuple, ('2020-1', 'Units'))

    def test_raises_exception_with_invalid_data_get_date_and_key_tuple(self):
        self.assertRaises(InvalidHeaderWithDateFormatException, self._class.get_date_and_key_tuple, '2020-1Units')

if __name__ == '__main__':
    unittest.main()