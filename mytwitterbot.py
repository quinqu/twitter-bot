import tweepy
import time

import config

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_KEY = config.ACCESS_KEY
ACCESS_SECRET = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
mentions = api.mentions_timeline()
file_name = 'last_tweet.txt'

def retrieveLast(fileName):
    readFile = open(fileName, 'r')
    try:
        lastSeenId= int(readFile.read().strip())
        readFile.close()
        return lastSeenId
    except Exception as e:
        print(str(e))


def storeId(lastSeenId, fileName):
    writeF = open(fileName, 'w')
    writeF.write(str(lastSeenId))
    writeF.close()
    return

def replyTweet():
    print('replying...',flush=True)
    lastSeenId = retrieveLast(file_name)

    mentions = api.mentions_timeline(lastSeenId,tweet_mode='extended')
    for i in reversed(mentions):
            print(str(i.id) + ' - ' + i.full_text, flush=True)
            lastSeen = i.id
            storeId(lastSeen, file_name)
            if '#yeet' in i.full_text.lower():
                print('found #helloworld!', flush=True)
                api.update_status('@' + i.user.screen_name +
                        '#skrrt #skrrt', i.id)

while True:
     replyTweet()
     time.sleep(10)
