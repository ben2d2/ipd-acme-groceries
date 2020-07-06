import logging
import unittest
import os
import pandas as pd
from data_importer import DataImporter
from summary import Summary

class TestSummary(unittest.TestCase):
    def setUp(self):
        data_importer = DataImporter()
        data_importer.load_as_dataframe_with_schema('tests/fixtures/test-201905.txt')
        dataframe = pd.read_csv('master.csv')
        dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])
        self._class = Summary(dataframe)
        # disable logging
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        os.remove('master.csv')

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        result = self._class.calculate_for('Produce', '2018', '12')
        self.assertEqual(result, 'Produce - Total Units: 717, Total Gross Sales: 11658.83')

    def test_calculate_for_no_data_available(self):
        result = self._class.calculate_for('NotACategory', '2020', '1')
        self.assertEqual(result, 'No data available')

    def test_calculate_for_with_duplicates(self):
        data_importer = DataImporter()
        data_importer.load_as_dataframe_with_schema('tests/fixtures/test-201905-with-dupes.txt')
        dataframe = pd.read_csv('master.csv')
        dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])
        summary = Summary(dataframe)
        result = summary.calculate_for('Produce', '2018', '12')
        self.assertEqual(result, 'Produce - Total Units: 717, Total Gross Sales: 11658.83')

if __name__ == '__main__':
    unittest.main()