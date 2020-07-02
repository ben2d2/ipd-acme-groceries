import logging
import unittest
from exceptions.data_importer_exceptions import (
    InvalidFileExtensionException, 
    InvalidHeaderWithDateFormatException, 
    InvalidDataFormatException
)

class TestDataImporterExceptions(unittest.TestCase):
    def setUp(self):
        # disable logging
        logging.disable(logging.CRITICAL)

    def test_invalid_data_format_exception(self):
        exception = InvalidDataFormatException('Gross Sales', 'foo')
        self.assertEqual(exception.message, "Invalid data format in 'foo' for 'Gross Sales'.")

    def test_invalid_file_extension_exception(self):
        exception = InvalidFileExtensionException('foo.md')
        self.assertEqual(exception.message, "Invalid file extension in 'foo.md'.")

    def test_invalid_header_with_date_format_exception(self):
        exception = InvalidHeaderWithDateFormatException('2020-1Units')
        self.assertEqual(exception.message, "Invalid format in '2020-1Units' for extracting a date.")

if __name__ == '__main__':
    unittest.main()