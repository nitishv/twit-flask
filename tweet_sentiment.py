import sys
import json
import re
import string
import twitterstream

def calculate_tweet_sentiment(score_file, tweet_count, n, dir):

	tweets = twitterstream.fetch_samples(tweet_count)
	
	n = int(n)
	dir = int(dir)
	scores = {}
	results = []
	with open(score_file) as f:
		for line in f.readlines():
			splits = line.split('\t')
			term = splits[0]
			score = splits[1]
			scores[term] = int(score)

	for line in tweets:
		t_score = 0
		tweet_dict = json.loads(line)
		if 'text' in tweet_dict.keys():
			tweet_text = tweet_dict['text'].encode('utf-8')
			for word in re.split('\s+', tweet_text):
				if '#' not in word:
					word = word.translate(string.maketrans("",""), string.punctuation)
				t_score = t_score + scores.get(word, 0)
				
			if t_score != 0:
				results.append((tweet_text, t_score))
				
	topResults = []
	if dir == 1:
		for key, val in sorted(results, key=lambda x: x[1], reverse=True)[:n]:
			topResults.append([key, str(val)])
	if dir == -1:
		for key, val in sorted(results, key=lambda x: x[1])[:n]:
			topResults.append([key, str(val)])
			
	print topResults
	return topResults
	
def main():
	score_file = (sys.argv[1])
	tweet_count = (sys.argv[2])
	n = (sys.argv[3])
	# 1 for desc, -1 asc as per sentiment score
	dir = (sys.argv[4])
	calculate_tweet_sentiment(score_file, tweet_count, n, dir)

if __name__ == '__main__':
	main()
