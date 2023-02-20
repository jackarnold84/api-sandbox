from datetime import datetime
import time
import boto3
from utils import response

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('publicForum')

def get_posts():
    data = table.scan(
        Limit=50,
    )
    data = data['Items']
    return [
        {
            'timestamp': int(x['timestamp']),
            'time': str(x['time']),
            'post': str(x['post']),
        } for x in data
    ]


def add_post(post):
    status = table.put_item(
        Item={
            'id': hash(post),
            'timestamp': int(time.time()),
            'time': str(datetime.now().strftime('%m-%d %H:%M')),
            'TTL': int(time.time()),
            'post': post,
        }
    )
    return status


def lambda_handler(event, context):

    # read query
    params = event['queryStringParameters']
    if (
        'action' not in params or
        params['action'] not in ['GET', 'POST'] or
        params['action'] == 'POST' and 'post' not in params
    ):
        return response('Invalid query parameters', status=400)

    action = params['action']

    # add new post
    if action == 'POST':
        post = params['post'].strip()
        add_post(post)

    # return list of posts
    return response(
        {
            'success': True,
            'posts': get_posts(),
        }
    )
