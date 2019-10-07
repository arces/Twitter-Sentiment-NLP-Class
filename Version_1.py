import os
import csv
import random
import time
import tweet


class Version_1:
    guess_when_unsure = False
    guess_when_neutral = False

    # Used for storing the randomly selected tweets
    tweets = []
    # Used to store the results of what our program things of the tweets
    scored_tweets = []
    # Used to store the list of positive sentiment words
    positive_words = []
    # Used to store the list of negative sentiment words
    negative_words = []

    def __init__(self):
        self.version = "1.0"

    def loadTweets(self):
        start_time = time.time()

        # Creates the positive word list
        positive_tmp = open('positive_words.txt', 'r')
        for line in positive_tmp:
            tmp = line.replace("\n", "")
            Version_1.positive_words.append(tmp)
        positive_tmp.close()

        # Createst the negative word list
        negative_tmp = open('negative_words.txt', 'r')
        for line in negative_tmp:
            tmp = line.replace("\n", "")
            Version_1.negative_words.append(tmp)
        negative_tmp.close()

        with open('NLP_Training.csv', 'r') as training_tweets:

            # Loads the CSV -> Reader -> List
            csv_temp = csv.reader(training_tweets)
            csv_list = list(csv_temp)

            # Prints the time it took to load the CSV
            timetook = time.time() - start_time
            print(f"It took {timetook} seconds to load the files")

            # Number of times to loop
            num_of_tweets = 100

            while (num_of_tweets > 0):
                # Picks a number from the full range of the tweets 0 - 1.6 Million
                random_tweet_number = random.randint(0, 1600000)
                random_tweet = csv_list[random_tweet_number]

                ##Test print function
                ##print(random_tweet[2])

                ##Makes a new tweetobject and adds it to the list of known tweets
                tweet_obj = tweet.tweet(random_tweet[0], random_tweet[1], random_tweet[2])
                # print(tweet_obj.score + tweet_obj.id + tweet_obj.text)
                Version_1.tweets.append(tweet_obj)
                num_of_tweets -= 1

        # Closes the temp tweets file
        training_tweets.close()

    # Scores the tweets and stores it in scored tweets
    def scoreTweets(self):

        for currentTweet in Version_1.tweets:
            # Gets the score for the current tweet in the Version1.tweets list
            tweetScore = Version_1.getScore(self, currentTweet.getText())

            # Makes a tmp tweet object using the new score from above
            tmpTweet = tweet.tweet(str(tweetScore), currentTweet.id, currentTweet.text)

            # Puts the tmp tweet into the scored_tweets list for later computations
            Version_1.scored_tweets.append(tmpTweet)

    # Returns one of the following: 0, 1, 2, 3, 4
    # 0 = Negative
    # 1 = Not Sure, no matches were found in the positive/negative list
    # 2 = Neutral, positive and negative was canceled out
    # 3 = NOT CURRENTLY USED
    # 4 = Positive
    def getScore(self, textInput):
        # Temp Vars for later computation
        positive_score = 0
        negative_score = 0

        # Loops throught he tweet text to see if any words are contained in the Positive Word List
        for tmpPositiveWords in Version_1.positive_words:
            if (tmpPositiveWords in textInput):
                positive_score += 1
        # Loops throught he tweet text to see if any words are contained in the Negative Word List
        for tmpNegativeWords in Version_1.negative_words:
            if (tmpNegativeWords in textInput):
                negative_score += 1

        # Final score based on the positive and negative score
        finalScore = positive_score - negative_score

        # Nothing was found from the two lists
        if positive_score == 0 and negative_score == 0:
            # If the program has to guess then it will return a positive result
            if Version_1.guess_when_unsure:
                return 4
            return 1
        # Neutral
        if finalScore == 0:
            # If the program has to guess then it will return a negative result
            if Version_1.guess_when_neutral:
                return 0
            return 2
        # Positive result
        if finalScore > 0:
            return 4
        # Negative result
        if finalScore < 0:
            return 0

    def getResults(self):
        # Our tmp vars
        totalTweets = len(Version_1.tweets)
        loopingVar = 0
        matchFound = 0
        missMatchFound = 0
        unsureFound = 0
        neutralFound = 0

        # Loops through all of the tweets in the Version1.tweets list
        for currentTweet in Version_1.tweets:

            #MAJOR DEBUG PRINT
            #print(currentTweet)
            #print(Version_1.scored_tweets[loopingVar])

            # Checks to see if a positive match is found between the labeled score and the getScore() function
            if currentTweet.score == Version_1.scored_tweets[loopingVar].score:

                matchFound += 1
            # Checks to see if nothing was found in the tweet
            elif Version_1.scored_tweets[loopingVar].score == "1":
                unsureFound += 1
            # Checks to see if a neutral score was given
            elif Version_1.scored_tweets[loopingVar].score == "2":
                neutralFound += 1
                missMatchFound += 1
            # Anything else must be a mismatch
            else:
                missMatchFound += 1

            # End of loop, add one to keep track with what number we are on
            loopingVar += 1

        # Final Print Statements
        print(
            f"Guess When Unsure is: {Version_1.guess_when_unsure} and Guess When Neutral is: {Version_1.guess_when_neutral}")
        print(f"Total Number of tweets: {totalTweets}")
        print(f"Total Number correctly identified: {matchFound} / {totalTweets} | {(matchFound / totalTweets) * 100}%")
        print(
            f"Total Number wrongly identified: {missMatchFound} / {totalTweets} | {(missMatchFound / totalTweets) * 100}%")
        print(f"Total Number neutral: {neutralFound} / {totalTweets} | {(neutralFound / totalTweets) * 100}%")
        print(f"Total Number unsure of: {unsureFound} / {totalTweets} | {(unsureFound / totalTweets) * 100}%")
        print(
            f"Total Number wrongly identified w/out neutral of: {missMatchFound - neutralFound} / {totalTweets} | {((missMatchFound - neutralFound) / totalTweets) * 100}%")


run = Version_1()
run.loadTweets()
run.scoreTweets()
run.getResults()
