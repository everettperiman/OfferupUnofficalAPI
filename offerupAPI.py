# Everett Periman 2/2/2021
import json
from urllib  import request 

class OUSearchEngine():
    # Base URL for the OU API
    base_api_url = "https://offerup.com/webapi/search/v4/feed?"

    # Default Search Parameters more details in the README
    default_params = {'q':'Laptop',
        'lat':'38.884057',
        'lon':'-77.051286',
        'limit':'100',
        'price_max':'1000',
        'price_min':'0',
        'platform':'web',
        'delivery_param':'p',
        'radius':'20',      
        'sort':'-posted',
        }

    # Default Header may be a good idea to rotate user-agents
    default_header = {'Host': 'offerup.com',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Accept-Encoding': 'deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9'}

    def __init__(self):
        # Create a search url with the default parameters
        self.set_search_params(**self.default_params)

    # Setter method used to set a new request url
    def set_search_params(self, **search_params):
        self.request_api_url = self.build_request(**search_params)

    # Verifies good parameter values and builds the request url
    def build_request(self,**search_params):
        request_string = ""
        PARAMS = {'q':'NoLimit',
        'lat':'NoLimit',
        'lon':'NoLimit',
        'limit':'NoLimit',
        'price_max':'NoLimit',
        'price_min':'NoLimit',
        'platform':'web',
        'delivery_param':['p','s','p_s'],
        'radius':['5','10','20','30','50'],      
        'sort':['-posted','posted','distance','-distance','price','-price'],
        }

        # Checks that parameters are acceptable
        for key, value in search_params.items():
            if key in PARAMS:
                if(value in PARAMS[key] or 'NoLimit' == PARAMS[key]):

                    # Add a valid parameter value to the request url
                    request_string += ("&" + key + "=" + value)
                else:
                    print(value + " Is a bad Value")
            else:
                print(key + " Is a bad Key")

        # The [1:] trims the first & from the string building process
        return self.base_api_url + request_string[1:]

    # Base method for all requests, uses the default header and request url to call
    def request_raw_feed(self):
        req = request.Request(self.request_api_url, headers=self.default_header)
        rawFeedString = request.urlopen(req).read()

        # Check for any errors with server comms
        self.check_request_status(rawFeedString)

        # Return raw string of the api response
        return rawFeedString
    
    # Checks if there were issues with server commss
    def check_request_status(self, rawFeed):
        status = json.loads(rawFeed)['status']['code']

        # 200 is a succesful server response
        if(status == '200'):
           return 1
        else:
            print('Failed request Code ' + status)
            return 0 

    # Translates the raw json feed into a python dictionary for ease of use
    def request_feed_dict(self, params=None):
        return json.loads(self.request_raw_feed())

    # Pulls just the 'feed items' section of the json dictionary
    def request_feed_items(self):
        return self.request_feed_dict()['data']['feed_items']

    # Returns the value of the server request status
    def request_feed_status(self):
        return self.request_feed_dict()['status']

    # Debug Method that prints server and location information 
    def request_vitals(self):
        data = self.request_feed_dict()
        print("Request Code :" + data['status']['code'])
        print("Location : " + data['data']['feed_options'][0]['label_short'])
        print("First Item : " + data['data']['feed_items'][0]['item']['title'])

    # Debug method that prints the first items and a few specification
    def request_example(self):
        data = self.request_feed_items()
        item = data[0]['item']
        print("Location: " + item['location_name'])
        print("Title: " + item['title'])
        print("Posting Time: " + item['post_date_ago'])
        print("Price: " + item['price'])