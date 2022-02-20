from requests import get
from json import loads

def get_quote():
    """
    gets a random quote from the zenquote api (motivation!!!)
    """
    response = get('https://zenquotes.io/api/random')
    json_data = loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']

    return quote
