class kiwi_api:

    URL = 'https://api.skypicker.com'

    @staticmethod
    def get_data(originplace, destinationplace, date_from):
        import requests
        info = f'/flights?fly_from={originplace}&fly_to={destinationplace}&date_from={date_from}'

        data_url = kiwi_api.URL+info

        response = requests.get(url=data_url)
        if response.status_code == 200:
            return response.json()


