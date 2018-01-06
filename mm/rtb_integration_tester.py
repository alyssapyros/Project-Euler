import json
import commands
import re
import sys

###--------------------------------
###  PRETTY PRINTING FUNCTIONS
###--------------------------------

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def header(string):
	print '\n' + bcolors.FAIL + string + bcolors.ENDC

def highlight(string):
	print '\n' + bcolors.WARNING + string + bcolors.ENDC



###--------------------------------
###  SEND BID REQUEST
###--------------------------------

def send_br(s):
	payload  = s['bid_request']
	dc       = s['win_datacenter']
	port     = s['br_port']
	exchange = s['exchange']

	# make curl
	template_curl = '''curl -D- -X POST -H "Content-Type: application/json" -H "x-mm-debug: 3" -H "x-mm-test: 3" -H "x-openrtb-version:2.2" -d '{payload}' 'http://{dc}.mediamath.com:{port}/bid/{exchange}' '''	
	curl = template_curl.format(payload=payload, dc=dc, port=port, exchange=exchange)
	response = commands.getoutput(curl)

	highlight('calling bid request using curl')
	print curl
	# parse result
	
	# PARSE AUCTION RESULST
	try:
		mm_auction = re.search('(x-mm-auction: .*)\n', response).group(1).decode('unicode_escape')
		mm_dbg     = re.search('(x-mm-dbg: .*)\n', response).group(1).decode('unicode_escape')
		highlight('extracted debug headers from response')
		print mm_dbg
		print mm_auction
	except:
		print ' ! ERROR - could not parse response headers'
		print response
		sys.exit()
	
	# PARSE RESPOSNE
	try:
		response   = re.search('({.*)',response, re.DOTALL).group(1)
		highlight('extracted bid json from response')
	except:
		print ' ! ERROR - could not parse bid response'
		sys.exit()


	# PARSE WIN
	try: # extraction for display
		win_url	   = re.search('"adm":.*?src=.(http://.+?).><',response).group(1)
		highlight('extracted win notification from bid json')
		print win_url
		return win_url
	except:
		pass # if display doesn't work try VAST parsing next

	try: # extraction for video
		return parse_vast(response, s)
	except:
		print ' ! ERROR - count not parse win url from bid response'
		sys.exit()

###--------------------------------
###  CUSTOM PARSING FOR VIDEO
###--------------------------------

def parse_vast(response, s):
	win_price = s.get('win_price','3000')

	# exctract wrapper
	vast_wrapper = json.loads(response)['seatbid'][0]['bid'][0]['nurl']
	highlight('extracted vast wrapper from bid json')
	print vast_wrapper

	# insert price into wrapper and generate curl
	vast_wrapper = re.sub('&price=[^&]+&','&price={}&'.format(win_price), vast_wrapper)
	curl = "curl -D- '{}'".format(vast_wrapper)
	highlight('calling vast wrapper using curl (with price inserted)')
	print curl
	vast = commands.getoutput(curl)

	# extract win notification from VAST
	win = re.search('(http://.*notify.*?)]]><', vast).group(1)
	highlight('win notification extracted from vast wrapper response')
	print win
	return win

###--------------------------------
###  SEND WIN NOTIFICATION
###--------------------------------

def send_win(win, s):
	win_price = s.get('win_price','3000') # use default of 3000 unless settings has a formated price

	win = re.sub('&price=[^&]+&','&price={}&'.format(win_price), win)
	curl = "curl -D- '{}'".format(win)

	highlight('calling win notification with curl (with price inserted)')
	print curl
	response = commands.getoutput(curl)
	
###--------------------------------
###  GET STRATEGY SPEND COUNTERS
###--------------------------------

def check_strategy_counts(datacenter, strategy_id):
	# check bidder strategy summary
	if strategy_id == None:
		return 'Strategy count disabled'
	else:

		curl = '''curl 'http://{dc}.mediamath.com:8081/strategy?op=query&exch=&org=&size=&value={s}' '''.format(dc=datacenter, s=strategy_id)
		curl_output = commands.getoutput(curl)

		# parse summary for counts


		re_output = re.search('Spend \(local\):\s*(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)', curl_output) 
		counts = {	'spend' : re_output.group(1),
					'match' : re_output.group(2),
					'bids'  : re_output.group(3),
					'imps'  : re_output.group(4)}

		return counts

###--------------------------------
###  COORDINATE TESTS AND METRICS
###--------------------------------

def run_test(s):
	header('>> STARTING TEST <<')
	print json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '))
	c0 = check_strategy_counts(s['br_datacenter'], s['strategy'])
	
	win = send_br(s)
	c1 = check_strategy_counts(s['br_datacenter'], s['strategy'])

	send_win(win, s)
	c2 = check_strategy_counts(s['br_datacenter'], s['strategy'])

	highlight('stats summary')
	print c0,' << initial'
	print c1,' << after bid'
	print c2,' << after win'

###--------------------------------
###  TEST LIBRARY
###--------------------------------

