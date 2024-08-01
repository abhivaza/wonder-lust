from flask import Flask
from flasgger import Swagger

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello World")
    return 'Hello, Docker!'

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=4100
    )