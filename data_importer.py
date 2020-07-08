import re
import pandas as pd
from datetime import datetime
from exceptions.data_importer_exceptions import (
    InvalidFileExtensionException, 
    InvalidHeaderWithDateFormatException, 
    InvalidDataFormatException,
    InvalidImportException
)

class DataImporter():
    PERMITTED_FILE_EXTENSIONS = ['.txt', '.xlsx']

    FILE_EXTENSIONS_REGEX = re.compile(r'({})$'.format(
        '|'.join(re.escape(x) for x in PERMITTED_FILE_EXTENSIONS)
    ))

    MASTER_SCHEMA = ['Year','Month','SKU','Category','Units','Gross Sales','ImportedAt']

    def load_and_save(self, from_file_path, to_file_path):
        if self.FILE_EXTENSIONS_REGEX.search(from_file_path):
            df = self.get_file_as_dataframe(from_file_path).dropna()
            # collect rows for insert to persistence file
            new_df = self.handle_transformations(df)
            self.save_to(new_df, to_file_path)
            return new_df
        else:
            raise InvalidFileExtensionException(from_file_path)

    # helper methods
    def get_date_and_key_tuple(self, header):
        # expects format of '2018-12 Units'
        # will throw exception if not in this format
        date_and_key = header.split(' ', 1)
        if len(date_and_key) == 2:
            date, key = date_and_key
            return (date, key)
        else:
            raise InvalidHeaderWithDateFormatException(header)

    def get_file_as_dataframe(self, from_file_path):
        # loads the specified file formats as a pandas dataframe
        if from_file_path.endswith('.xlsx'):
            return pd.read_excel(from_file_path)
        elif from_file_path.endswith('.txt'):
            return pd.read_csv(from_file_path, sep='\t', lineterminator='\r')

    def handle_transformations(self, df):
        # pivot columns to rows and handle transformations
        new_rows = []
        for i, row in df.iterrows():
            row_as_dict = {}
            for header, value in row.iteritems():
                if header not in ['SKU', 'Section']:
                    date, key = self.get_date_and_key_tuple(header)
                    try:
                        if date not in row_as_dict:
                            row_as_dict[date] = self.init_row(date, row)
                        row_as_dict[date][key] = self.transform_value(key, value)
                    except:
                        raise InvalidDataFormatException(key, value)
            new_rows.append(row_as_dict.values())

        return pd.DataFrame(
            [r for row in new_rows for r in row], 
            columns=self.MASTER_SCHEMA
        )

    def init_row(self, date, row):
        year, month = date.split('-')
        return {
            'Year': year,
            'Month': month,
            'SKU': row.SKU,
            'Category': row.Section,
            'ImportedAt': datetime.now()
        }

    def save_to(self, dataframe, to_file_path):
        # saves the dataframe data to specified file path for a persistence layer
        try:
            with open(to_file_path, 'a') as f:
                dataframe.to_csv(f, header=f.tell()==0)
        except:
            raise InvalidImportException

    def transform_value(self, key, value):
        # handles transformation of values to either int or float  if needed
        v = value
        if key == 'Units':
            v = int(value)
        elif key == 'Gross Sales':
            v = round(float(value), 2)
        return v
        