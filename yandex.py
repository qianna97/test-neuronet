import requests

class YandexAPI:
    def __init__(self, apikey):
        self.apikey = apikey
    
    def get_coordinate(self, geo):
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/",
            params=dict(format="json", apikey=self.apikey, geocode=geo, lang='en_US'),
        )
        if response.status_code == 200:
            data = response.json()["response"]["GeoObjectCollection"]
            if int(data["metaDataProperty"]["GeocoderResponseMetaData"]["found"]) > 0:
                return {
                    'status_code': response.status_code,
                    'content': list(map(float, data["featureMember"][0]['GeoObject']['Point']['pos'].split(' ')))
                }
            else:
                return {
                    'status_code': 404,
                    'content': "Location is not found"
                }
        elif response.status_code == 403:
            return {
                'status_code': response.status_code,
                'content': "API Key is Invalid"
            }
        else:
            return {
                'status_code': response.status_code,
                'content': response.content
            }