import requests
import json

def get_quote():
  """
  gets a random quote from the zenquote api (motivation!!!)
  """
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "\r\n - " + json_data[0]['a']
  return quote
