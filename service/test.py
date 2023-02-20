import json
import sys


# testing function
def test_lambda(handler, event={}, context={}, name=''):
    result = handler(event, context)
    print('=====', name, '=====')
    if result['statusCode'] != 200:
        print(result)
        print()
    else:
        print(json.dumps(json.loads(result['body']), indent=2))
        print()


# wikiSearch
sys.path.append('service/lambdas/wikiSearch')
import lambdas.wikiSearch.lambda_function as wikiSearch

test_lambda(
    wikiSearch.lambda_handler,
    event={
        'queryStringParameters': {
            'search': 'chicago bears'
        }
    },
    name='Wiki Search',
)


# publicForum
sys.path.append('service/lambdas/publicForum')
import lambdas.publicForum.lambda_function as publicForum

test_lambda(
    publicForum.lambda_handler,
    event={
        'queryStringParameters': {
            'action': 'GET'
        }
    },
    name='Public Forum GET',
)

test_lambda(
    publicForum.lambda_handler,
    event={
        'queryStringParameters': {
            'action': 'POST',
            'post': 'I prefer pears over apples'
        }
    },
    name='Public Forum POST',
)
