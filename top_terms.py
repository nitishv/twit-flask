import sys
import re
import json
import string
import twitterstream

def calculate_term_frequency(tweet_count, n):
	
	tweets = twitterstream.fetchsamples(tweet_count)
	
	n = int(n)
	word_count = {}
	total = 0.0

	for line in tweets:
		tweet_dict = json.loads(line)
		if 'text' in tweet_dict.keys():
			tweet_text = tweet_dict['text'].encode('utf-8')
			words = re.split('\s+', tweet_text)
			total = total + len(words)
			for word in words:
				if '#' not in word:
					word = word.translate(string.maketrans("",""), string.punctuation)
				if word:
					word_count[word] = word_count.get(word, 0) + 1
	
	for key, val in word_count.items():
		val = float(val/total)
		word_count[key] = val
		#print key, str(val)
		
	results = []
	for key, val in sorted(word_count.items(), key=lambda x: float(x[1]), reverse=True)[:n]:
		results.append([key,str(val)])

	print results
	return results
					

def main():
	tweet_count = (sys.argv[1])
	#top n frequent terms
	n = (sys.argv[2])
	calculate_term_frequency(tweet_count, n)

if __name__ == '__main__':
	main()
