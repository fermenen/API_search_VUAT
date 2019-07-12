
from pymongo import MongoClient

client = MongoClient('35.195.187.105', 27017)


class cities:

    @staticmethod
    def upload_mongo():
        import csv
        c = 'c-es-'
        i = 1
        with open('list-esp.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                post = {
                    "id_citie": c + str(i),
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
                print(post)
                i += 1
                line_count += 1
            print(f'Processed {line_count} lines.')


if __name__ == '__main__':
    cities.upload_mongo()
