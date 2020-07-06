class Summary():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def calculate_for(self, category, year, month):
		df = self.dataframe
		results = df[
			(df.Category == category) & (df.Year == int(year)) & (df.Month == int(month))
		].sort_values(by='ImportedAt').drop_duplicates(
			subset=['SKU', 'Year', 'Month'], keep='last'
		)
		if len(results) > 0:
			total_units = results['Units'].sum()
			total_sales = results['Gross Sales'].sum()
			return "%s - Total Units: %s, Total Gross Sales: %s" % (category, total_units, total_sales)
		else:
			return 'No data available'