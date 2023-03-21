import json
from utils import response
import auth


def lambda_handler(event, context):

    # read payload
    params = event['queryStringParameters'] if 'queryStringParameters' in event else {}
    body = json.loads(event['body']) if 'body' in event else {}
    auth_body = body['auth'] if 'auth' in body else {}

    # auth
    authorized = auth.is_authorized(auth_body)
    if 'auth' in params and params['auth'] == 'checkAuth':
        return response({'authorized': authorized})
    elif 'auth' in params and params['auth'] == 'requestAuth':
        token = auth.request_authorization(auth_body)
        if token:
            return response({'authorized': True, 'authToken': token})
        else:
            return response({'authorized': False})
    elif not authorized:
        return response({'authorized': False}, status=401)

    return response(
        {
            'message': "I am going to steal the Krabby Patty formula!",
        }
    )
