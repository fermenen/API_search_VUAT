class calculate:

    @staticmethod
    def search(origin, destination, date, adults=1, children=0, babies=0):
        import Scrapper.kiwi as api_flights
        import Scrapper.bus_radar as api_bus




        data_kiwi = api_flights.kiwi_api.get_data('BCN', 'MAD', '08/07/2019')

        data_bus = api_bus.bus_radar_api.get_data(origin, destination, "2019-07-20", adults)


        return data_bus
