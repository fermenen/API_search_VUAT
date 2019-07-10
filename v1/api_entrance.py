import flask
from flask import request, jsonify
import jwt
import datetime
import v1.calculate as aux

app = flask.Flask(__name__)
app.config.from_object('config.BaseConfig')


class Auth:

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5, minutes=15),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise Exception('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise Exception('Invalid token. Please log in again.')


@app.route('/api/v1/auth/login', methods=['GET'])
def api_auth_login():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return Auth.encode_auth_token(id)


@app.route('/api/v1/home', methods=['GET'])
def home():
    if 'token' in request.args:
        token = request.args['token']
    else:
        return "Error: token necessary"

    try:
        Auth.decode_auth_token(token)
    except Exception as e:
        return f"ERROR: {str(e)}"

    return '''<h1>API V1 VUAT</h1>
    <p>Busqueda de vuelos, autobuses y trenes.</p>'''


@app.route('/api/v1/search', methods=['GET'])
def search():
    if 't' in request.args:
        token = request.args['t']
    else:
        return "Error: token necessary"

    try:
        Auth.decode_auth_token(token)
    except Exception as e:
        return f"ERROR: {str(e)}"

    if 'o' in request.args:
        origin_e = request.args['o']
    if 'd' in request.args:
        destination_e = request.args['d']
    if 'date' in request.args:
        date = request.args['date']
    if 'a' in request.args:
        adults = request.args['a']

    return jsonify(aux.calculate.search(origin=origin_e, destination=destination_e, date=date, adults=adults, children=0,
                                        babies=0))


app.run()
