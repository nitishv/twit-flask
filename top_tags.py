import sys
import re
import json
import string
import twitterstream

def calculate_top_tags(tweet_count, n):

	tweets = twitterstream.fetchsamples(tweet_count)
	
	n = int(n)
	tag_count = {}
	
	for line in tweets:
		tweet_dict = json.loads(line)
		if 'entities' in tweet_dict.keys():
			entities = tweet_dict['entities']
			tags = entities['hashtags']
			if len(tags) > 0:
				for tag in tags:
					word = tag['text'].encode('utf-8')
					tag_count[word] = tag_count.get(word,0) + 1

	results = []
	for key, val in sorted(tag_count.items(), key=lambda x: x[1], reverse=True)[:n]:
		results.append([key, str(val)])
		
	print results
	return results

def main():
	tweet_count = (sys.argv[1])
	#top n tags
	n = (sys.argv[2])
	calculate_top_tags(tweet_count, n)

if __name__ == '__main__':
	main()
