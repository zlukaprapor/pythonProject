import tweepy
import json

# Завантажити credentials із JSON файла
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Функція доступу до API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

    # клас API надає доступ до всіх методів Twitter API
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# Створити API об'єкт
api = connect_to_twitter_OAuth()

# отримати останніх 20 твітів з власної стрічки
user_tweets = api.user_timeline()
for tweet in user_tweets:
    print(tweet.text)
