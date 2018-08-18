from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'SPA Home!'


@app.route('/api')
def home():
    return 'API!'


if __name__ == "__main__":
    app.run()
