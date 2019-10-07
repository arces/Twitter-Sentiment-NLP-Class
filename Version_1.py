import os
import csv
import random
import tweet
import time


class Version_1:
    tweets = []

    def __init__(self):
        self.version = "1.0"

    def loadtweets(self):
        with open('NLP_Training.csv', 'r') as training_tweets:
            start_time = time.time()
            # Loads the CSV -> Reader -> List
            csv_temp = csv.reader(training_tweets)
            csv_list = list(csv_temp)

            # Prints the time it took to load the CSV
            timetook = time.time() - start_time
            print(f"It took {timetook} seconds to load the CSV")

            # Number of times to loop
            num_of_tweets = 100

            print("Creating Tweets Objects")
            while (num_of_tweets > 0):
                # Picks a number from the full range of the tweets 0 - 1.6 Million
                random_tweet_number = random.randint(0, 1600000)
                random_tweet = csv_list[random_tweet_number]
                print(random_tweet[1])
                # print(csv_list[random_tweet_number])
                # tweet_obj = tweet(csv_temp.row['1'])
                # tweets.append()
                num_of_tweets -= 1


run = Version_1()
run.loadtweets()
