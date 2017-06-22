# SniffStats
Sniffstats is used parse the output obtained from using the bid_sniff page.

For example: `http://ewr-bidder-x1.mediamath.com:8081/bid_sniffer`

### Generate File to Parse
1. Use bid_sniffer to capture any stream of bid requests or responses (note, sniffstats does not work on "capture=both" outputs).
2. Copy and paste the entire output of the page into a text file.  Save the file in the same directory as sniffstats.py  
	* Be sure to use a text editor that does not add hidden characters (Sublime is a good choice, Word is a terrible choice)
	* Be sure to capture the entire output of the page.  The first few lines of the page should look like this.

Example file:

	Menu   |   Strategy   |   Campaign   |   ResourcePool   |   User   |   Configure   |   Diagnose
	Bid Request/Response Sniffer

	Supported filters: escape(pixel=ns:id|ns:id&adsize=wxh,wxh&deal=exid:dealId,exid:dealId&geo=id|id&site=domain|domain&csl=id|id)
	Use "none" to reset the filter.

	Active: false
	Capture on: Request
	Exchange: ruc
	Strategy Report Level: bid
	Max number of requests: 10000
	Number of requests captured: 10000
	Targeting filters: n/a


### Using SniffStats
SniffStats can be used in two different ways.

1. As a command line tool using the built in analysis features
2. As an imported python module


###Command line: File Analysis
Simply run following command

`python sniffstats.py –f <filename> -e <three-letter-exchange>`

This will produce an output that looks like this


```
count   pct   list_len  uniqs  variable_name
------------------------------------------------------------
6208    100%    -        -    { 
3107     50%    -     3107    { *bidid*
3107     50%    -        1    { *cur*
3107     50%    -     3107    { *id*
3107     50%    -        5    { seatbid[ 
3107     50%    3.2      -    { seatbid[ { 
3107    100%    -      129    { seatbid[ { *seat*
3107    100%    -        1    { seatbid[ { bid[ 
3107    100%    3.2      -    { seatbid[ { bid[ { 
3107    100%    -     1488    { seatbid[ { bid[ { *adid*
3107    100%    -    10082    { seatbid[ { bid[ { *adm*
3107    100%    -      594    { seatbid[ { bid[ { *cid*
3107    100%    -     1488    { seatbid[ { bid[ { *crid*
 241      7%    -       86    { seatbid[ { bid[ { *dealid*
3107    100%    -     3107    { seatbid[ { bid[ { *id*
3107    100%    -        1    { seatbid[ { bid[ { *impid*
2545     81%    -     1136    { seatbid[ { bid[ { *iurl*
3107    100%    -      631    { seatbid[ { bid[ { *price*
3107    100%    -        1    { seatbid[ { bid[ { adomain[ 
3107    100%    3.2    401    { seatbid[ { bid[ { adomain[ **
3107    100%    -        1    { seatbid[ { bid[ { attr[ 
```

The last column, shows the node in the json object that being counted.  The variable name contains the full path starting from the root node.  New child objects are denoted using `{` while list objects are denoted using `[`.  Leaf nodes, are denoted with double `*`.  In the case of the leaf node being a key-value pair, the key name is included between the `*`, for example `*seat*`.  When the leaf node is a list of values, the key between the asterisks is left empty, for example `[ **`


The first four columns give you the count, percentage, list_length, and number of uniques for each node. Note, the % value is calculated in based on the occurence the current node, divided by the occurence of the parent node (not the root node).  The easiest way to find the the parent node is to simply look for the preceeding line the ends with `{`

####Example

Here's an example on how to read the iurl line `{ seatbid[ { bid[ { *iurl*`

* The root node `{` contains a seatbid object `{ seatbid`
* The `{ seatbid` contains a list of bid objects `{ seatbid[ { bid`
* The `{ seatbid[ { bid` contains a list of objects each holding number of variables
* `{ seatbid[ { bid[ { *iurl*` is one of these variables

This variable appears 2545 times, which is 81% of the time its parent appears (the parent is `{ seatbid[ { bid[ {` which appears 3107 times).  Over those 2545 occurences we saw 631 unique values for this variables.

###Command line: Single Variable Analysis
The node descriptor produced in the File Analysis output can be reused to do an analysis on a specific variable.  To do this, simply include the `-v` parameter and the variable name.

`python sniffstats.py –f '<file_name>' –v '<variable_name>'`

In this example we'll use `–v '{ seatbid[ { bid[ { *iurl*'` from the output above.

This command produces a basic histogram of the occurance of each value of that variable.  In this example you can see that 23% of the time `*cid*=114423` 

```
count  pct  variable="{ seatbid[ { bid[ { *cid*"
------------------------------
1      0 %    197244
1      0 %    191279
1      0 %    197558
...
... (this output had 594 lines)
...
94     3 %    185449
107    3 %    189181
124    3 %    202916
151    4 %    168544
219    7 %    200751
723   23 %    114423
```


### Module Import
SniffStats is also designed to be used as a module imported into another script.  The key to using SniffStats in this way is to understand the `FILE_PROCESSOR` generator and the yielded `BID` class.

Simply use `FILE_PROCESSOR` as a generator by passing it a file name and calling it within a `for` loop.  Like so

```
import sniffstats
for bid in sniffstats.FILE_PROCESSOR('<file_name>', '<exchange>'):
```

The variable yielded is a `BID` class.  The bid contains a couple of useful methods.

* `print bid` pretty prints the bid in formatted json
* `print bid.raw` prints the raw bid request in its original form (json, url, or protobuf.textformat) 
* `bid.match('<key>')` return True/False on the existance of that key in the bid
* `bid.match('<key>','<value>')` return True/False on the existance of that key-value pair in the bid
* `bid.fetch('<key>')` returns the value associated with that key


Below is an example of how to use this module.  This script prints the url when a video bid request from youtube appears for a given ad_group.

```
import sniffstats

# use generator to parse file and yield bid objects
for bid in sniffstats.FILE_PROCESSOR('ewr_adx.txt','adx'):
	
	# key only match
	if bid.match('{ video{'):
		
		# key and value match
		if bid.match('{ adslot[ { matching_ad_data[ { adgroup_id[ **','20035004448'):

			# fetch value from key
			url = bid.fetch('{ video{ *description_url*')
			print url
```

###Exchange not in Python File:
If you open the sniffstats.py in Sublime and go to the "determine_parser" function, you can see the exchanges the file is prepared to read. If the exchange is not in that list, add it to the section based on the format it sends the bid request (JSON or URL). To add the file, use the three letter abbreviation passed in the Bid Sniffer under Exchange.



