import requests
import commands
import urllib, json 
import pprint
import rauth
import random

location = input ('Where are you? ')

formatted_location = location.replace(" ", "+")
# print Google formatted_location for easy entry into URL

def get_lat (formatted_location):
	google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={l}&key=AIzaSyAuJPX-qffStexwYLYlPbgzh4v8EOAhquQ'.format(l=formatted_location)
	googleResponse = urllib.urlopen(google_maps_url)
	jsonResponse = json.loads(googleResponse.read())
	# pprint.pprint(jsonResponse)
	lat_lon = json.dumps([s['geometry']['location'] for s in jsonResponse['results']], indent=3)

	lat = json.dumps([s['geometry']['location']['lat'] for s in jsonResponse['results']], indent=3)
	
	return lat

# jsonResponse is a dictionary
# jsonResponse['results'] is a list of dictionaries
# The loop for s in jsonResponse['results'] assigns s to a dictionary for each iteration through the loop **note to self list comprehension
# s['geometry'] is a dictionary
# s['geometry']['location'] pulls out location object from the geometry object to get the latitutde/longitude

def get_lon (formatted_location):
	google_maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={l}&key=AIzaSyAuJPX-qffStexwYLYlPbgzh4v8EOAhquQ'.format(l=formatted_location)
	googleResponse = urllib.urlopen(google_maps_url)
	jsonResponse = json.loads(googleResponse.read())
	# pprint.pprint(jsonResponse)

	lon = json.dumps([s['geometry']['location']['lng'] for s in jsonResponse['results']], indent=3)
	
	return lon

latitude = get_lat(formatted_location)
longitude= get_lon(formatted_location)

len_latitude = len(latitude)
len_longitude = len(longitude)
latitude = latitude[5:(len(latitude)-2)]
longitude = longitude[5:(len(longitude)-2)]

lat=str(latitude)
lon=str(longitude)


def get_yelp_results(params):
	#Yelp keys
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

def get_yelp_groceries(lat,lon):
	#Adding search parameters
	params = {}
	params["term"] = "groceries"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"
	params["sort"] = "1"

	return params

