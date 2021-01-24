import requests
import json
import kivy
from kivy.app import App
from kivy.uix.label import Label

project_token_covid = 'tTnALN6Fj0H0'
project_token_weather = 'tTjnG688Gbpg'

def covid19api():
    params = {
        "api_key": "txWWHovibbxi",
        "format": "json"
    }
    r = requests.get(f'https://www.parsehub.com/api/v2/projects/{project_token_covid}/last_ready_run/data', params=params)
    data = json.loads(r.text)
    return data

def weatherapi():
    notparams = {
        "api_key": "txWWHovibbxi",
        "format": "json" 
    }
    r2 = requests.get(f'https://www.parsehub.com/api/v2/projects/{project_token_weather}/last_ready_run/data', params=notparams)
    data2 = json.loads(r2.text)
    return data2



