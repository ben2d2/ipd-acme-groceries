import pandas as pd
import logging

class Report():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def gather_data(self):
		try:
			df = self.dataframe.sort_values(by='ImportedAt').drop_duplicates(
				subset=['SKU', 'Year', 'Month'], keep='last'
			)
			results = df[(df['Units'] != 0) & (df['Gross Sales'] != 0)].drop(columns=['ImportedAt'], axis=1)
			return results.sort_values(by=['SKU', 'Year', 'Month'])
		except Exception as error:
			logging.error(error)
			raise error