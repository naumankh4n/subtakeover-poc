from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=False)
