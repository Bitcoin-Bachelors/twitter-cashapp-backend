import tweepy
from django.conf import settings


# send user direct message
def send_new_direct_message(oauth_token, oauth_token_secret, message):
    try:
        auth = tweepy.OAuth1UserHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, oauth_token, oauth_token_secret)
        api = tweepy.API(auth)
        message_response = api.send_direct_message(recipient_id=message['recipient_id'],
                                                   text=message['text'])
        return message_response
    except Exception as e:
        print('Twitter Send Direct Messages - ERROR: '.format(e))


# list user direct messages
def list_user_direct_messages(oauth_token, oauth_token_secret):
    try:
        auth = tweepy.OAuth1UserHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, oauth_token, oauth_token_secret)
        api = tweepy.API(auth)
        direct_messages = api.get_direct_messages()
        return direct_messages
    except Exception as e:
        print('Twitter List Direct Messages - ERROR: '.format(e))


# get user direct message using message id
def get_user_direct_message_id(oauth_token, oauth_token_secret, message_id):
    try:
        auth = tweepy.OAuth1UserHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, oauth_token, oauth_token_secret )
        api = tweepy.API(auth)
        direct_message = api.get_direct_message(id=message_id)
        return direct_message
    except Exception as e:
        print('Twitter Get Direct Messages - ERROR: '.format(e))


# delete direct message using id
def delete_direct_message_id(oauth_token, oauth_token_secret, message_id):
    try:
        auth = tweepy.OAuth1UserHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, oauth_token, oauth_token_secret)
        api = tweepy.API(auth)
        api.delete_direct_message(id=message_id)
        return "Successfully deleted direct message"
    except Exception as e:
        print('Twitter Delete Direct Messages - ERROR: '.format(e))
