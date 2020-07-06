import logging

class InvalidDataFormatException(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.message = "Invalid data format in '%s' for '%s'." % (value, key)
        logging.error(self.message)
        super().__init__(self.message)

class InvalidFileExtensionException(Exception):
    def __init__(self, file_path):
        self.file_path = file_path
        self.message = "Invalid file extension in '%s'." % (file_path)
        logging.error(self.message)
        super().__init__(self.message)

class InvalidHeaderWithDateFormatException(Exception):
    def __init__(self, string):
        self.string = string
        self.message = "Invalid format in '%s' for extracting a date." % (string)
        logging.error(self.message)
        super().__init__(self.message)

class InvalidImportException(Exception):
    def __init__(self):
        self.message = "Invalid import."
        logging.error(self.message)
        super().__init__(self.message)