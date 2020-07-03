import logging
import unittest
from data_importer import DataImporter
from report import Report

class TestReport(unittest.TestCase):
    def setUp(self):
        data_importer = DataImporter()
        dataframe = data_importer.load_as_dataframe_with_schema('tests/fixtures/test-201905-with-rows-with-zeros.txt')
        self._class = Report(dataframe)
        # disable logging
        logging.disable(logging.CRITICAL)

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        results = self._class.gather_data('foo.csv')
        # given file with 5 rows, one of which has all zeros, and 6 unique dates in multiple columns
        self.assertEqual(len(results), 24)

if __name__ == '__main__':
    unittest.main()