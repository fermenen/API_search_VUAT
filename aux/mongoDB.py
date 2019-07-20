from pymongo import MongoClient

client = MongoClient("mongodb://vuat:k114RkwkOdYE@35.195.187.105:27017/vuat")


class cities:

    @staticmethod
    def upload_mongo():
        import csv

        mydb = client["vuat"]
        mycol = mydb["city"]

        c = 'c-es-'
        i = 1
        with open('list-esp.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                post = {
                    "id_city": c + str(i),
                    "country": 'es',
                    "comunidad": row[0],
                    "provincia": row[1],
                    "poblacion": row[2],
                    "location": {"lat": row[3], "lon": row[4]},
                    "altitud": row[5],
                    "habitantes": row[6],
                    "hombres": row[7],
                    "mujeres": row[8]

                }
                x = mycol.insert_one(post)
                print(post)
                i += 1
                line_count += 1
            print(f'Processed {line_count} lines.')


class airpot:
    @staticmethod
    def upload_mongo():
        import csv

        mydb = client["vuat"]
        mycol = mydb["airpots"]

        c = 'a-es-'
        i = 1
        with open('list-esp-airpot.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                post = {
                    "id_airpot": c + str(i),
                    "country": 'es',
                    "code": row[1],
                    "type": row[2],
                    "name": row[3],
                    "location": {"lat": float(row[4]), "lon": float(row[5])},
                    "elevation": row[6],
                    "iso-region": row[9],
                    "municipality": row[10],
                    "comercial": int(row[11]),
                    "iataocode": row[13],
                    "web-link": row[15],
                    "wikipedia-link": row[16],
                    "last-updated": row[19],

                }
                x = mycol.insert_one(post)
                print(post)
                i += 1
                line_count += 1
            print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    airpot.upload_mongo()
