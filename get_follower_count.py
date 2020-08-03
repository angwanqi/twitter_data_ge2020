# import sys
# sys.path.append('/usr/lib/python3.6/site-packages/')
import tweepy
import time
from conf import *

# Insert your own API credentials below
# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# ACCESS_KEY = ''
# ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Peoples Voice, Singapore Democratic Alliance missing
screen_names = ['nsp_sg', 'PAPSingapore', 'ProgressSgParty', 'RedDotUnitedSG', 'thereformparty', 'yourSDP', 'SPP_SG',
                'wpsg']

party_abbrev = ['NSP', 'PAP', 'PSP', 'RDU', 'RP', 'SDP', 'SPP', 'WP']


def get_user_object(screen_name):
    return api.get_user(screen_name)


def get_follower_count(screen_name_list):
    num_of_followers = []
    user_object = []
    for name in screen_name_list:
        result = get_user_object(name)
        user_object.append(result)
        num_of_followers.append(result.followers_count)
    return num_of_followers, user_object


while True:
    follower_count, userobj = get_follower_count(screen_names)
    title = 'Follower Counts for Politcal Parties with Twitter\n'
    text = party_abbrev[0] + ': ' + str(follower_count[0]) + '\n' + \
           party_abbrev[1] + ': ' + str(follower_count[1]) + '\n' + \
           party_abbrev[2] + ': ' + str(follower_count[2]) + '\n' + \
           party_abbrev[3] + ': ' + str(follower_count[3]) + '\n' + \
           party_abbrev[4] + ': ' + str(follower_count[4]) + '\n' + \
           party_abbrev[5] + ': ' + str(follower_count[5]) + '\n' + \
           party_abbrev[6] + ': ' + str(follower_count[6]) + '\n' + \
           party_abbrev[7] + ': ' + str(follower_count[7])
    api.update_status(title + text)
    time.sleep(3600)
