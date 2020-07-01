import unittest
from data_importer import DataImporter, InvalidImportException

class TestDataImporter(unittest.TestCase):
    def setUp(self):
        self._class = DataImporter()

    def test_load_data(self):
        self.assertEqual(self._class.load("foo.txt"), "foo.txt")

    def test_raises_exception_with_invalid_file_type(self):
        self.assertRaises(InvalidImportException, self._class.load, "foo.md")

if __name__ == '__main__':
    unittest.main()