improve_test1 = {
	'br_datacenter'  : 'cdg-integration-x1',
	'win_datacenter' : 'zrh-integration-x1',
	'br_port'       : '9130',
	'exchange'           : 'ipv',
	'strategy'           : '123451',
	'bid_request'		 : '''{"site":{"domain":"http://improvedigital.com","pagecat":["IAB17-39","IAB17-40"],"publisher":{"id":"671"},"id":"121485","name":"Test Site Display","page":"http://www.improvedigital.com/bannerexample"},"imp":[{"secure":0,"tagid":"835725","banner":{"h":90,"pos":1,"w":728}}],"user":{"buyeruid":"12345","id":"55abced4-1416-4cd6-9f64-ef2c28e2c9f5"},"device":{"geo":{"country":"NL"},"ua":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0","osv":"Windows_Other","ip":"46.226.57.66","devicetype":2,"os":"Windows","dnt":0,"language":"en"},"regs":{"coppa":0},"id":"1a46691f-7c94-490d-9cbf-47af9c8470fd"}'''
}

improve_test2 = {
	'br_datacenter'  : 'pao-integration-x1',
	'win_datacenter' : 'ewr-integration-x1',
	'br_port'       : '9130',
	'exchange'           : 'ipv',
	'strategy'           : '12345',
	'bid_request'		 : '''{"site":{"domain":"http://improvedigital.com","pagecat":["IAB17-39","IAB17-40"],"publisher":{"id":"671"},"id":"121485","name":"Test Site Display","page":"http://www.improvedigital.com/bannerexample"},"imp":[{"secure":0,"tagid":"835725","banner":{"h":90,"pos":1,"w":728}}],"user":{"buyeruid":"12345","id":"55abced4-1416-4cd6-9f64-ef2c28e2c9f5"},"device":{"geo":{"country":"NL"},"ua":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0","osv":"Windows_Other","ip":"46.226.57.66","devicetype":2,"os":"Windows","dnt":0,"language":"en"},"regs":{"coppa":0},"id":"1a46691f-7c94-490d-9cbf-47af9c8470fd"}'''
}

lsx_test1 = {
	'br_datacenter'  : 'pao-integration-x1',
	'win_datacenter' : 'ewr-integration-x1',
	'br_port'       : '9100',
	'exchange'           : 'lsx',
	'strategy'           : '123123123',
	'bid_request'		 : '''{"site":{"domain":"http://improvedigital.com","pagecat":["IAB17-39","IAB17-40"],"publisher":{"id":"671"},"id":"121485","name":"Test Site Display","page":"http://www.improvedigital.com/bannerexample"},"imp":[{"secure":0,"tagid":"835725","banner":{"h":90,"pos":1,"w":728}}],"user":{"buyeruid":"12345","id":"55abced4-1416-4cd6-9f64-ef2c28e2c9f5"},"device":{"geo":{"country":"NL"},"ua":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0","osv":"Windows_Other","ip":"46.226.57.66","devicetype":2,"os":"Windows","dnt":0,"language":"en"},"regs":{"coppa":0},"id":"1a46691f-7c94-490d-9cbf-47af9c8470fd"}''',
	'win_price'			 : 'NjAwMA' # NjAwMA = 6000 base64 encoded price
}

video_test1 = {
	'br_datacenter'  : 'pao-integration-x1',
	'win_datacenter' : 'ewr-integration-x1',
	'br_port'       : '9130',
	'exchange'           : 'lij',
	'strategy'           : '252528',
	'bid_request'		 : '{"id":"48","imp":[{"id":"1","video":{"mimes":["video/mp4"],"linearity":1,"minduration":5,"maxduration":15,"protocols":[2,5],"w":700,"h":450,"startdelay":0,"battr":[],"pos":1,"api":[1,2]}}],"site":{"id":"288440","page":"http://www.gentryandhutch.com","keywords":"toyota-cars-trucks-ford-chevy"},"device":{"dnt":0,"ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0","ip":"63.225.31.147","geo":{"region":"US"},"language":"en","os":"OS X","osv":"10.10"},"user":{"id":"48"},"at":2,"bcat":[]}'
}


global_deal_test1 = {
	'br_datacenter'  : 'ewr-bidder-x1',
	'win_datacenter' : 'ewr-bidder-x1',
	'br_port'        : '9200',
	'exchange'       : 'mms',
	'strategy'       :  None,
	'bid_request'	 : '{"id":"071A27202A1A19C9","imp":[{"id":"1","banner":{"w":300,"h":250,"pos":1,"topframe":1},"pmp":{"private_auction":0,"deals":[{"id":"2016081801","at":2}]}}],"site":{"id":"172833","cat":["IAB5"],"page":"http://www.answers.com/Q/What_is_hybridization_of_the_central_atom_OF2?#slide=9","ref":"https://www.google.com/","publisher":{"id":"183369","name":"Answers.com"},"content":{"keywords":"2"}},"device":{"ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36","ip":"130.160.6.57","language":"EN"},"user":{"id":"V9DHDMAoJDgAAD72fwgAAADP","buyeruid":"325a57d1-c70c-4500-a7ef-259c7b08deeb"},"ext":{"exchangeid":15,"win_price_macro":"${AUCTION_PRICE}"}}'
}

run_test(global_deal_test1)


