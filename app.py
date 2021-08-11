from flask import Flask
from geo import distance_bp

app = Flask(__name__)
app.register_blueprint(distance_bp)