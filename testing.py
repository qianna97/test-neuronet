import unittest
import requests
from utils import YandexAPI

'''
This is unit test module
Make sure the server is online
Default url server is localhost port 5000
'''

class AppTester(unittest.TestCase):
    url = 'http://localhost:5000'
    yandex_api = YandexAPI('e957dd18-ae0d-4b11-aa53-a4f2957abc15')

    def test_server_availability(self):
        # test server online status
        res = requests.get(self.url)
        self.assertEqual(res.status_code, 200)
    
    def test_yandex_api(self):
        res = self.yandex_api.get_coordinate('MKAD')
        self.assertEqual(res['status_code'], 200)
    
    def test_http_unkown_endpoint(self):
        # 404 response if path url is unknown
        res = requests.get(self.url+'/dsadbvds787686')
        self.assertEqual(res.status_code, 404)
    
    def test_http_method(self):
        # invalid http request -> method not allowed
        res = requests.post(self.url + '/mkad/?address=1122', {})
        self.assertEqual(res.status_code, 405)
    
    def test_input_none_type(self):
        # blank parameter
        res = requests.get(self.url + '/mkad/?address=')
        self.assertEqual(res.status_code, 400)

    def test_input_none_parameter(self):
        # parameter doesnt exist
        res = requests.get(self.url + '/mkad/')
        self.assertEqual(res.status_code, 400)
    
    def test_input_unkown_location(self):
        # unknown location
        res = requests.get(self.url + '/mkad/?address=112233')
        self.assertEqual(res.text, '"Location is not found"')
    
    def test_input_coordinate_format(self):
        # format of coordinate with different separator
        res_1 = requests.get(self.url + '/mkad/?address=37.526286,55.831216')
        res_2 = requests.get(self.url + '/mkad/?address=37.526286 55.831216')
        self.assertEqual(res_1.text, res_2.text)
    
    def test_address_outside(self):
        # location outside MKAD via address
        res = requests.get(self.url + '/mkad/?address=Zvenigorod')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text.split(' ')[1], 'km')
    
    def test_coordinate_outside(self):
        # location outside MKAD via coordinate
        res = requests.get(self.url + '/mkad/?address=37.34868,55.708019')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text.split(' ')[1], 'km')

    def test_address_inside(self):
        # location inside MKAD via address
        res = requests.get(self.url + '/mkad/?address=район%20Щукино')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.text.split(' ')), 2)
    
    def test_coordinate_inside(self):
        # location inside MKAD via coordinate
        res = requests.get(self.url + '/mkad/?address=37.526286,55.831216')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.text.split(' ')), 2)


if __name__ == '__main__':
    unittest.main()