from offerupAPI import OUSearchEngine
import time

if __name__ == '__main__':
	search = OUSearchEngine()

	# Setup your search requirments any spaces should be replace with %20
	search_items = ['Laptop', 'standing%20desk','Desktop','Cpu','Ryzen']
	
	# Setup base parameters to match your requirments
	base_params = {'q':' ',
	'lat':'38.884057',
	'lon':'-77.051286',
	'limit':'100',
	'price_max':'1000',
	'price_min':'0',
	'platform':'web',
	'delivery_param':'p',
	'radius':'50',      
	'sort':'-posted',
	}

	# Search over several different queries
	for search_item in search_items:

		# Update search parameters with the new query
		base_params['q'] = search_item

		# Build the new search url
		search.set_search_params(**base_params)
		
		# Call the api and return with the 'feed_items' section as a list
		search_results = search.request_feed_items()

		# The amount of search results
		search_count = len(search_results)

		# Grab the first item in the search results
		item = search_results[0]['item']
		print("Location: " + item['location_name'])
		print("Title: " + item['title'])
		print("Posting Time: " + item['post_date_ago'])
		print("Price: " + item['price'] + '\n')

		# Try to respect the server limits they will deny access if requests are too fast
	time.sleep(60)
