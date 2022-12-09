import pandas as pd
import re


def nr_cleaner(data_path):
    """
    This function will help with cleaning tweets by @naira_rate bot.

    Parameters
    ----------
    arg1: path
        The path for the csv file containing a csv file of the tweets. 
        Be sure to name the tweet column as "Tweet".

    Returns
    -------
    nr_dol: dataframe
        A new dataframe that contains the cleaned tweet that has extracted
        the USD rate from the tweet.
    """
    # loading the dataset
    raw_data = pd.read_csv(data_path, index_col=0)
    # setting data types
    tweet = raw_data['Tweet'].astype('string')
    date_in_dt = pd.to_datetime(raw_data['Date'])
    raw_data['Date'] = date_in_dt
    # cleaning up the tweets
    dirty_tweet = tweet.str.replace('&gt;', "").str.replace('₦', "")
    pattern = "(?:USD)  \d{3}.\d{3}"
    com_pat = re.compile(pattern)
    cleaned_tweet = dirty_tweet.apply(lambda x: com_pat.findall(x))
    raw_data['Dollar Rate'] = cleaned_tweet.explode().str[3:].astype('float')
    # returning the new dataframe
    nr_dol = raw_data[['Date', 'Dollar Rate']]
    print(nr_dol.head())
    return nr_dol

#Use case for the function
dataset = "TwitterProjects/nr_blackmarket_raw.csv" 
nr_cleaner(dataset)

#OUTPUT
"""
                       Date  Dollar Rate
0 2022-11-30 11:05:01+00:00      755.717
1 2022-11-29 11:05:01+00:00      773.201
2 2022-11-28 11:05:02+00:00      773.201
3 2022-11-27 11:05:01+00:00      773.201
4 2022-11-26 11:05:01+00:00      773.201

"""
