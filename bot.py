import tweepy
import time
from datetime import datetime

now=datetime.now()
current_time=now.strftime("%H:%M:%S")

api_key="hQDIbYe8CBWJV83NFx1aWyvI3"
api_key_secret="eEGMT6XqBdHZy5680iniZVcDG2DyQ78BbTjkG8T1iknI3hkrZx"
btoken="AAAAAAAAAAAAAAAAAAAAAMUjZgEAAAAA16Y3XYIIK%2BR5%2FBjYBoxTvvRxmgA%3DTFGrGxFzYWealDToKT0W5AZOFhiTLlVD0Yg4Lf9fz3bA0Ptpam"
Atoken="1496292699372204032-ZKLEUDUPEoOG7kWIJVCF8Gi2W0oEkr"
Atoken_secret="LTuOHPFHaBS0ex7CkFS0Mie4XTfeZ5TZJpikG50wINurV"

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
