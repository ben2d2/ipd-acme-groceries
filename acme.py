import os
import click
from data_importer import DataImporter
from exceptions.data_importer_exceptions import InvalidClearDataException

TO_FILE_PATH = 'master.csv'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('file_path')
def ingest(file_path):
	data_importer = DataImporter().load_and_save(file_path, TO_FILE_PATH)
	if len(data_importer) > 0:
		click.echo('Success')
	else:
		click.echo('Error')

@cli.command()
def clear_data():
	try:
		if os.path.exists(TO_FILE_PATH):
			os.remove(TO_FILE_PATH)
	except:
		raise InvalidClearDataException

if __name__ == '__main__':
    cli()