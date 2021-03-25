import os
import json
import csv
from unidecode import unidecode
import html
import datetime as datetime

def scrap(handle):
    #create json from twitter
    userHandle = handle
    os.system('cmd /c "snscrape --jsonl twitter-user {} > tweets\\JSON\\twitter_{}.json" '.format(userHandle,userHandle))

    #read json
    data = []
    with open('tweets\\JSON\\twitter_{}.json'.format(userHandle)) as j:
        for line in j:
            data.append(json.loads(line))

    #output content in csv
    with open("tweets\\CSV\\tweet_{}.csv".format(userHandle), mode='w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['tweet']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
        for tweet in data:
            if (tweet['lang'] == 'en' 
            and tweet['media'] == None 
            and tweet['outlinks'] == [] 
            and tweet['mentionedUsers'] == None 
            and tweet['quotedTweet'] == None 
            and tweet['likeCount'] > 100):
                s = json.dumps(tweet['content'], ensure_ascii=False)
                s = html.unescape('{}'.format(s))
                s = unidecode(u'{}'.format(s))
                s = s.replace('\\n',' ').replace('\\\"','\\n').replace('\"','').replace('\\n','\"')
                writer.writerow({'tweet': s})



