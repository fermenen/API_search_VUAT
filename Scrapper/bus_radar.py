class bus_radar_api:

    URL = 'https://www.busliniensuche.de/api2/search/connections'
    SESSION = '0cd66ad5-1990-4896-8677-c811928de9a5'
    LANGUAGE = 'es'
    CURRENCY = 'EUR'

    @staticmethod
    def get_data(originplace, destinationplace, date_from):
        import requests
        import json

        headers = {
            'Cookie': f'session_id={bus_radar_api.SESSION}',
            'Accept-Language': bus_radar_api.LANGUAGE,
            'X-Language': bus_radar_api.LANGUAGE,
            'Accept-Currency': bus_radar_api.CURRENCY,
            'Content-Type':	'application/json; charset=utf-8',

        }
        data = r'''{
            "allTransports": true,
            "allowDeletion": true,
            "allowFerry": true,
            "allowFlight": true,
            "allowStored": true,
            "flexibility": 0,
            "from": "{originplace}" ,
            "passengers": 1,
            "radius": 15000,
            "to": "{destinationplace}" ,
            "visibilityUpdates": 2,
            "when": "{date_from}"
            }'''

        data = data.replace('{originplace}', originplace)
        data = data.replace('{destinationplace}', destinationplace)
        data = data.replace('{date_from}', date_from)

        response = requests.post(url=bus_radar_api.URL, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()


