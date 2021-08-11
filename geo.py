from flask import Blueprint, request, Response
from yandex import YandexAPI
from math import cos, asin, sqrt, pi
import json

distance_bp = Blueprint('distance_bp', __name__)

yandex_api = YandexAPI('e957dd18-ae0d-4b11-aa53-a4f2957abc15')

# MKAD coordinates longlat lower/upper bounding box for comparator 
MKAD_bbox = [37.368775, 55.571826, 37.843427, 55.911123]
MKAD_coordinates = [37.632206, 55.898947]


@distance_bp.route('/')
def index():
    address = request.args.get('address')
    res = yandex_api.get_coordinate(address)
    
    if res['status_code'] == 200:
        pos = res['content']

        # Check if point inside bbox of MKAD coordinate
        if pos[1] > MKAD_bbox[1] and pos[1] < MKAD_bbox[3] and pos[0] > MKAD_bbox[0] and pos[0] < MKAD_bbox[2]:
            # Return original pos 
            return " ".join(pos)
        else:
            # Calculate distance in kilometer using Haversine formula
            p = pi/180
            a = (0.5 - cos((MKAD_coordinates[1]-pos[1])*p) / 2 
                + cos(pos[1]*p) * cos(MKAD_coordinates[1] * p)
                * (1-cos((MKAD_coordinates[0]-pos[0])*p)) / 2)
            return str(12742 * asin(sqrt(a)))
    else:
        return Response(
            json.dumps(res['content']),
            status=res['status_code'], 
            mimetype='application/json')