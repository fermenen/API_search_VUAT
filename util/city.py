import v1.api_entrance as v1

class city_mongo:

    from pymongo import MongoClient
    client = MongoClient("mongodb://vuat:k114RkwkOdYE@35.195.187.105:27017/vuat")

    mydb = client["vuat"]
    mycol = mydb["city"]

    @staticmethod
    def get_city(string):

        x = city_mongo.mycol.find_one({"$text": {"$search": string}})
        if x is not None:
            return x
        else:
            print("DEBUG - city nout found")


class airpot_mongo:
    from pymongo import MongoClient
    client = MongoClient("mongodb://vuat:k114RkwkOdYE@35.195.187.105:27017/vuat")

    mydb = client["vuat"]
    airpots = mydb["airpots"]

    @staticmethod
    def get_airpot(city):
        #TODO: Crear indice en mongo
        airpot_prox = airpot_mongo.airpots.find_one({"location": {"$near": [float(city["location"]["lat"]),
                                                                  float(city["location"]["lon"])]}, 'comercial': 1})

        v1.log.push_log_debug(f"AIRPOT -> {airpot_prox['name']}-{airpot_prox['code']}")

        if airpot_prox is not None:
            return airpot_prox
        else:
            print("DEBUG - airpot nout found")
