class tweet(object):
    score = ""
    id = ""
    text = ""

    def getText(self):
        return self.text

    def getID(self):
        return self.id

    def getScore(self):
        return self.score

    def __init__(self, score, id, tweet_text):
        self.score = score
        self.id = id
        self.text = tweet_text

    def __str__(self):
        tmpstr = "Score: %s | ID: %s | Text: %s" % (self.score, self.id, self.text)
        return tmpstr

    ##def make_Tweet_obj(score, id, tweet_text):
    ##   thisTweet = tweet()
    ##   thisTweet.score = score
    ##   thisTweet.id = id
    ##   thisTweet.text = tweet_text
    ##   return thisTweet
