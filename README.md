# OfferupUnofficalAPI
Unofficial API for the ecommerce site Offerup
This is an unoffical api and is to be used at your own risk.

Intro
	The example.py is included to introduce the api tool, its a very simple tool and is open to further improvements and optimizations
	I would strongly recommend using http://jsonviewer.stack.hu/ or another json viewer to figure out the most useful information
	Included is an example response from the website for easy review but you can get your own request by saving a request_raw_feed() output
	
Tips
	Try to limit API calls to > 1s, they will block your requests if they are too fast
	Would recommend using a library such as geopy to automate the searching of lat and lon values
	Geopy .lat and .lon attributes plug and play directly into the search params

	When building the search parameters the table below has acceptable values
	# Options
	# radius=x: 5, 10, 20, 30, 50
	# price_min=x: 0->inf
	# price_max=x: 0->inf
	# q=x: any strings with % to signify spaces
	# delivery_param=x: p for pickup, s for shipping, p_s for both
	# limit=x: 10 default, range limit set on the api side at ~400
	# lat=x: 28.5417016 
	# lon=x: -81.2408689
	# sort=x: Newest -posted, Oldest posted, Closest distance, LowToHigh price, HighToLow -price
	
	request_vitals() is useful to ensure that your search parameters are set correctly
	request_example() is useful to confirm that you are getting acceptable search results