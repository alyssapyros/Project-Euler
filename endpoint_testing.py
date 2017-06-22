import requests


def highlight(string):
	WARNING = '\033[93m'
	ENDC = '\033[0m'
	print WARNING + string + ENDC,

url  = 'http://us-east-bidder.mathtag.com:9180/bid/gor'

data = '''
{"id":"48a6666792dc1ebfb68f8fb16aaa7bb5e6f0cccf","at":2,"tmax":120,"ext.ssp":"SelfService37","wseat":["101338"],"imp":[{"id":"1","tagid":"30174","instl":0,"video":{"mimes":["video/mp4","video/flv","audio/mpeg","audio/x-ms-wma","audio/aac","audio/ogg","audio/mp4","audio/vnd.wav"],"linearity":1,"pos":0,"minduration":0,"maxduration":30,"startdelay":0,"protocol":5,"battr":[],"playbackmethod":[3],"api":[1],"companiontype":[1,2],"companionad":[{"w":300,"h":250}]},"pmp":{"private_auction":1,"deals":[{"id":"90ad65e6-e9f0-4e89-9be6-ad78235d137f","bidfloor":2.5,"bidfloorcur":"USD","at":2,"wseat":["101338"]}]}}],"site":{"id":"12345","name":"Example Site","domain":"example.com","cat":["IAB1-1","IAB1-3"],"page":"http://www.example.com/foo?bar=1","publisher":{"id":"67890"},"content":{"language":"en"}},"device":{"ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4","ip":"192.168.1.10","geo":{"country":"NLD","region":"NB","type":2},"language":"en","js":1,"devicetype":2},"user":{"id":"fe845197532eb8b02a11a1576b12e7957ab7d26f","buyeruid":"2761F376-7D7A-472A-8392-0735FF36F74C"}}
'''

headers = {	"Content-Type": "application/json",
			"x-mm-debug"  : "3",
			"x-mm-test": "3"}


r = requests.post(url, data, headers=headers)

headers_to_print = ['x-mm-latency', 'x-mm-dbg', 'x-mm-host', 'x-mm-auction']
for h in headers_to_print:
	highlight(h+':'),
	print r.headers[h].decode('unicode_escape')

highlight('response body:')
print r.text
