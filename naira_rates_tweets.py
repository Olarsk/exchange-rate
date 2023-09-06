import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "-crypto (from:naira_rates) until:2022-12-01 since:2022-01-01"
tweets = []
limit = 1000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'Username', 'Tweet'])
df.to_csv('raw_exchange_rate.csv')
# print(df.head())
