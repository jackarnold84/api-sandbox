import json
import sys


# testing function
def test_lambda(handler, event={}, context={}):
    result = handler(event, context)
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
    }
)
