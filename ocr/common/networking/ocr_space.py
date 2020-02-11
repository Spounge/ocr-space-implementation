import os

import requests
from requests.exceptions import HTTPError

def ocr(filename, content):
    """Calls ocr space's ocr api
    Arguments:
    filename - filename
    content  - file content as a string
    Returns:
    results  - a list of parsed text as string or a description of an
               error as first element
    """
    payload = { 'apikey': os.getenv('ocr_space_api_key') }
    response = requests.post(
        'https://api.ocr.space/parse/image',
        data = payload,
        files = { filename: content }
    )
    try:
        response.raise_for_status()
        results = [
            parsed_result['ParsedText']
                for parsed_result in response.json()['ParsedResults']
        ]
    except HTTPError as err:
        results = ['HTTP Error: {}'.format(err)]
    return results
