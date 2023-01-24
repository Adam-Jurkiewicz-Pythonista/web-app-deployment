from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! From Adam Jurkiewicz - go to <a href="deploy"> deploy endpoint</a>'

@app.route('/deploy')
def hello_next():
    return 'Hello, World! From Adam Jurkiewicz - make <pre>deta deploy</pre> to push changes.'
