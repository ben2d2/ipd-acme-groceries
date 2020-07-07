import unittest
import logging
import os
import pandas as pd
from data_importer import DataImporter

class TestBase(unittest.TestCase):
    TEST_PERSISTENCE_FILE_PATH = 'master.csv'

    def setUp(self):
        # disable logging
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        # delete TEST_PERSISTENCE_FILE_PATH test file
        if os.path.exists(self.TEST_PERSISTENCE_FILE_PATH):
            os.remove(self.TEST_PERSISTENCE_FILE_PATH)

    def read_persistence_file(self):
        # read from persistence file TEST_PERSISTENCE_FILE_PATH
        dataframe = pd.read_csv(self.TEST_PERSISTENCE_FILE_PATH, index_col=[0])
        dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])

        return dataframe

    def load_data(self, from_file_path):
        DataImporter().load_and_save(from_file_path, self.TEST_PERSISTENCE_FILE_PATH)