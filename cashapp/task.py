from square.client import Client
from django.conf import settings

cashapp_enviroment = settings.CASHAPP_ENVIROMENT


# list user payments
def list_user_payments(access_token):
    client = Client(access_token=access_token, environment=cashapp_enviroment)
    result = client.payments.list_payments()

    if result.is_success():
        print("[PAYMENT RESULT]", result)
        return result.body
    elif result.is_error():
        print('Cashapp List Payments - ERROR: '.format(result.body))