def get_yelp_coffee(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "coffee"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"
	params["sort"] = "1"
	return params

def get_yelp_pharmacy(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "pharmacy"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"
	params["sort"] = "1"

	return params

def get_yelp_dry_cleaners(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "dry+cleaners"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"
	params["sort"] = "1"

	return params


def formatted_json(a):
	response = json.dumps(a, indent=3)
	name = response ['businesses']['name']
	address = response ['location']['address']
	phone = response ['businesses']['display_phone']
	rating = response ['businesses']['rating']
	print name
	print address
	print phone
	print rating

def pretty_print_yelp(a):
	key = 'businesses'
	inner = a[key][0]
	location_object = inner ['location']
	print "Name = ", inner ['name']
	print "Rating = ", inner ['rating']
	print "Location = ", str(location_object['address'])[2:-1]


grocery_store = get_yelp_results(get_yelp_groceries(lat,lon))
dry_cleaner = get_yelp_results(get_yelp_dry_cleaners(lat,lon))
pharmacy = get_yelp_results(get_yelp_pharmacy(lat,lon))
coffee_shop = get_yelp_results(get_yelp_coffee(lat,lon))


def get_yelp_movies(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "movies"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params


def get_yelp_restaurant_for_movie(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params


def movie_recommendations ():
	nyt_movie_reviews = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&api-key=8c5650ca25024e509fe359b76947779a'
	nytResponse = urllib.urlopen(nyt_movie_reviews)
	jsonResponse = json.loads(nytResponse.read())

	x=1

	while x < len(jsonResponse['results']):
		print 'MOVIE NAME:', jsonResponse['results'][x]['display_title']
		print 'DESCRIPTION:', jsonResponse['results'][x]['summary_short']
		x=x+1
	return x

def meetup_events(lat,lon):
	meetups_events_url = 'https://api.meetup.com/recommended/events?&key=61b2385d722d40361320a254ee45&sign=true&photo-host=public&lon={lon}&page=1&lat={lat}&radius=20'.format(lat=lat,lon=lon)
	eventsResponse = urllib.urlopen(meetups_events_url)
	jsonResponse = json.loads(eventsResponse.read())
	# pprint.pprint(jsonResponse)
	index = 0

	while index < len(jsonResponse):
		print "NAME: ", jsonResponse[index]['name']
		if 'description' in jsonResponse[index].keys():
			print "DESCRIPTION: ", jsonResponse[index]['description']
		if 'venue' in jsonResponse[index].keys():
			print "VENUE:", jsonResponse[index]['venue']['address_1']
		index +=1

def meetup_groups(lat,lon):
	meetups_groups_url = 'https://api.meetup.com/recommended/groups?&key=61b2385d722d40361320a254ee45&sign=true&photo-host=public&lon={lon}&page=1&lat={lat}&radius=20'.format(lat=lat,lon=lon)
	groupsResponse = urllib.urlopen(meetups_groups_url)
	jsonResponse = json.loads(groupsResponse.read())
	# pprint.pprint(jsonResponse)
	# print "NAME: ", jsonResponse[0]['name']
	# print "DESCRIPTION: ", jsonResponse[0]['description']
	# print "LINK:", jsonResponse[0]['link']

	index = 0
	while index < len(jsonResponse):
		print "NAME: ", jsonResponse[0]['name']
		if 'description' in jsonResponse[index].keys():
			print "DESCRIPTION: ", jsonResponse[index]['description']
		if 'link' in jsonResponse[index].keys():
			print "LINK:", jsonResponse[0]['link']	
		index +=1

def eventbrite(lat,lon):
	response = requests.get("https://www.eventbriteapi.com/v3/events/search?&sort_by=best&location.latitude={lat}&location.longitude={lon}&price=free&start_date.keyword=this_month&location.within=1mi&include_all_series_instances=0&include_unavailable_events=0".format(lat=lat,lon=lon),
	headers = {
    "Authorization": "Bearer F7ZFTGYNOYL4254AWMPX",
	},
	verify = True,  # Verify SSL certificate
	)
	print 'FREE EVENT:'
	print response.json()['events'][1]['name']['text']
	print 'TIME:'
	print response.json()['events'][1]['start']['local']
	print 'DESCRIPTION:'
	print response.json()['events'][1]['description']['text']


errands_or_activities = input ('How can I help? Please enter errands or activites ')
# asking what to return

list_of_activities = ['dinner+movies', 'meetups','events']

if errands_or_activities == 'errands':
	print 'Try these locations near you!'
	print "GROCERIES:"
	print pretty_print_yelp(grocery_store)
	print "DRY CLEANERS:"
	print pretty_print_yelp(dry_cleaner)
	print "PHARMACY:"
	print pretty_print_yelp(pharmacy)
	print "COFFEE SHOP:"
	print pretty_print_yelp(coffee_shop)

elif errands_or_activities == 'activities':

	activity_choice = input ('What are you looking to do? Please enter choose or roll the dice ')
	if activity_choice == 'roll the dice':
		activity = (random.choice(list_of_activities))
		if activity == 'dinner+movies':
			movie_theater = get_yelp_results(get_yelp_movies(lat,lon))
			dinner = get_yelp_results(get_yelp_restaurant_for_movie(lat,lon))
			print "DINNER:"
			print pretty_print_yelp(dinner)
			print "MOVIE THEATHER:"
			movie_reviews = input ('Do you want to see the critic picked movies and descriptions? ')
			if movie_reviews == 'yes':
				print "MOVIE RECOMMENDATIONS:"
				movie_recs = movie_recommendations()
				print movie_recs
			if movie_reviews == 'no':
				print 'Enjoy your movie!'
		if activity == 'meetups':
			groups = meetup_events (lat,lon)
			events = meetup_groups (lat,lon)
			print groups
			print events
		if activity == 'events':
			eventbrite = eventbrite(lat,lon)
		else:
			print 'Not valid'
	elif activity_choice == 'choose':
		chosen_activity = input ('Please choose from dinner+movies, meetups, or events ')
		if chosen_activity =='dinner+movies':
			movie_theater = get_yelp_results(get_yelp_movies(lat,lon))
			dinner = get_yelp_results(get_yelp_restaurant_for_movie(lat,lon))
			print "DINNER:"
			print pretty_print_yelp(dinner)
			print "MOVIE THEATHER:"
			print pretty_print_yelp(movie_theater)
			movie_reviews = input ('Do you want to see the critic picked movies and descriptions? ')
			if movie_reviews == 'yes':
				print "MOVIE RECOMMENDATIONS:"
				movie_recs = movie_recommendations()
				print movie_recs
			if movie_reviews == 'no':
				print 'Enjoy your movie!'
		if chosen_activity == 'meetups':
			groups = meetup_events (lat,lon)
			events = meetup_groups (lat,lon)
			print groups
			print events
		if chosen_activity == 'events':
			eventbrite = eventbrite(lat,lon)
			print eventbrite
		else:
			print 'Not valid'
	else:
		print 'Not valid entry'

