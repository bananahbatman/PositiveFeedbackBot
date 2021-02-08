#!/usr/bin/python
import praw

#Enter your correct Reddit information into the variable below

userAgent = 'PositiveFeedbackBot'

cID = 'Enter your personal use script'

cSC= 'Enter you client secret'

userN = 'Enter your Reddit username'

userP ='Enter your Reddit password'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

bot_phrase = 'You seem negative today you need to chill'

for mention in reddit.inbox.mentions(limit=25)
    numfound=numfound+1
    parent = mention.parent()
    #bot_phrase = SentimentAnalysis(parent.body)
    mention.reply(bot_phrase)
    print('Bot replying to: ') #replies and outputs to the command line
    print("Title: ", mention.title)
    print("Text: ", mention.selftext)
    print("Score: ", mention.score)
    print("---------------------------------")
    print('Bot saying: ', bot_phrase)
    print()

if numFound == 0:

print()

print("Sorry, didn't find any posts with those keywords, try again!")