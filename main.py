# from urllib import request

from flask import *
import json, time

app = Flask(__name__)
@app.route('/', methods =['GET'])
def home_page():
    # data_set = {'page': 'Home', 'Message': 'Successfully loaded', 'Time': time.time()}
    data_set = {'page': 'Home', 'Message': 'API Successfully loaded', 'Time': time.time()}
    #convert data set to json
    json_dump = json.dumps(data_set)
    return json_dump

#enable user input filter item
@app.route('/msisdn/', methods =['GET'])
def request_page():
    usr_query = str(request.args.get('msisdn')) #/user/?user=query
    data_set = {'page': 'Request', 'Message': 'Successfully got the request for {usr_query}', 'Time': time.time()}
    #convert data set to json
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=8888)