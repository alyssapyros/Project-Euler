import json
import sys, getopt, fnmatch

sys.path.append("protobuffer/protobuf-3.0.0a3-py2.7.egg")

# protobuf imports
from google.protobuf import text_format
#from protobuffer.google.protobuf import text_format
from protobuffer import protobuf_json
from protobuffer import adx_pb2, opx_pb2

class BID():
	def __init__(self, raw, json, flat, headers):
		self.raw  = raw
		self.json = json
		self.flat = flat
		self.headers = headers

	def match(self, key, value=None):
		for k, v in self.flat: # check all key value pairs
			if str(k).strip() == str(key).strip(): # if keys match
				if value == None:  # check if value was provided
					return True
				elif str(v) == str(value):
					return True
		return False

	def fetch(self, key):
		# to do - update fetch to grab multiple keys... or not, just use fetch twice...
		a = []
		for k,v in self.flat:
			if str(k) == str(key):
				a.append(v)

		return a

	def __str__(self):
		return json.dumps(self.json, separators=(',',':'), sort_keys=True, indent=4)


class BASE_PARSER():
	def __init__(self, filename):
		self.filename = filename
		self.prep_file()

	def prep_file(self):
		# open file
		self.file = open(self.filename, 'r')
		
		# throw out summary at top of page
		trash = self.file.readline()
		while trash.startswith('Targeting filters') == False:
			trash = self.file.readline()

	def flattener(self, node, d, prefix=''):
		# if node is a dictionary
		if type(node) == type({}):
			key = prefix + '{ '
			d.append( (key,None) )
			
			# recursion through children
			for child in node:
				next_node = node[child]
				next_key  = key + str(child)
				d = self.flattener( next_node,  d, next_key )

		# elif node is a list
		elif type(node) == type([]):
			key = prefix + '[ '
			# Realized twice independently this append adds no value
			d.append( (key,len(node)) )

			# recursion through children
			for child in node:
				next_node = child
				next_key  = key
				d = self.flattener( next_node,  d, next_key )

		# else this is a leaf
		else:
			# string manipulation, * are used so default sort does the right thing
			key = prefix.split(' ')
			key[-1] = '*' + key[-1] + '*'
			key = ' '.join(key)		
			d.append( (key,node) )
		return d

	def __iter__(self):		
		for headers, bid in self.yield_bids():
			json_bid = self.reformat_bid(bid) # convert bid to json
			flat_bid = self.flattener( json_bid, [] ) # convert json to flat
			br = BID(bid, json_bid, flat_bid, headers)
			yield br

class PROTO_PARSER(BASE_PARSER):
	def __init__(self, filename, message):
		self.message = message
		# it's probably cleaner to jsut call the inhereted __init_
		self.filename = filename
		self.prep_file()
	
	def yield_bids(self):
		# initialize self.line to the \n after the summary
		line = self.file.readline()
		record = ''

		while line !='':

			# find http headers and drop them all
			if 'HTTP/1.1' in line or fnmatch.fnmatch(line,'[????:\n'):
				header = ''
				while line != '\n' and line != '\r\n':
					line = self.file.readline()
					header += line
					if line == '':break # used to prevent looping forever with unexpected file formats
				continue

			elif line.startswith('ip:'):
				pass	# TODO : this could be reformated with quotes
			elif line.startswith('mm_'):
				pass	# TODO : this could be added into the json after the merge

	
			# throw out lines with enumerated keys due to out of date .proto files
			elif len(line.strip()) > 0 and line.strip()[0].isdigit(): # test to throw out line
				# test to throw out line or section
				if line.strip()[-1] == '{': 
					# this is the start of a whole section we need to remove
					bracket_counter = 1 # use {}s to determine what to skip
					while bracket_counter > 0:
						line = self.file.readline() # get a new line to consider
						line = line.strip()
						if len(line) > 0 and line[-1] == '}': # have to look in a specific place for } incase they're used as escape characters in urls (like opx)
							bracket_counter -= 1
						if len(line) > 0 and line[-1] == '{':
							bracket_counter += 1

						if line == '':break # used to prevent looping on end of file					
				
	

			# determine if this line ends the record
			elif line.startswith('------------------'):
				# check if record is empty and set default
				if record.strip() == '':  
					record = '{}'
				yield (header, record)
				record = ''

			# save bid string into record
			else:
				record += line
			
			line = self.file.readline()

	def reformat_bid(self, bid):
		m = self.message()
		try:
			text_format.Merge(bid, m)				
		except:
			print '! error : protobuf parsing failed, skipped bid'
		jstr = protobuf_json.pb2json(m) # should this line be inside the "try" ?  seems to work outside...
		return jstr


