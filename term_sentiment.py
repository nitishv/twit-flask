import sys
import json
import re
import string

def calculate_term_sentiment(score_file, tweet_file):
	scores = {}
	new_scores = {}
	max_score = 0
	min_score = 0
	with open(score_file) as f:
		for line in f.readlines():
			splits = line.split('\t')
			term = splits[0]
			score = int(splits[1])
			if score > max_score:
				max_score = score
			if score < min_score:
				min_score = score
			scores[term] = score

	with open(tweet_file) as f:
		for line in f.readlines():
			t_score = 0
			tweet_dict = json.loads(line)
			if 'text' in tweet_dict.keys():
				tweet_text = tweet_dict['text'].encode('utf-8')
				count_pos = 1;
				count_neg = 1;
				new_words = []
				for word in re.split('\s+', tweet_text):
					if '#' not in word:
						word = word.translate(string.maketrans("",""), string.punctuation)
					w_score = scores.get(word, 0)
					t_score = t_score + w_score
					if w_score > 0:
						count_pos = count_pos + 1
					elif w_score < 0:
						count_neg = count_neg + 1
					elif word not in scores.keys():
						if word:
							new_words.append(word)
				sentiment_score = float(count_pos)/float(count_neg)
				if (sentiment_score) > 1:
					for word in new_words:
						new_scores[word] = new_scores.get(word, 0.000) + 1*float(sentiment_score)
				elif (sentiment_score) < 1:
					for word in new_words:
						new_scores[word] = new_scores.get(word, 0.000) - 1*float(1/sentiment_score)
				else:
					for word in new_words:
						new_scores[word] = new_scores.get(word, 0.000)
	
	max_new_score = 0.000
	min_new_score = 0.000				
	for val in new_scores.values():
		if val > max_new_score:
			max_new_score = val
		elif val < min_new_score:
			min_new_score = val

	for key, val in new_scores.items():
		if val > 0:
			new_scores[key] = (val/max_new_score)*(max_score)
		elif val < 0:
			new_scores[key] = (val/min_new_score)*(min_score)


	#scores = dict(scores.items() + new_scores.items())
	for key, val in new_scores.items():
		if val != 0:
			print key + ' ' + str(val)

def main():
	score_file = (sys.argv[1])
	tweet_file = (sys.argv[2])
	hw(score_file, tweet_file)

if __name__ == '__main__':
    main()
