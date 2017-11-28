import os
import json
import requests
import subprocess
from datetime import datetime
import csv

account = 799407610192326
business_id = 799404736859280

# Lookalike
# curl \
#   -F 'name=My lookalike audience' \
#   -F 'subtype=LOOKALIKE' \
#   -F 'origin_audience_id=<SEED_AUDIENCE_ID>' \
#   -F 'lookalike_spec={"type":"similarity","country":"US"}' \
#   -F 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v2.11/act_<AD_ACCOUNT_ID>/customaudiences

# Website Audience
# curl 'https://graph.facebook.com/v2.11/act_799407610192326/customaudiences?access_token=EAAGNO4a7r2wBAP0cDMKBQ7yfOn6hi8zEdBp189g6Jqvars4ktNSZAPwuKmvIE1aIZB2OIRa7hHhuwZCpNw3BZCllu0NGrbUQOAXsuurpmnpcyNUQ6QgtMZB9WXBSftcz3OtoMuRJnzYiefiKdNQLtt1wPONWQHsQCleDDfYClAgZCMo85MMRIsTazKEMmmpvIZD&_business_id=799404736859280' 
# -F'pixel_id=465074777218447' 
# -F'name=Alyssa Test' 
# -F 'subtype=WEBSITE' 
# -F 'retention_days=30' 
# -F 'rule={"url":{"i_contains":"alyssapyros.com"}}' 
# -F 'prefill=1'


url_contains = input ('What do you want the URL to contain? ')
name = input ('What do you want to name your Custom Audience? ')
# influencer_name = input('Who is the Influencer? ')

def create_custom_audience (name, url_contains, account):
	base_url = "'https://graph.facebook.com/v2.11/act_{account}/customaudiences?access_token=EAAGNO4a7r2wBAP0cDMKBQ7yfOn6hi8zEdBp189g6Jqvars4ktNSZAPwuKmvIE1aIZB2OIRa7hHhuwZCpNw3BZCllu0NGrbUQOAXsuurpmnpcyNUQ6QgtMZB9WXBSftcz3OtoMuRJnzYiefiKdNQLtt1wPONWQHsQCleDDfYClAgZCMo85MMRIsTazKEMmmpvIZD&_business_id=799404736859280'".format(account=account)
	pixel_id = " -F'pixel_id=465074777218447'"
	name = " -F'name={name}'".format(name=name)
	subtype = " -F'subtype=WEBSITE'"
	rentention_days = " -F 'retention_days=30'"
	rule = {"url":{"i_contains":"{url_contains}"}}
	rule["url"]["i_contains"]=url_contains
	rule = json.dumps(rule)
	rule = " -F 'rule="+rule+"'"
	''' -F'rule={"url":{"i_contains":"{url_contains}"}}'''
	prefill = " -F'prefill=1'"
	call = base_url+pixel_id+name+subtype+rentention_days+prefill+rule
	return call

x=(create_custom_audience(name,url_contains, account))
output = subprocess.check_output('curl '+ x, shell=True)
output = json.loads(output)
# print output["id"]

def create_lookalike (pixel_id,lookalike_name, account):
	base_url = "'https://graph.facebook.com/v2.11/act_{account}/customaudiences?access_token=EAAGNO4a7r2wBAP0cDMKBQ7yfOn6hi8zEdBp189g6Jqvars4ktNSZAPwuKmvIE1aIZB2OIRa7hHhuwZCpNw3BZCllu0NGrbUQOAXsuurpmnpcyNUQ6QgtMZB9WXBSftcz3OtoMuRJnzYiefiKdNQLtt1wPONWQHsQCleDDfYClAgZCMo85MMRIsTazKEMmmpvIZD&_business_id=799404736859280'".format(account=account)
	pixel_id = " -F'origin_audience_id={pixel_id}'".format(pixel_id=pixel_id)
	name = " -F'name={lookalike_name}'".format(lookalike_name=lookalike_name)
	subtype = " -F'subtype=LOOKALIKE'"
	lookalike_spec = ''' -F 'lookalike_spec={"ratio":"0.1","country":"US"}'''
	# lookalike_spec = ''' -F 'lookalike_spec={"ratio":"0.01-0.10","country":"US"}'''
	#similarity creates the top 1% in a selected country
	lookalike_spec= lookalike_spec+"'"
	call = base_url+pixel_id+name+subtype+lookalike_spec
	return call

lookalike_name=name+' Lookalike 10% US'

y=create_lookalike(output["id"],lookalike_name, account)
# print y

output2=subprocess.check_output('curl ' + y, shell=True)
output2=json.loads(output2)
# print output2, type(output2)

print 'Your Custom Audience ID is '
print output["id"]
print 'Your Lookalike Audience ID is '
print output2["id"]

page_audience = input ('Do you want to create a Page Engagement Custom Audience? ')
if page_audience == 'yes':
	page_name = input ('What is the page name? ')

	def find_page_id(page_name):
		base_url = "'https://graph.facebook.com/v2.11/{page_name}?access_token=EAAGNO4a7r2wBAP0cDMKBQ7yfOn6hi8zEdBp189g6Jqvars4ktNSZAPwuKmvIE1aIZB2OIRa7hHhuwZCpNw3BZCllu0NGrbUQOAXsuurpmnpcyNUQ6QgtMZB9WXBSftcz3OtoMuRJnzYiefiKdNQLtt1wPONWQHsQCleDDfYClAgZCMo85MMRIsTazKEMmmpvIZD'".format(page_name=page_name)
		page_id = subprocess.check_output('curl ' + base_url, shell=True)
		page_id = json.loads(page_id)
		page_id = page_id["id"]
		return page_id

	page_id = find_page_id(page_name)


	def create_page_audience (page_audience_name, account,page_id):
		base_url = "'https://graph.facebook.com/v2.11/act_{account}/customaudiences?access_token=EAAGNO4a7r2wBAP0cDMKBQ7yfOn6hi8zEdBp189g6Jqvars4ktNSZAPwuKmvIE1aIZB2OIRa7hHhuwZCpNw3BZCllu0NGrbUQOAXsuurpmnpcyNUQ6QgtMZB9WXBSftcz3OtoMuRJnzYiefiKdNQLtt1wPONWQHsQCleDDfYClAgZCMo85MMRIsTazKEMmmpvIZD&_business_id=799404736859280'".format(account=account)
		name = " -F'name={page_audience_name}'".format(page_audience_name=page_audience_name)
		subtype = " -F'subtype=ENGAGEMENT'"
		rule = {"object_id":"{page_id}", "event_name":"page_engaged"}
		rule["object_id"]=page_id
		rule = json.dumps(rule)
		rule = " -F 'rule=["+rule+"]'"
		prefill = " -F'prefill=1'"
		call = base_url+name+subtype+prefill+rule
		return call

	page_audience_name=name+' Page Engagements'

	z=create_page_audience(page_audience_name,account,page_id)

	output3 = subprocess.check_output('curl '+ z, shell=True)
	output3 = json.loads(output3)



	print 'Your Page Engagement Audience ID is '
	print output3["id"]

# 	facebook_page = 'https://www.facebook.com/'+page_name
# 	influencer_name='test'
# 	f=open('All_Whitelisted_Influencers.csv','a')
# 	f.write([influencer_name, datetime.now(), 'yes',facebook_page,url_contains])
# 	f.close()

# else:
# 	print 'Your audiences have been created.'

