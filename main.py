import requests
import json
import kivy 
from kivy.app import App 
from kivy.uix.label import Label 

params = {
  "api_key": "txWWHovibbxi",
  "format": "json"
}
r = requests.get('https://www.parsehub.com/api/v2/projects/tTnALN6Fj0H0/last_ready_run/data', params=params)

Country = input('enter country ')

data = json.loads(r.text)

for content in data['Country']:
  if content['name'] == Country:
    print(content)
