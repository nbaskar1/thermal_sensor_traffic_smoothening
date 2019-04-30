import urllib3
import json

http = urllib3.PoolManager()
count = 0

from flask import Flask
app = Flask(__name__)

@app.route("/<num>")
def fib(num):
    global count
    count += 1
    number = int(num)
    fib_arr = []
    fib_arr.append(0)
    fib_arr.append(1)

    data = {'NanoCpus': prediction()}
    encoded_data = json.dumps(data).encode('utf-8')

    r = http.request('POST', 'http://172.16.0.4:5001/containers/test/update', body=encoded_data, headers={'Content-Type': 'application/json'})
    print (r.status)
    print (r.data)

    for num in range(2, number):
        fib_arr.append(fib_arr[num - 1] + fib_arr[num - 2])

    return (str(fib_arr[number - 1]))

def prediction():
    return (500000000)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
