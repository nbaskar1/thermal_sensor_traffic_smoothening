import urllib3
import random

http = urllib3.PoolManager()
average = 23 # Room Temperature

def prediction(num):
    global average
    average = (0.8 * average + num) // 2
    if num > 1.05 * average or num < 0.95 * average:
        return (num)
    return (False)

if __name__ == "__main__":
    while(True):
        random_gen = random.randint(1, 101)
        if random_gen <= 15:
            temperature = random.randint(-30, 20)
        elif 15 < random_gen < 86:
            temperature = random.randint(20, 26)
        else:
            temperature = random.randint(26, 101)

        prediction_value = prediction(temperature)

        # False if value does not exceed the threshold, actual value is passed otherwise
        if prediction_value:
            r = http.request('GET', 'http://0.0.0.0:5002/' + str(prediction_value))
