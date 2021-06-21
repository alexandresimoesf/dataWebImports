from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Data Web Import init'


if __name__ == "__main__":
    app.run()
