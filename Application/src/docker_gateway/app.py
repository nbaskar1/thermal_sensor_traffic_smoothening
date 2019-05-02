import urllib3
import json

http = urllib3.PoolManager()
count = 0
average = None

from flask import Flask
app = Flask(__name__)

@app.route("/<num>")
def data_aggregate(num):
    global count
    count += 1

    data = {'NanoCpus': prediction_resource(count)}
    encoded_data = json.dumps(data).encode('utf-8')

    r = http.request('POST', 'http://172.16.0.4:5001/containers/gateway/update', body=encoded_data, headers={'Content-Type': 'application/json'})

    if predict(num):
        r = http.request('GET', 'http://0.0.0.0:5003/' + str(predict(num)))
    #print (r.status)
    #print (r.data)

    return ("")

def prediction_resource(count):
    return (500000000)

# False if outside of threshold range, actual value otherwise
def predict(number):
    global average
    if average:
        average = (0.8 * average + num) / 2
    else:
        average = number

    if num > 1.05 * average or num < 0.95 * average:
        return (number)
    return (False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5002')