class URL_PARSER(BASE_PARSER):
	def yield_bids(self):
		# initialize self.line to the \n after the summary
		line = self.file.readline()
		record = ''
		while line !='':

			# find http headers and drop them all
			if 'GET' in line:
				start = line.find('?')+1
				end   = -9

				record = line[start:end]
				yield '',record # HEADERS NOT ENABLED FOR URL BECAUSE LAZY

			line = self.file.readline()

	def reformat_bid(self,bid):
		data = {}
		bid = bid.split('&')
		for keyval in bid:
			keyval = keyval.split('=')
			key = keyval[0]
			val = keyval[1]
			data[key] = val
		return data


class JSON_PARSER(BASE_PARSER):
	def reformat_bid(self, bid):
		try:
			output = json.loads(bid)
		except:
			print 'bid skipped due to parse error'
			print bid
			output = {}
		return output

	def yield_bids(self):
		# initialize self.line to the \n after the summary
		line = self.file.readline()
		record = ''

		while line !='':
			# find http headers and drop them all
			if 'HTTP/1.1' in line or fnmatch.fnmatch(line,'[????:\n'):
				headers = ''
				while line != '\n' and line != '\r\n':
					line = self.file.readline()
					headers+=line
					if line == '':break # used to prevent looping forever with unexpected file formats
				continue

			# determine if this line ends the record
			elif line.startswith('------------------'):
				# check if record is empty and set default
				if record.strip() == '':  
					record = '{}'
				yield (headers,record)
				record = ''

			# save bid string into record
			else:
				record += line
			
			line = self.file.readline()

class BOF_PARSER(BASE_PARSER):
	# override inhereted prep_file because this file didn't come from sniffstats
	def prep_file(self):
		self.file = open(self.filename, 'r')

	def yield_bids(self):
		data = json.load(self.file)
		for br in data:
			yield ('',data) # headers is ''

	def reformat_bid(self, bid):
		return bid # noop since bid is already in json




# file_processor yields json objects
class FILE_PROCESSOR():
	def __init__(self, filename, exchange):
		self.filename = filename		
		self.determine_parser(exchange)

	def determine_parser(self, exchange):
		capture  = ''

		# determine exchange and capture type
		f = open(self.filename, 'r')
		line = f.readline()
		while not line.startswith('Targeting filters') and line!='':
			if line.startswith('Exchange'):
				exchange = line[10:13].lower()
				print 'auto detected exchange =', exchange
			if line.startswith('Capture on'):
				capture = line[12:15].lower()
			line = f.readline()
		f.close()

		# TODO : fix all the protobuf stuff
		if exchange in ['sas', 'opx','liv','adt','apn','ruc','cri','swi','sxc','fbx','pub','amt','sta','max','son','cas','lij','lvi','lsx','nxg','bsw','adn','spm','yon','gen','zdx', 'btm']:
			self.parser = JSON_PARSER(self.filename)		

		elif exchange in ['ipv','ctw','atv','ads','kli']:
			self.parser = URL_PARSER(self.filename)
	
		elif exchange == 'bof':
			self.parser = BOF_PARSER(self.filename)

		# PROTOBUFF based exchanges
		elif exchange == 'adx' and capture == 'req':
		 	self.parser = PROTO_PARSER(self.filename, adx_pb2.BidRequest)
		elif exchange == 'adx' and capture == 'res':
			self.parser = PROTO_PARSER(self.filename, adx_pb2.BidResponse)

		# elif exchange == 'opx' and capture == 'req':
		# 	self.parser = PROTO_PARSER(self.filename, opx_pb2.BidRequest)
		# elif exchange == 'opx' and capture == 'res':
		# 	self.parser = PROTO_PARSER(self.filename, opx_pb2.BidResponse)


		else:
			print '\n!! ERROR: could not determine exchange or capture type from file\n'

	

	def __iter__(self):
		for br in self.parser:
		 	yield br


