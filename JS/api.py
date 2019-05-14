import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='QKQNWWM5N0BADH4O424AV5AIEP5YONOLKYBI0ZGXNKVIGHCY',
  client_secret='OIFU2RYCGPXAM4Y2Y414VQ41W10YJZQWW3OQ3JZLQDQAVY0X',
  v='20180323',
  ll='40.7243,-74.0018',
  query='coffee',
  limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(data)