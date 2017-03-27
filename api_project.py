import requests
import commands
import urllib, json 
import pprint
import time
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

	return params

def get_yelp_coffee(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "coffee"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params

def get_yelp_pharmacy(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "pharmacy"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params

def get_yelp_dry_cleaners(lat,lon):
	#See the Yelp API for more details
	params = {}
	params["term"] = "dry+cleaners"
	params["ll"] = "{},{}".format(str(lat),str(lon))
	params["radius_filter"] = "2000"
	params["limit"] = "1"

	return params

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
	pprint.pprint(jsonResponse)


def meetup_events(lat,lon):
	meetups_events_url = 'https://api.meetup.com/recommended/events?&key=61b2385d722d40361320a254ee45&sign=true&photo-host=public&lon={lon}&page=1&lat={lat}&radius=20'.format(lat=lat,lon=lon)
	eventsResponse = urllib.urlopen(meetups_events_url)
	jsonResponse = json.loads(eventsResponse.read())
	pprint.pprint(jsonResponse)
	
def meetup_groups(lat,lon):
	meetups_groups_url = 'https://api.meetup.com/recommended/groups?&key=61b2385d722d40361320a254ee45&sign=true&photo-host=public&lon={lon}&page=1&lat={lat}&radius=20'.format(lat=lat,lon=lon)
	groupsResponse = urllib.urlopen(meetups_groups_url)
	jsonResponse = json.loads(groupsResponse.read())
	pprint.pprint(jsonResponse)

def eventbrite(lat,lon):
	response = requests.get("https://www.eventbriteapi.com/v3/events/search?&sort_by=best&location.latitude={lat}&location.longitude={lon}&price=free&start_date.keyword=this_month&location.within=1mi&include_all_series_instances=0&include_unavailable_events=0".format(lat=lat,lon=lon),
	headers = {
    "Authorization": "Bearer F7ZFTGYNOYL4254AWMPX",
	},
	verify = True,  # Verify SSL certificate
	)
	print response.json()['events'][1]['name']['text']


chores_or_activities = input ('How can I help? Please enter chores or activites ')
# asking what to return

list_of_activities = ['dinner+movies', 'meetups','events']

if chores_or_activities == 'chores':
	print 'Try these locations near you!'
	print grocery_store
	print dry_cleaner
	print pharmacy
	print coffee_shop

elif chores_or_activities == 'activities':

	activity_choice = input ('What are you looking to do? Please enter choose or surprise ')
	if activity_choice == 'surprise':
		activity = (random.choice(list_of_activities))
		if activity == 'dinner+movies':
			movie_theater = get_yelp_results(get_yelp_movies(lat,lon))
			movie_recs = movie_recommendations()
			dinner = get_yelp_results(get_yelp_restaurant_for_movie(lat,lon))
			print dinner
			print movie_theater
			print movie_recs
		if activity == 'meetups':
			groups = meetup_events (lat,lon)
			events = meetup_groups (lat,lon)
			print groups
			print events
		if activity == 'events':
			eventbrite = eventbrite(lat,lon)
	elif activity_choice == 'choose':
		chosen_activity = input ('Please choose from movie+dinner, meetups, or events ')
		if chosen_activity =='dinner+movies':
			movie_theater = get_yelp_results(get_yelp_movies(lat,lon))
			movie_recs = movie_recommendations()
			dinner = get_yelp_results(get_yelp_restaurant_for_movie(lat,lon))
			print dinner
			print movie_theater
			print movie_recs
		if chosen_activity == 'meetups':
			groups = meetup_events (lat,lon)
			events = meetup_groups (lat,lon)
			print groups
			print events
		if chosen_activity == 'events':
			eventbrite = eventbrite(lat,lon)
			print eventbrite
	else:
		print 'Not valid entry'

