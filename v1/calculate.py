class calculate:

    @staticmethod
    def search(origen, destino, fecha, pasajeros):
        import Scrapper.kiwi as api_flights
        import Scrapper.bus_radar as api_bus

        originplace = 'BCN'
        destinationplace = 'MAD'
        date_from = '08/07/2019'

        data_kiwi = api_flights.kiwi_api.get_data(originplace, destinationplace, date_from)

        data_bus = api_bus.bus_radar_api.get_data("Oviedo", "Madrid", "2019-07-10")

        return data_bus
