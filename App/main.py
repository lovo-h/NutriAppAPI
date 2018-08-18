from flask import Flask

from App.infrastructure import routes

app = Flask(__name__)

routes.init(app)


if __name__ == "__main__":
    app.run()

