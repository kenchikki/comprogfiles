import tweepy

consumer_key = 'uedYQBlvZqcQ8JXCp9H2FmYYg'
consumer_secret = 'ovKRmvC6bmJz8AcWbCpns3WzJMW34Pgt6xqHHoDr6waMx4kZ9Y'
access_token = '1143221562738241536-a1znD1MynAJaj6PRVQlR2gDLn6gbi7'
access_token_secret = 'MKqKMS7VtNVta9oxp80S3rqRuoC2BIeGqWRwqrbL4SI6y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = input("Enter your tweet: ")

api.update_status(tweet)

print("Tweeted:", tweet)
