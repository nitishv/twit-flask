import oauth2 as oauth
import urllib2 as urllib
import sys


with open('nvcmu_twitter.csv', 'rb') as f:
	api_key, api_secret, access_token_key, access_token_secret = f.readline().split(',')

api_key = api_key.strip()
api_secret = api_secret.strip()
access_token_key = access_token_key.strip()
access_token_secret = access_token_secret.strip()


_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples(tweet_count):
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  count = 0
  results = []
  tweet_count = int(tweet_count)
  file = 'tweet_dump.txt'
  
  '''
  response = twitterreq(url, "GET", parameters)
  for line in response:
	if count < tweet_count:
		count = count + 1
		print str(line.encode('utf-8')).strip()
	else:
		break
  
  
  
  response = twitterreq(url, "GET", parameters)
  with open(file, 'wb') as f:
	print 'Writing tweets to ' + file
	for line in response:
		if count < tweet_count:
			count = count + 1
			f.write(str(line.encode('utf-8')).strip() + '\n')
		else:
			break
  '''
  
  print 'Reading ' +file
  with open(file, 'rb') as f:
	for line in f.readlines():
		results.append(line)
  
  return results
  

if __name__ == '__main__':
  count = (sys.argv[1])
  fetchsamples(count)
