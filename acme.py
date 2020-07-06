import os
import click
import pandas as pd
from data_importer import DataImporter
from summary import Summary

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
@click.argument('category')
@click.argument('year')
@click.argument('month')
def summary(category, year, month):
	dataframe = read_persistence_file()
	result = Summary(dataframe).calculate_for(category, year, month)
	click.echo(result)

@cli.command()
def clear_data():
	if os.path.exists(TO_FILE_PATH):
		os.remove(TO_FILE_PATH)
	
def read_persistence_file():
	# read from persistence file TEST_TO_FILE_PATH
	dataframe = pd.read_csv(TO_FILE_PATH, index_col=[0])
	dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])

	return dataframe

if __name__ == '__main__':
    cli()