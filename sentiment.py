from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))

def reply(post_string):
    score = analyzer.polarity_scores(post_string)['compound']
    if score > 0.7:
        return "Due to the sentiment analysis of your above post, we have concluded that you must be on ecstasy."
    elif score > 0.4:
        return "You're part of the 5 percent of people that are actually decent on the internet."
    elif score > 0.0:
        return "I diagnose you as only as sad as the average American worker."
    elif score > -0.4:
        return "You need to take a chill pill."
    elif score > -0.7:
        return "You're extremely negative, but don't seem to need supernatural intervention."
    else:
        return "You need Jesus."

if __name__ == '__main__':
    reply("hello!")
