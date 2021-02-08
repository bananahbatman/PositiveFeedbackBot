#!/usr/bin/python
import praw
import secret
#Enter your correct Reddit information into the variable below

userAgent = 'PositiveFeedbackBot'

cID = secret.ID

cSC= secret.SC

userN = secret.userName

userP = secret.userPassword

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)



bot_phrase = 'You seem negative today you need to chill'

for mention in reddit.inbox.unread(limit=3):
    numFound=numFound+1
    parent = mention.parent()
    #bot_phrase = SentimentAnalysis(parent.body)
    mention.reply(bot_phrase)
    print('Bot replying to: ') #replies and outputs to the command line
    print("Title: ", mention.title)
    print("Text: ", mention.selftext)
    print("Score: ", mention.score)
    print("---------------------------------")
    print('Bot saying: ', bot_phrase)

if numFound == 0:
    print()
    print("Sorry, could not find any mentions")