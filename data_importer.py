import re

class InvalidImportException(Exception):
    pass

class DataImporter():
    PERMITTED_FILE_EXTENSIONS = [".txt", ".xlsx"]

    def load(self, file_path):
        if self.is_valid_file_extension(file_path):
            return file_path
        else:
            raise InvalidImportException

    def is_valid_file_extension(self, file_path):
        regex = re.compile(r'({})$'.format(
            '|'.join(re.escape(x) for x in self.PERMITTED_FILE_EXTENSIONS)
        ))
        return bool(regex.search(file_path))