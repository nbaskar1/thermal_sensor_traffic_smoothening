from flask import Flask
app = Flask(__name__)

@app.route("/<num>")
def data_aggregate(num):
    print (num)
    return ("")

if __name__ == "__main__":
    app.run(host= '172.16.0.4')
