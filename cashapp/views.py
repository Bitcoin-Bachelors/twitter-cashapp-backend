import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .task import list_user_payments


# This will fetch users cashapp payments
class CashAppListPayments(APIView):

    def get(self, request):
        # check if cashapp access token is available in request
        if request.COOKIES['cashapp_access_token']:
            try:
                access_token = json.loads(request.COOKIES['cashapp_access_token'])
                list_response = list_user_payments(access_token)
                return Response({"messages": list_response})
            except:
                return Response("An error occured while getting cashapp payments")
        else:
            return Response("You have not linked your cashapp.")
