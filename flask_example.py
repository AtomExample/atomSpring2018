from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h5>SPHERE.GREYONE.RU</h5><div>Hello</div>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='2000')
