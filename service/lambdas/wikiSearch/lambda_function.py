from bs4 import BeautifulSoup
import requests
import re
from utils import response

def clean_text(rgx_list, text):
    new_text = text
    for rgx in rgx_list:
        new_text = re.sub(rgx, '', new_text)
    return new_text


def lambda_handler(event, context):

    # read query
    reqired = ['search']
    if not all([x in event['queryStringParameters'] for x in reqired]):
        return response('Invalid query parameters', status=400)

    search = event['queryStringParameters']['search']
    search = search.lower().strip().replace(' ', '+')

    url = 'https://en.wikipedia.org/w/index.php?search=' + search
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')

    # get paragraph content
    p_content = [p.text.strip() for p in soup.findAll('p')]
    p_content = p_content[0: min(len(p_content), 10)]

    # check if valid search results
    for p in p_content:
        if (
            (not p_content) or
            ('no results matching the query' in p) or
            ('does not exist' in p and 'The page' in p)
        ):
            return response({'validSearchResults': False})

    # find content paragraphs (first 2)
    summary = []
    for i in range(len(p_content) - 1):
        if len(p_content[i]) > 200:
            summary.append(p_content[i])
            if len(p_content[i + 1]) > 200:
                summary.append(p_content[i + 1])
            break

    if not summary:
        return response({'validSearch': False})

    # clean text
    for i in range(len(summary)):
        summary[i] = clean_text(
            [r'\[\d*\]', r'/ʃ\w*/', r'\(listen\)'],
            summary[i]
        )
        summary[i] = summary[i].replace('  ', ' ').replace('( ', '(')

    return response(
        {
            'validSearch': True,
            'summary': summary,
        }
    )
