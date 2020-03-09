from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello From Flask!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
