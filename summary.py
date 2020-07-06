class Summary():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def calculate_for(self, category, year, month):
		df = self.dataframe.drop_duplicates(subset=self.dataframe.columns.difference(['ImportedAt']))
		results = df[(df.Category == category) & (df.Year == year) & (df.Month == month)]
		if len(results) > 0:
			total_units = results['Units'].sum()
			total_gross_sales = results['Gross Sales'].sum()
			return "%s - Total Units: %s, Total Gross Sales: %s" % (category, total_units, total_gross_sales)
		else:
			return 'No data available'