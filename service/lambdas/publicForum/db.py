import boto3
import time
from datetime import datetime

class PostsDB:

    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('publicForum')
        self.cached_keys = set()

    def get_posts(self):
        data = self.table.scan(
            Limit=50,
        )
        data = data['Items']
        self.cached_keys = set([x['id'] for x in data])
        return [
            {
                'timestamp': int(x['timestamp']),
                'time': str(x['time']),
                'post': str(x['post']),
            } for x in data
        ]

    def add_post(self, post):
        self.table.put_item(
            Item={
                'id': hash(post),
                'timestamp': int(time.time()),
                'time': str(datetime.now().strftime('%m-%d %H:%M')),
                'TTL': int(time.time() + 604800),
                'post': post,
            }
        )
        self.cached_keys = set()

    def is_valid_cache(self):
        data = self.table.scan(
            ProjectionExpression="id",
        )
        data = data['Items']
        keys = set([x['id'] for x in data])
        return keys == self.cached_keys
