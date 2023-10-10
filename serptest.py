from serpapi import GoogleSearch
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json

params = {
  "api_key": "replace this with your api key to make it work",
  'engine': 'google_trends',				# SerpApi search engine	
	'date': 'today 12-m',					# by default Past 12 months
	'cat': 0,								# by default All categories
	# 'geo': '',							# by default Worldwide
	# 'gprop': 'images',					# by default Web Search
	# 'data_type': '',						# type of search (defined in the function)
	# 'q': '',								# query (defined in the function)
}

# search = GoogleSearch(params)
# ##SERPAPI results are stored in a dictionary
# results = search.get_dict()
# ##check intial dictionary
# df = pd.DataFrame.from_dict(results)
# df.to_csv('trends.csv',index=False)
# ##homing in on dictionary of interest
# test = results['interest_over_time']
# df2 =pd.DataFrame.from_dict(test)
# df2.to_csv('trends2.csv',index=False)
# for value in test.values():
#     print(value)

def scrape_google_trends(data_type: str, key: str, query: str):
	params['data_type'] = data_type
	params['q'] = query
	
	search = GoogleSearch(params)           # where data extraction happens on the SerpApi backend
	results = search.get_dict()         	# JSON -> Python dict
	## check results here later 
	return results 


def get_all_data():
	data = {
		'interest_over_time': {},
		'compared_breakdown_by_region': [],
		'interest_by_region': [],
		'related_topics': {},
		'related_queries': {}
	}

	interest_over_time = scrape_google_trends('TIMESERIES', 'interest_over_time', 'Mercedes,BMW,Audi')
	data['interest_over_time'] = interest_over_time

	compared_breakdown_by_region = scrape_google_trends('GEO_MAP', 'compared_breakdown_by_region', 'Mercedes,BMW,Audi')
	data['compared_breakdown_by_region'] = compared_breakdown_by_region

	interest_by_region = scrape_google_trends('GEO_MAP_0', 'interest_by_region', 'Mercedes')
	data['interest_by_region'] = interest_by_region

	related_topics = scrape_google_trends('RELATED_TOPICS', 'related_topics', 'Mercedes')
	data['related_topics'] = related_topics

	related_queries = scrape_google_trends('RELATED_QUERIES', 'related_queries', 'Mercedes')
	data['related_queries'] = related_queries

	return data


def plot_interest_over_time(data: dict):
	timeseries = []

	# Extracting data
	for result in data['interest_over_time']['timeline_data']:
		for value in result['values']:
			query = value['query']
			extracted_value = value['extracted_value']
			
			timeseries.append({
				'timestamp': result['timestamp'],
				'query': query,
				'extracted_value': extracted_value,
			})


if __name__ == "__main__":
	google_trends_result = get_all_data()
	df3 =pd.DataFrame.from_dict(google_trends_result)
	df3.to_csv('trends3.csv',index=False)
	print(json.dumps(google_trends_result, indent=2, ensure_ascii=False))
