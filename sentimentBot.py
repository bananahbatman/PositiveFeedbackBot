#!/usr/bin/python
import praw

#Enter your correct Reddit information into the variable below

userAgent = 'Enter Bot name'

cID = 'Enter your personal use script'

cSC= 'Enter you client secret'

userN = 'Enter your Reddit username'

userP ='Enter your Reddit password'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('weather') #any subreddit you want to monitor

bot_phrase = 'Aw shucks, looks like I am staying in >:(' #phrase that the bot replies with

keywords = {'Cold', 'chicago', 'polar', 'vortex'} #makes a set of keywords to find in subreddits

for submission in subreddit.hot(limit=10): #this views the top 10 posts in that subbreddit

n_title = submission.title.lower() #makes the post title lowercase so we can compare our keywords with it.

for i in keywords: #goes through our keywords

if i in n_title: #if one of our keywords matches a title in the top 10 of the subreddit

numFound = numFound + 1

print('Bot replying to: ') #replies and outputs to the command line

print("Title: ", submission.title)

print("Text: ", submission.selftext)

print("Score: ", submission.score)

print("---------------------------------")

print('Bot saying: ', bot_phrase)

print()

submission.reply(bot_phrase)

if numFound == 0:

print()

print("Sorry, didn't find any posts with those keywords, try again!")