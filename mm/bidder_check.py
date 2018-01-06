#!/usr/bin/python 

import requests
import re
import sys, getopt

def prettyprintconfig(s):
	temp = [a.split(':') for a in s.split('\n')]
	maxlen = max( [len(key[0]) for key in temp] )
	for pair in temp[1:]:
		key = pair[0]
		try: 
			value = pair[1]
		except:
			value = ''
		spacing = ' '*(maxlen-len(key))
		print  spacing, key, ':', value


def strategy(d, s):
	url = 'http://{domain}.mediamath.com:8081/strategy?op=query&value={strategy}'.format(domain=d, strategy=s)
	r = requests.get(url)

	output = re.search('<h4>Query Strategy</h4>(.*)Placebo', r.text, re.DOTALL) 
	output = output.group(1) # grab value of q
	print output

def config(d, s):
	url = 'http://{domain}.mediamath.com:8081/config'.format(domain=d)
	r = requests.get(url)

	output = r.text
	output = output.replace('<code>','')
	output = output.replace('</code><br>','')
	output = re.search('<u>(.*'+s+'.*)</u><br>([.\s\S]+?)<br>\n<u>(?i)', output)
	print output.group(1)
	prettyprintconfig(output.group(2))

def server(d, s):
	url = 'http://{domain}.mediamath.com:8081/server?name=MMBD-MMI'.format(domain=d)
	r = requests.get(url)

	output = r.text
	output = re.search('<u>(.*'+s+'.*)</u>([.\s\S]+?)<u>(?i)', output)
	print output.group(1)
	print output.group(2)


def main(argv):
	domain = 'pao-integration-x1'
	opts, args = getopt.getopt(argv,"d:")	
	print args


	# parse inputs
	for opt, arg in opts:
		
		if opt == '-d':
			domain = arg

	if args[0] == 'strategy':
		strategy(domain, args[1])

	if args[0] == 'config':
		config(domain, args[1])

	if args[0] == 'server':
		server(domain, args[1])

if __name__ == "__main__":
   main(sys.argv[1:])
