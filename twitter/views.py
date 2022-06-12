import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from .task import list_user_direct_messages, get_user_direct_message_id, delete_direct_message_id, \
    send_new_direct_message


# This will fetch only direct messages that are 30 days old
class TwitterDirectMessageListView(APIView):

    def get(self, request):
        # check if access token is available in request
        # if not available send user to login page.
        if request.COOKIES['access_token']:
            try:
                oauth_token = json.loads(request.COOKIES['access_token'])['oauth_token']
                oauth_token_secret = json.loads(request.COOKIES['access_token'])['oauth_token_secret']
                list_response = list_user_direct_messages(oauth_token, oauth_token_secret)
                handle_response = self.handle_direct_message_list(list_response)
                return Response({"messages": handle_response})
            except:
                return Response("An error occured while getting direct message")
        else:
            return HttpResponseRedirect(redirect_to=settings.NEXT_LOGIN_REDIRECT_URL)

    def handle_direct_message_list(self, messages):
        response_array = []
        for message in messages:
            response_array.append({"message": message._json})
        return response_array


# get direct message using the message
class TwitterDirectMessageGetView(APIView):

    def get(self, request):
        # check if access token is available in request
        # if not available send user to login page
        message_id = request.query_params.get("message_id")
        if request.COOKIES['access_token']:
            if message_id:
                try:
                    oauth_token = json.loads(request.COOKIES['access_token'])['oauth_token']
                    oauth_token_secret = json.loads(request.COOKIES['access_token'])['oauth_token_secret']
                    direct_message_response = get_user_direct_message_id(oauth_token, oauth_token_secret, message_id)
                    return Response(direct_message_response._json)
                except:
                    return Response("An error occured while getting direct message")
            else:
                return Response("Please provide message id in your request")
        else:
            return HttpResponseRedirect(redirect_to=settings.NEXT_LOGIN_REDIRECT_URL)


# delete direct messages
class TwitterDirectMessageSendView(APIView):

    def post(self, request):
        message = json.loads(request.body)
        # check if access token is available in request
        # if not available send user to login page
        if request.COOKIES['access_token']:
            if message:
                try:
                    oauth_token = json.loads(request.COOKIES['access_token'])['oauth_token']
                    oauth_token_secret = json.loads(request.COOKIES['access_token'])['oauth_token_secret']
                    message_response = send_new_direct_message(oauth_token, oauth_token_secret, message)
                    print(message_response)
                    return Response(message_response._json)
                except:
                    return Response("An error occured while sending direct message")
            else:
                return Response("Please provide message content and recipient id")
        else:
            return HttpResponseRedirect(redirect_to=settings.NEXT_LOGIN_REDIRECT_URL)


class TwitterDirectMessageRemoveView(APIView):

    def delete(self, request):
        message_id = request.query_params.get("message_id")
        # check if access token is available in request
        # if not available send user to login page
        if request.COOKIES['access_token']:
            if message_id:
                try:
                    oauth_token = json.loads(request.COOKIES['access_token'])['oauth_token']
                    oauth_token_secret = json.loads(request.COOKIES['access_token'])['oauth_token_secret']
                    delete_direct_message_id(oauth_token, oauth_token_secret, message_id)
                    return Response("Successfully deleted direct message")
                except:
                    return Response("An error occured while deleting direct message")
            else:
                return Response("Please provide message id in your request")
        else:
            return HttpResponseRedirect(redirect_to=settings.NEXT_LOGIN_REDIRECT_URL)
