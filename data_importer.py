import re
import pandas as pd
from pandas.core.common import flatten
from datetime import datetime

class InvalidFileFormatException(Exception):
    pass

class InvalidFileExtensionException(Exception):
    pass

class InvalidHeaderWithDateFormatException(Exception):
    pass

class DataImporter():
    PERMITTED_FILE_EXTENSIONS = ['.txt', '.xlsx']

    FILE_EXTENSIONS_REGEX = re.compile(r'({})$'.format(
        '|'.join(re.escape(x) for x in PERMITTED_FILE_EXTENSIONS)
    ))

    MASTER_SCHEMA = ['Year','Month','SKU','Category','Units','Gross Sales']

    def load_as_dataframe_with_schema(self, file_path):
        new_rows = []
        if self.FILE_EXTENSIONS_REGEX.search(file_path):
            df = self.get_file_as_dataframe(file_path)
            for i, row in df.iterrows():
                row_as_dict = {}
                for data_tuple in row.iteritems():
                    header = data_tuple[0]
                    value = data_tuple[1]
                    if header not in ['SKU', 'Section']:
                        date_and_key_tuple = self.get_date_and_key_tuple(header)
                        date = date_and_key_tuple[0]
                        key = date_and_key_tuple[1]
                        if date not in row_as_dict:
                            year_and_month = date.split('-')
                            row_as_dict[date] = {
                                'Year': year_and_month[0],
                                'Month': year_and_month[1],
                                'SKU': row.SKU,
                                'Category': row.Section
                            }
                        row_as_dict[date][key] = value
                new_rows.append(row_as_dict.values())

            return pd.DataFrame(
                [r for row in new_rows for r in row], 
                columns=self.MASTER_SCHEMA
            )
        else:
            raise InvalidFileExtensionException

    def get_date_and_key_tuple(self, key):
        date_and_key = key.split(' ', 1)
        if len(date_and_key) == 2:
            return (date_and_key[0], date_and_key[1])
        else:
            raise InvalidHeaderWithDateFormatException

    def get_file_as_dataframe(self, file_path):
        if file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.txt'):
            return pd.read_csv(file_path, sep='\t', lineterminator='\r')