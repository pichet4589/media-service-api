from flask import Flask
from waitress import serve
app = Flask(__name__)
@app.route('/api/v1/')
def myendpoint():
    return 'We are computering now'
serve(app, host='0.0.0.0', port=8080, threads=1) #WAITRESS!