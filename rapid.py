import requests

from gemini import gemin
headers = { 
  "apikey": "YOUR_RAPID_API_KEY"}
k="next t20 match"
params = (
   ("q",k),
);

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);
# print(gemin(response.text))
print(response)