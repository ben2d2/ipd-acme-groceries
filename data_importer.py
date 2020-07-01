import re

class InvalidImportException(Exception):
    pass

class DataImporter():
    PERMITTED_FILE_EXTENSIONS = [".txt", ".xlsx"]

    FILE_EXTENSIONS_REGEX = re.compile(r'({})$'.format(
        '|'.join(re.escape(x) for x in PERMITTED_FILE_EXTENSIONS)
    ))

    def load(self, file_path):
        if self.is_valid_file_extension(file_path):
            return file_path
        else:
            raise InvalidImportException

    def is_valid_file_extension(self, file_path):
        return bool(self.FILE_EXTENSIONS_REGEX.search(file_path))