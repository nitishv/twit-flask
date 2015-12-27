import oauth2 as oauth
import urllib2 as urllib
import sys
import os.path
import time, threading


'''
==============================================================================================
Method definitions
==============================================================================================
'''
    
'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitter_req(url, method, parameters):
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

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    url = req.to_url()
    response = opener.open(url, encoded_post_data)

    return response

def update_tweet_dump():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    
    curr_time = time.time()
    global last_update_time
    
    if (os.path.exists(file) and tweet_count != line_count(file)) or curr_time - last_update_time > tweet_dump_interval:
        response = twitter_req(url, "GET", parameters)
        count = 0
        with open(file, 'wb') as f:
            print 'Writing ' + str(tweet_count) + ' tweets to ' + file
            for line in response:
                if count < tweet_count:
                    count = count + 1
                    f.write(str(line.encode('utf-8')).strip() + '\n')
                else:
                    break
        last_update_time = curr_time
    threading.Timer(10, update_tweet_dump).start()
    
def fetch_samples(num_tweets):
    results = []
    
    global tweet_count
    global is_updater_started
    
    if is_updater_started:
        tweet_count = int(num_tweets)
    else:
        tweet_count = int(num_tweets)
        updater.start()
        is_updater_started = True

    if not os.path.exists(file) or (os.path.exists(file) and line_count(file) != tweet_count):
        print 'Tweet dump not ready yet'
        time.sleep(10)
        return results
        
    print 'Reading ' + file
    with open(file, 'rb') as f:
        for line in f.readlines():
            results.append(line)

    return results

def line_count(file):
    count = 0
    with open(file, 'rb') as f:
        count = len(f.readlines())
    return count


'''
===========================================================================================
Global
===========================================================================================
'''

tweet_count = -1
file = 'tweet_dump.txt'
# Time in secs after which the Tweet dump in asynchronously updated in background
tweet_dump_interval = 3600
last_update_time = 0
updater = threading.Thread(target=update_tweet_dump, args=())
updater.daemon = True
is_updater_started = False

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
==============================================================================================
Main
==============================================================================================
'''

if __name__ == '__main__':
    count = (sys.argv[1])
    fetch_samples(count)