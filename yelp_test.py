#!/usr/bin/python
# coding: latin-1

import rauth
import time
import json

# def main():
# 	locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
# 	api_calls = []
# 	for lat,long in locations:
# 		params = get_search_parameters(lat,long)
# 		api_calls.append(get_results(params))
# 		#Be a good internet citizen and rate-limit yourself
# 		time.sleep(1.0)
		
	##Do other processing	

def get_yelp_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = "lm5U3-k7vQUMf8GJS15Uig"
	consumer_secret = "DjE8d2T60HpZoRhWZGnBQ-2oXJk"
	token = "WNxkDjh05BdrsJgxD_GPueAxcwp4cVq-"
	token_secret = "bNZIRIrni56M6Hjms_1fMedK9Zw"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	
	return data
		
def get_yelp_search_parameters(lat,long):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{},{}".format(str(lat),str(long))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params

# def no_unicode(object, context, maxlevels, level):
#     # """ change unicode u'foo' to string 'foo' when pretty printing"""
#     if pprint._type(object) is unicode:
#         object = str(object)
#     return pprint._safe_repr(object, context, maxlevels, level)


def formatted_json(a):
	response = json.dumps(a)
	response = json.loads(a)
	name = response ['businesses']
	# address = response ["location"]["address"]
	# phone = response ["businesse"]["display_phone"]
	# rating = response ["businesses"]["rating"]
	print name
	# print address
	# print phone
	# print rating


d = get_yelp_results(get_yelp_search_parameters(39.98,-82.98))
# print json.dumps(d, indent = 3)
key = 'businesses'
inner = d[key][0]
location_object = inner['location']

# c=location_object['address']
# print str(c)[2:-1]

print "Name =", inner['name']
print "Rating =",inner ['rating']
print "Location =", str(location_object['address'])[2:-1]

# (get_yelp_results(get_yelp_search_parameters(39.98,-82.98)), indent=4)

# if __name__=="__main__":
# 	main()
