#!/usr/local/bin/python
# coding: latin-1

import requests
import commands
import urllib, json 
import pprint
import rauth
import random


def movie_recommendations ():
	# from jq import jq
	curl = '''curl 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&api-key=8c5650ca25024e509fe359b76947779a' | jq'''
	curl_output = commands.getoutput(curl)

	# nyt_movie_reviews = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&api-key=8c5650ca25024e509fe359b76947779a'
	# nytResponse = urllib.urlopen(nyt_movie_reviews)
	# nytResponse=nytResponse.read()
	# jsonResponse = json.dumps(nytResponse)
	# jsonResponse2 = json.loads(jsonResponse)
	# print nytResponse.read()


	# jsonResponse = json.loads(nytResponse.read())

	# key = 'results'
	# inner = jsonResponse[key][0]
	# print inner ['display_title']
	# print inner ['summary_short']

	# pprint.pprint(jsonResponse)


# def movie_recommendations ():
# 	nyt_movie_reviews = 'http://api.nytimes.com/svc/movies/v2/reviews/search.json?critics-pick=Y?order=by-date&api-key=8c5650ca25024e509fe359b76947779a'
# 	nytResponse = urllib.urlopen(nyt_movie_reviews)
# 	jsonResponse = json.loads(nytResponse.read())
# 	pprint.pprint(jsonResponse)

print movie_recommendations()