class ANALYZE_VARIABLE_OCCURANCE():
	def __init__(self):
		self.temp_exist = {}
		self.exist = {}
		self.count = {}
		self.value = {}

	def add_record(self, bid):
		record = bid.flat
		temp_exist = {} # a temp exist is used to ensure no more than 1 event registers per bid request

		for key,value in record:
			#print key,value
			temp_exist[key] = 1
			self.count[key] = self.count.get(key, 0) + 1
			
			# not all nodes have values
			if value != None:
				# conditional used to preven error on subsequent line
				if key not in self.value.keys():
					self.value[key] = {} 
				self.value[key][value] = 1

		# combine temp_exist into exist
		for key in temp_exist:
			self.exist[key] = self.exist.get(key, 0) + 1

 
	def pretty_print(self):
		keys = self.exist.keys()
		keys.sort()
		print 'count   pct   list_len  uniqs  variable_name'
		print '-'*60
		for k in keys:
			parent = self.find_parent(k)

			count = str( self.exist[k] )    # number of events
			occur = str( 100*self.exist[k] / self.exist[parent])+ '%'
			
			# determine if list
			test = k.strip().split(' ')
			
			if len(test)>2 and '[' in test[-2]:
				
				length = str( round(1.0 * self.count[k] / self.exist[k],1) )
			else:
				length = '-'
			
			# d only have values for leaf nodes
			if k in self.value.keys():
				divers = str( len(self.value[k].keys()) ) # how many different values we see
			else:
				divers = '-'

			print '\t'.join([count,occur,length,divers,k])

	def find_parent(self, key):
		# special handling for root
		if key == '{ ':
			return key
		else:
			# if ending in dictionary remove tailing {
			if key.strip()[-1] == '{':
				key = key[:-2]
			
			# prior dictionary is always the parent
			x = key.rfind('{')
			return key[:x+2] #+2 to catch the delimiter and the space

class ANALYZE_SINGLE_VARIABLE():
	def __init__(self, variable_name):
		self.data = {}
		self.variable_name = variable_name

	def add_record(self, bid):
		if bid.match(self.variable_name):
			value = bid.fetch(self.variable_name)
			
			# if type list, grab values out of the list
			if type(value) == type([]):
				for v in value:
					self.data[v] = self.data.get(v,0) + 1
			# if not list, just count
			else:
				self.data[value] = self.data.get(value,0) + 1

	def pretty_print(self):
		sort = sorted(self.data.items(), key=lambda x: x[1])
		total = sum(self.data.values())
		print 'count \tpercent  variable="' + self.variable_name + '"'
		print '-'*30
		for i in sort:
			print i[1], '\t', 100*i[1]/total, '%\t', i[0] 


def main(argv):
	file_name = ''
	variable_name = ''
	exchange = ''
	error_msg = 'USAGE: sniffstats.py -f <inputfile>'
	
	# get inputs from command line
	try:
		opts, args = getopt.getopt(argv,"he:f:v:")
	except getopt.GetoptError:
		print error_msg
		sys.exit(2)
	

	# parse inputs
	for opt, arg in opts:
		
		if opt == '-h':
			print 'sniffstats.py -f <inputfile>'
			sys.exit()
		
		if opt == "-f":
			file_name = arg
			
		if opt == '-e':
			exchange = arg
			print arg

		if opt == '-v':
			variable_name = arg
			

	# input validation, filename is required
	if file_name == '':
		print error_msg
		sys.exit()

	# setup analyzer	
	if variable_name == '':
		analyzer = ANALYZE_VARIABLE_OCCURANCE() 
	else:
		analyzer = ANALYZE_SINGLE_VARIABLE(variable_name)


	bid_file = FILE_PROCESSOR(file_name, exchange)
	counter = 0
	for bid in bid_file: 
		counter+=1
		if counter%100 == 0:
			print 'processed {0} bids'.format(counter)
		analyzer.add_record(bid)
	analyzer.pretty_print()

if __name__ == "__main__":
   main(sys.argv[1:])






