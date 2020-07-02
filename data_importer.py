import re
import pandas as pd
from pandas.core.common import flatten
from datetime import datetime

class InvalidDataFormatException(Exception):
    pass

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
                    header, value = data_tuple
                    if header not in ['SKU', 'Section']:
                        date, key = self.get_date_and_key_tuple(header)
                        try:
                            if date not in row_as_dict:
                                year, month = date.split('-')
                                row_as_dict[date] = {
                                    'Year': year,
                                    'Month': month,
                                    'SKU': row.SKU,
                                    'Category': row.Section
                                }
                            formatted_value = 0
                            if key == 'Units':
                                formatted_value = int(value)
                            elif key == 'Gross Sales':
                                formatted_value = float(value)
                            row_as_dict[date][key] = formatted_value
                        except:
                            raise InvalidDataFormatException

                new_rows.append(row_as_dict.values())
                
            return pd.DataFrame(
                [r for row in new_rows for r in row], 
                columns=self.MASTER_SCHEMA
            )
        else:
            raise InvalidFileExtensionException

    def get_date_and_key_tuple(self, header):
        date_and_key = header.split(' ', 1)
        if len(date_and_key) == 2:
            date, key = date_and_key
            return (date, key)
        else:
            raise InvalidHeaderWithDateFormatException

    def get_file_as_dataframe(self, file_path):
        if file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)
        elif file_path.endswith('.txt'):
            return pd.read_csv(file_path, sep='\t', lineterminator='\r')