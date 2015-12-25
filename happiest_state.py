import sys
import json
import re
import string
import heapq
import twitterstream


def get_state_happiness(score_file, tweet_count):

	print 'get_state_happiness' 
	tweets = twitterstream.fetchsamples(tweet_count)
	
	print 'Tweets retrieval completed.'
	
	code_state = json.load(open('resources/us_states_code_name.json'))
	state_code = json.load(open('resources/us_states_name_code.json'))
	state_bounds = json.load(open('resources/us_states_geo_bounds.json'))
	
	scores = {}
	with open(score_file) as f:
		for line in f.readlines():
			splits = line.split('\t')
			term = splits[0]
			score = splits[1]
			scores[term] = int(score)
	
	'''
	for key in state_code.keys():
		if key not in state_bounds.keys():
			print key
	'''

	state_score = {}
	state_count = {}
	coord_count = 0 
	place_count = 0
	count = 0

	for line in tweets:
		t_score = 0
		tweet_dict = json.loads(line)
		if 'text' in tweet_dict.keys():
			tweet_text = tweet_dict['text'].encode('utf-8')
			for word in re.split('\s+', tweet_text):
				if '#' not in word:
					word = word.translate(string.maketrans('',''), string.punctuation)
				t_score = t_score + scores.get(word, 0)
	
		state_c = ''	
		if 'coordinates' in tweet_dict.keys():
			if tweet_dict['coordinates']:
				if tweet_dict['coordinates']['type'] == 'Point':
					coords = tweet_dict['coordinates']['coordinates']
					long, lat = coords
				
					for key, val in state_bounds.items():
						minlat, maxlat, minlong, maxlong = val
						if (lat > minlat) & (lat < maxlat) & (long > minlong) & (long < maxlong):
							state_c = key
							coord_count = coord_count + 1
		
		state_p = ''	
		if 'place' in tweet_dict.keys():
			place = tweet_dict['place']
			if place:
				country = place['country_code']
				if country == 'US':
					state_p = place['name'].encode('utf-8')
					if state_p not in state_code.keys():
						state_p = ''
						for word in re.split('\s+', place['full_name'].encode('utf-8')):
							word = word.translate(string.maketrans('',''), string.punctuation)
							if word in code_state.keys():
								state_p = code_state[word]
								place_count = place_count + 1
					else:
						place_count = place_count + 1
		
		state = ''
		if state_c == state_p:
			state = state_c
		elif (state_c != '') & (state_p != ''):
			state = state_p
			val = tweet_dict['coordinates']['coordinates']
			val.reverse()
			'''
			print val
			print state_c
			print state_p
			'''
		elif state_p:
			state = state_p
		elif state_c:
			state = state_c
		
		if state:
			code = state_code.get(state,'')
			if code:
				count = count + 1
				state_score[code] = state_score.get(code, 0) + t_score 
				state_count[code] = state_count.get(code, 0) + 1 
							
	'''
	print str(coord_count)
	print str(place_count)
	print str(count)
	'''
	
	h = []
	for key, val in state_score.items():
 		heapq.heappush(h, (-val, key))
	
	results = []
	for x in range(len(h)):
		val, key = heapq.heappop(h)
		state_code = key
		state_name = code_state[state_code]
		count = state_count[state_code]
		results.append([state_code, state_name, count, -val])
		
	print results
	return results
	
def main():
	score_file = (sys.argv[1])
	tweet_count = (sys.argv[2])
	get_state_happiness(score_file, tweet_count)

if __name__ == '__main__':
	main()
