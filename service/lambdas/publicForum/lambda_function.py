from utils import response
from db import PostsDB

posts_db = PostsDB()
cached_response = None

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
        posts_db.add_post(post)

    # return list of posts
    global cached_response
    if cached_response and posts_db.is_valid_cache():
        posts_list = cached_response
    else:
        posts_list = posts_db.get_posts()
        cached_response = posts_list

    return response(
        {
            'success': True,
            'posts': posts_list,
        }
    )
