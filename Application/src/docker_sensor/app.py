import urllib3
import json

http = urllib3.PoolManager()

def prediction(num):
    return (num)

if __name__ == "__main__":
    while(True):
	prediction_value = prediction(random.randint(1, 101))

	# False if value does not exceed the threshold, actual value is passed otherwise
	if prediction_value:
	    r = http.request('GET', 'http://172.16.0.4:5002/' + str(prediction_value))
