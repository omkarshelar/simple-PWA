from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/after', methods=['GET'])
def after():
    return render_template('afterlogin.j2')

@app.route('/cache', methods=['GET'])
def cache():
    return render_template('cache.html')

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)