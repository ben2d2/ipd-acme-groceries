import pandas as pd

class Report():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def gather_data(self):
		df = self.dataframe.sort_values(by='ImportedAt').drop_duplicates(
			subset=['SKU', 'Year', 'Month'], keep='last'
		)
		results = df[(df['Units'] != 0) & (df['Gross Sales'] != 0)].drop(columns=['ImportedAt'], axis=1)
		return results.sort_values(by=['SKU', 'Year', 'Month'])