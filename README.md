# Acme Groceries Sales Analysis Application
This project is a python command line application designed to ingest data/reports and generate sales analysis reports.

## Business Requirements
Build an application to ingest monthly reports, generate sales summaries by category and output consolidated reports.

See the [Requirements Document](description.pdf) for full details.

Use the files provided below:

[data/201904.xlsx](https://github.com/ben2d2/ipd-acme-groceries/blob/master/data/201904.xlsx)

[data/201905.txt](https://github.com/ben2d2/ipd-acme-groceries/blob/master/data/201905.txt)

## Technical Requirements
- python3
- pip
- [pandas](https://pandas.pydata.org/)
- [click](https://click.palletsprojects.com/en/7.x/)

Check out the [requirements.txt](requirements.txt) to find supporting python package requirements

## Installation
Download or clone this repo to your preferred workspace directory

`git clone git@github.com:ben2d2/ipd-acme-groceries.git`

## Running the App
- From your terminal cd into the app directory
- Create a virtualenv if you so please or ensure python3 is you default python version
- `pip install -r requirements.txt`

#### Using setuptools implementation
- `pip install .` to access the app from your terminal with the simple command `acme`
- `acme --help` to see the list of available commands
- `acme ingest data/201904.xlsx` to import data to the application
- `acme summary Produce 2018 12` to generate a Summary for the given Category, Year, and Month
- `acme generate-report foo.csv` to generate a Sales Report and save to a .csv file
- `acme clear-data` to delete the persistence .csv file and start fresh

or

#### Using `python` command
- `python acme.py --help` to see the list of available commands
- `python acme.py ingest data/201904.xlsx` to import data to the application
- `python acme.py summary Produce 2018 12` to generate a Summary for the given Category, Year, and Month
- `python acme.py generate-report foo.csv` to generate a Sales Report and save to a .csv file
- `python acme.py clear-data` to delete the persistence .csv file and start fresh


## Running Tests
`python -m unittest discover tests`