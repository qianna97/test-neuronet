from flask import Flask
from geo import distance_bp

app = Flask(__name__)
app.register_blueprint(distance_bp, url_prefix='/mkad')

@app.route('/')
def index():
    return '''
        <h3>Ths project is to calculate distance between MKAD to specific address using Yandex Geo API</h3>
        <a>If the address inside MKAD, then system will return the address longitude/lattitude without calculating distance<br>
        if the address outside MKAD, then system will return distance in kilometer using Haversine formula</a>
        <p>
        endpoint -> /mkad/?address=ADDRESS 
        <p>
        <p>ADDRESS (string/text) can be : <br>
        specific address, example : http://127.0.0.1:5000/mkad/?address=Аэропорт%20Внуково <br>
        or longitude,lattitude, example : http://127.0.0.1:5000/mkad/?address=37.34868,55.708019
        </p>
        '''