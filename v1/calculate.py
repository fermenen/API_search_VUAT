class calculate:

    @staticmethod
    def search(origen, destino, fecha, pasajeros):
        import Scrapper.api as api

        originplace = 'BCN'
        destinationplace = 'MAD'
        date_from = '08/07/2019'

        data_kiwi = api.kiwi_api.get_data(originplace, destinationplace, date_from)


        return  data_kiwi
