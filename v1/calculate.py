def search(origin, destination, date, adults=1, children=0, babies=0):
    import Scrapper.kiwi as api_flights
    import Scrapper.bus_radar as api_bus
    import util.city as city
    import v1.api_entrance as v1
    import datetime

    city_origin = city.city_mongo.get_city(origin)
    city_destination = city.city_mongo.get_city(destination)
    date = datetime.datetime(int(date.split('-')[2]), int(date.split('-')[1]), int(date.split('-')[0]))

    v1.log.push_log_debug(f"CALCULATE -> from [{city_origin['poblacion']}] to [{city_destination['poblacion']}] at {date}")

    data_bus = api_bus.bus_radar_api.get_data(city_origin['poblacion'], city_destination['poblacion'],
                                              f'{date.year}-{date.month}-{date.day}', adults)

    data_kiwi = api_flights.kiwi_api.get_data(city.airpot_mongo.get_airpot(city_origin),
                                              city.airpot_mongo.get_airpot(city_destination),
                                              f'{date.day}/{date.month}/{date.year}')

    # data_return = decorate_response(data_bus, data_kiwi)


    return data_bus
