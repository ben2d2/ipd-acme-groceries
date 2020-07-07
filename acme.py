import os
import signal
import click
import pandas as pd
from data_importer import DataImporter
from summary import Summary
from report import Report

TO_FILE_PATH = 'master-EHg8u63zYd.csv'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('file_path')
def ingest(file_path):
	try:
		data_importer = DataImporter().load_and_save(file_path, TO_FILE_PATH)
		click.secho('Success', fg='white', bg='blue')
	except Exception as e:
		if hasattr(e, 'message'):
			error_message = 'Error: %s' % e.message
		else:
			error_message = e
		click.secho(error_message, fg='white', bg='red')

@cli.command()
@click.argument('category')
@click.argument('year')
@click.argument('month')
def summary(category, year, month):
	dataframe = read_persistence_file()
	if len(dataframe) > 0:
		result = Summary(dataframe).calculate_for(category, year, month)
		if result == 'No data available':
			click.secho(result, bg='white', fg='blue')
		else:
			click.secho(result, fg='white', bg='blue')
	else:
		click.secho('No data has been imported. Please run the `ingest` command to import some data.', fg='white', bg='yellow')

@cli.command()
@click.argument('file_path')
def generate_report(file_path):
	dataframe = read_persistence_file()
	if len(dataframe) > 0:
		result = Report(dataframe).gather_data()
		with open(file_path, 'a') as f:
			result.to_csv(f, header=f.tell()==0)
		click.secho('File generated', fg='white', bg='blue')
	else:
		click.secho('No data has been imported. Please run the `ingest` command to import some data.', fg='white', bg='yellow')

@cli.command()
def exit():
	if os.path.exists(TO_FILE_PATH):
		os.remove(TO_FILE_PATH)
	click.secho('Good bye!', fg='white', bg='green')
	os.kill(os.getppid(), signal.SIGHUP)

@cli.command()
def clear_data():
	if os.path.exists(TO_FILE_PATH):
		os.remove(TO_FILE_PATH)
	
def read_persistence_file():
	if os.path.exists(TO_FILE_PATH):
		# read from persistence file TEST_TO_FILE_PATH
		dataframe = pd.read_csv(TO_FILE_PATH, index_col=[0])
		dataframe.set_index(['ImportedAt', 'Year', 'Month', 'Category'])

		return dataframe
	else:
		return pd.DataFrame()

if __name__ == '__main__':
    cli()