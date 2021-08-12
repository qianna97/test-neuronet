from flask import Blueprint, request, Response
from utils import YandexAPI, Log
from math import cos, asin, sqrt, pi
import json

'''
Blueprint for calculating MKAD distance from specific address
'''

# Log File
log = Log()

# Blueprint
distance_bp = Blueprint('distance_bp', __name__)

# Yandex Geomap API
yandex_api = YandexAPI('e957dd18-ae0d-4b11-aa53-a4f2957abc15')

# MKAD coordinates longlat lower/upper bounding box for comparator 
MKAD_bbox = [37.368775, 55.571826, 37.843427, 55.911123]
MKAD_coordinates = [37.632206, 55.898947]


@distance_bp.route('/')
def mkad_distance():
    address = request.args.get('address')
    
    # Checking valid input
    if address is None or len(address) == 0:
        log.write('[ERROR] Bad Request. Input does not exist')
        return Response(
            'Please input string address at ?address=',
            status=400) 
    
    res = yandex_api.get_coordinate(address)
    log.write(str(res['status_code']) + ' Request Input ' + address)
    
    # Checking HTTP status from Yandex API
    if res['status_code'] == 200:
        pos = res['content']

        # Check if point inside bbox of MKAD coordinate
        if pos[1] > MKAD_bbox[1] and pos[1] < MKAD_bbox[3] and pos[0] > MKAD_bbox[0] and pos[0] < MKAD_bbox[2]:
            # Return original pos
            log.write('[INFO] The Address inside MKAD')
            return str(pos[0]) + ' ' + str(pos[1]) 
        else:
            # Calculate distance in kilometer using Haversine formula
            p = pi/180
            a = (0.5 - cos((MKAD_coordinates[1]-pos[1])*p) / 2 
                + cos(pos[1]*p) * cos(MKAD_coordinates[1] * p)
                * (1-cos((MKAD_coordinates[0]-pos[0])*p)) / 2)
            result = str(round(12742 * asin(sqrt(a)), 3))
            log.write('[INFO] The Address outside MKAD. Distance : ' + result + ' km')
            return result + ' km'
    else:
        log.write('[ERROR] ' + str(res['status_code']))
        return Response(
            json.dumps(res['content']),
            status=res['status_code'], 
            mimetype='application/json')