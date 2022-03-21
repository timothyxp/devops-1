from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Current datetime is {}".format(datetime.now())

if __name__ == "__main__":
    app.run()
