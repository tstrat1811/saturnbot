import tweepy
import time
from datetime import datetime

now=datetime.now()
current_time=now.strftime("%H:%M:%S")

# Tokens in previous commit are decomissioned

api_key="[INSERT AS STRING]"
api_key_secret="[INSERT AS STRING]"
btoken="[INSERT AS STRING]"
Atoken="[INSERT AS STRING]"
Atoken_secret="[INSERT AS STRING]"

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(Atoken,Atoken_secret)

api=tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


File_name= 'stuff.txt'

def read_log(File_name):
    file_read=open(File_name,'r')
    last_seen_id=int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_log(File_name, last_seen_id):
    file_write=open(File_name,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    for tweet in tweets:
        print(str(tweet.id)+'-'+ tweet.full_text)

        api.update_status("@"+ tweet.user.screen_name+"zoom"+"\n Your ID is:"+ str(tweet.id))
        api.create_favorite(tweet.id)
        api.retweet(tweet.id)
        store_log(File_name,tweet.id)
        time.sleep(15)

while True:
    loop=1
    tweets=api.mentions_timeline(since_id=read_log(File_name), tweet_mode='extended')
    reply()
    print(loop,"time: ", current_time)
    time.sleep(15)
    loop+=1
