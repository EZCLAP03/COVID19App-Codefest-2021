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


weather = ''
if Country == 'India':
    weather = "Bangalore"

response = requests.get('http://api.openweathermap.org/data/2.5/weather?appid=4af162d6114fcf57f692885c1ba40863&q=' + weather)
CountryWeather = response.json()
print(CountryWeather)
