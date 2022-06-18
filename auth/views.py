import json

from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponseRedirect
from .task import twitter_get_oauth_request_token, twitter_get_user_authorization, twitter_get_access_token, cashapp_get_user_authorization, cashapp_get_access_token


# twitter redirect user to authorize application
class InitiateTwitterAuth(APIView):

    def get(self, request):
        request_token_response = twitter_get_oauth_request_token()
        authorization_url = twitter_get_user_authorization(request_token_response)
        response = HttpResponseRedirect(redirect_to=authorization_url)
        if hasattr(request.COOKIES, "access_token"):
            response.delete_cookie('access_token')
        return response


# twitter callback generate access token
class TwitterAuthCallback(APIView):

    def get(self, request):
        oauth_token = request.query_params.get("oauth_token")
        oauth_verifier = request.query_params.get("oauth_verifier")
        access_token = twitter_get_access_token(oauth_token, oauth_verifier)
        response = HttpResponseRedirect(redirect_to=settings.NEXT_REDIRECT_URL)
        response.set_cookie('access_token', json.dumps(access_token))
        return response


class InitiateCashAppAuth(APIView):

    def get(self, request):
        authorization_url = cashapp_get_user_authorization()
        response = HttpResponseRedirect(redirect_to=authorization_url)
        if hasattr(request.COOKIES, "cashapp_access_token"):
            response.delete_cookie('cashapp_access_token')
        return response

class CashAppAuthCallback(APIView):

    def get(self, request):
        authorization_code = request.query_params.get("code")
        if authorization_code:
            authorization_response = cashapp_get_access_token(authorization_code)
            response = HttpResponseRedirect(redirect_to=settings.NEXT_REDIRECT_URL)
            response.set_cookie('cashapp_access_token', json.dumps(authorization_response))
            return response

# logout and redirect to login page
class TwitterLogOut(APIView):

    def get(self, request):
        response = HttpResponseRedirect(redirect_to=settings.NEXT_LOGIN_REDIRECT_URL)
        response.delete_cookie('access_token')
        return response




