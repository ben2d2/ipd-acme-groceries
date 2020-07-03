class Report():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def gather_data(self, filename):
		df = self.dataframe.drop_duplicates()
		results = df[(df['Units'] != 0) & (df['Gross Sales'] != 0)]
		return results.sort_values(by=['SKU', 'Year', 'Month'])