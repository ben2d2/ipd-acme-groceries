import logging
import unittest
from data_importer import DataImporter
from summary import Summary
from exceptions.data_importer_exceptions import (
    InvalidFileExtensionException, 
    InvalidHeaderWithDateFormatException, 
    InvalidDataFormatException
)
from xlrd import XLRDError
from pandas.errors import ParserError

class TestSummary(unittest.TestCase):
    def setUp(self):
        data_importer = DataImporter()
        dataframe = data_importer.load_as_dataframe_with_schema('tests/fixtures/test-201905.txt')
        self._class = Summary(dataframe)
        # disable logging
        logging.disable(logging.CRITICAL)

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        result = self._class.calculate_for('Produce', '2018', '12')
        self.assertEqual(result, 'Produce - Total Units: 717, Total Gross Sales: 11658.83')

    def test_calculate_for_no_data_available(self):
        result = self._class.calculate_for('NotACategory', '2020', '1')
        self.assertEqual(result, 'No data available')

if __name__ == '__main__':
    unittest.main()