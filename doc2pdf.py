"""Convert .doc files sent through the interface to PDF, adding a cover page and headers."""
__author__ = 'Edouard Klein <edou -at- rdklein.fr>'


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
