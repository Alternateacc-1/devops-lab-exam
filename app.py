import os, socket
from flask import Flask, render_template

app = Flask(__name__)
VERSION = 'v1'


@app.route('/')
def home():
    return render_template('index.html', version=VERSION,
                           message=os.getenv('MESSAGE', 'Hello from Flask!'),
                           host=socket.gethostname())


@app.route('/health')
def health():
    return 'Server is up and running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
