import logging
import pandas as pd
from test_base import TestBase
from data_importer import DataImporter
from summary import Summary

class TestSummary(TestBase):
    def setUp(self):
        super().setUp()
        # import and save data
        DataImporter().load_and_save('tests/fixtures/test-201905.txt', self.TEST_TO_FILE_PATH)
        # read from persistence file and init class
        self._class = Summary(self.read_persistence_file())

    def tearDown(self):
        super().tearDown()

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        result = self._class.calculate_for('Produce', '2018', '12')
        self.assertEqual(result, 'Produce - Total Units: 717, Total Gross Sales: 11658.83')

    def test_calculate_for_no_data_available(self):
        result = self._class.calculate_for('NotACategory', '2020', '1')
        self.assertEqual(result, 'No data available')

    def test_calculate_for_with_duplicates(self):
        # import and save concat with previous data
        df = DataImporter().load_and_save('tests/fixtures/test-201905-with-dupes.txt', self.TEST_TO_FILE_PATH)
        # read from persistence file TEST_TO_FILE_PATH
        dataframe = pd.read_csv(self.TEST_TO_FILE_PATH)
        dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])
        summary = Summary(dataframe)
        
        result = summary.calculate_for('Produce', '2018', '12')
        self.assertEqual(result, 'Produce - Total Units: 717, Total Gross Sales: 11658.83')

if __name__ == '__main__':
    unittest.main()