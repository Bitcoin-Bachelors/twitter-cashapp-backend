from django.conf import settings
from requests_oauthlib import OAuth1Session
from square.client import Client

consumer_key = settings.TWITTER_CONSUMER_KEY
consumer_secret = settings.TWITTER_CONSUMER_SECRET
twitter_oauth_api = settings.TWITTER_OAUTH_API


def twitter_get_oauth_request_token():
    # create an object of OAuth1Session
    oauth = OAuth1Session(client_key=consumer_key, client_secret=consumer_secret)
    request_token_url = str(str(twitter_oauth_api) + str("request_token"))
    fetch_response = oauth.fetch_request_token(request_token_url)
    return fetch_response


def twitter_get_user_authorization(request_token_response):
    base_authorization_url = str(str(twitter_oauth_api) + str("authorize"))
    oauth = OAuth1Session(client_key=consumer_key, client_secret=consumer_secret,
                          resource_owner_key=request_token_response['oauth_token'],
                          resource_owner_secret=request_token_response['oauth_token_secret'])
    authorization_url = oauth.authorization_url(base_authorization_url)
    return authorization_url


def twitter_get_access_token(oauth_token, verifier):
    access_token_url = str(str(twitter_oauth_api) + str("access_token"))
    oauth = OAuth1Session(client_key=consumer_key, client_secret=consumer_secret,
                          resource_owner_key=oauth_token,
                          verifier=verifier)
    access_tokens = oauth.fetch_access_token(access_token_url)
    return access_tokens


def cashapp_authenticate_application(access_token):
    client = Client(access_token=access_token, environment='sandbox')
    access_token = ""
    return access_token
