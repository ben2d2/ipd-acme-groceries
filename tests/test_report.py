import logging
import unittest
import os
import pandas as pd
from data_importer import DataImporter
from report import Report

class TestReport(unittest.TestCase):
    def setUp(self):
        # import and save data
        DataImporter().load_and_save('tests/fixtures/test-201904.xlsx', 'master.csv')
        DataImporter().load_and_save('tests/fixtures/test-201905-with-rows-with-zeros.txt', 'master.csv')
        # read from persistence file master.csv
        dataframe = pd.read_csv('master.csv')
        dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])
        self._class = Report(dataframe)
        # disable logging
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        # delete master.csv test file
        os.remove('master.csv')

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        results = self._class.gather_data()
        # given xlsx with 4 rows, some rows are dupes from the txt file
        # and 6 unique dates in multiple columns with one unique from txt file
        # given txt with 5 rows, one row has all zeros, and 6 unique dates in multiple columns
        self.assertEqual(len(results), 28)

if __name__ == '__main__':
    unittest.main()