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

#### Using setuptools implementation `acme` command
- `pip install .` to install as a package and access sub-commands with the simple command `acme`
- `acme --help` to see the list of available commands
- `acme ingest data/201904.xlsx` to import data to the application
- `acme categories` to list the available Categories for Summary
- `acme summary Produce 2018 12` to generate a Summary for the given Category, Year, and Month
- `acme generate-report foo.csv` to generate a Sales Report and save to a .csv file
- `acme reset` to delete the persistence .csv file and start fresh
- `acme exit` to delete the persistence .csv file and exit the terminal

or

#### Using `python3` command
- `python3 acme.py --help` to see the list of available commands
- `python3 acme.py ingest data/201904.xlsx` to import data to the application
- `python3 acme.py categories` to list the available Categories for Summary
- `python3 acme.py summary Produce 2018 12` to generate a Summary for the given Category, Year, and Month
- `python3 acme.py generate-report foo.csv` to generate a Sales Report and save to a .csv file
- `python3 acme.py reset` to delete the persistence .csv file and start fresh
- `python3 acme.py exit` to delete the persistence .csv file and exit the terminal



## Running Tests
`python3 -m unittest discover tests`


## Setting up a `virtualenv`
Run the following commands from your terminal and inside the app directory
- `pip install virtualenvwrapper`
- `python3 -m venv acme`
- `source acme/bin/activate`

Your virtual environment is now established