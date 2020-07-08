import logging

class Summary():
	def __init__(self, dataframe):
		self.dataframe = dataframe

	def calculate_for(self, category, year, month):
		try:
			df = self.dataframe
			if category == 'ALL':
				aggregations = {
				    'Units':'sum',
				    'Gross Sales':'sum'
				}
				results = df[
					(df.Year == int(year)) & (df.Month == int(month))
				].sort_values(by=['ImportedAt', 'Category']).drop_duplicates(
					subset=['SKU', 'Year', 'Month'], keep='last'
				).groupby('Category').agg(aggregations)
				return results
			else:
				results = df[
					(df.Category == category) & (df.Year == int(year)) & (df.Month == int(month))
				].sort_values(by='ImportedAt').drop_duplicates(
					subset=['SKU', 'Year', 'Month'], keep='last'
				)
				if len(results) > 0:
					total_units = results['Units'].sum()
					total_sales = round(results['Gross Sales'].sum(), 2)
					return "%s - Total Units: %s, Total Gross Sales: %s" % (category, total_units, total_sales)
				else:
					return 'No data available'
		except Exception as error:
			logging.error(error)
			raise error