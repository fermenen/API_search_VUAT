class calculate:

    @staticmethod
    def search(origen, destino, fecha, pasajeros):
        import Scrapper.api as api
        results = {}

        country = 'ES'
        currency = 'EUR'
        locale = 'es-ES'
        originplace = 'MAD-sky'
        destinationplace = 'SVQ-sky'
        outboundpartialdate = '2019-07-09'
        inboundpartialdate = ''

        results = api.Skyscanner.get_data(country, currency, locale, originplace, destinationplace, outboundpartialdate, inboundpartialdate)
        return results
