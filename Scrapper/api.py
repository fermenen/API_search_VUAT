class Skyscanner:

    TOKEN = 'ceabdcd708msh8e214f643d58de6p18e13cjsnb1cd40632505'

    @staticmethod
    def get_data(country, currency, locale, originplace, destinationplace, outboundpartialdate, inboundpartialdate):
        """
        :param country: The market country your user is in
        :param currency: The currency you want the prices in
        :param locale: The locale you want the results in (ISO locale)
        :param originplace: The origin place (see places)
        :param destinationplace: The destination place (see places)
        :param outboundpartialdate: The outbound date. Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”.
        :param inboundpartialdate: OPTIONAL The return date. Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”. Use empty string for oneway trip.
        """
        import requests
        r = requests.get(f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/{country}/{currency}/{locale}/{originplace}/{destinationplace}/{outboundpartialdate}?inboundpartialdate={inboundpartialdate}",
                headers={
                "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                "X-RapidAPI-Key": Skyscanner.TOKEN}
            )
        if r.status_code == 200:
            return r.json()
        else:
            return Exception
