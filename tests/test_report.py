import logging
from test_base import TestBase
from data_importer import DataImporter
from report import Report

class TestReport(TestBase):
    def setUp(self):
        super().setUp()
        # import and save data
        DataImporter().load_and_save('tests/fixtures/test-201904.xlsx', self.TEST_TO_FILE_PATH)
        DataImporter().load_and_save('tests/fixtures/test-201905-with-rows-with-zeros.txt', self.TEST_TO_FILE_PATH)
        # read from persistence file and init class
        self._class = Report(self.read_persistence_file())

    def tearDown(self):
        super().tearDown()

    # TESTS LOADING DATAFRAME USING MASTER SCHEMA
    def test_calculate_for(self):
        results = self._class.gather_data()
        # given xlsx with 4 rows, some rows are dupes from the txt file
        # and 6 unique dates in multiple columns with one unique from txt file
        # given txt with 5 rows, one row has all zeros, and 6 unique dates in multiple columns
        self.assertEqual(len(results), 28)

if __name__ == '__main__':
    unittest.main()