import requests

GOOGLE_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json?address='
GOOGLE_API_KEY = 'AIzaSyCvi5z8qZyzZXRM_zXnHC3olXSEVi-PJGU'


class location:
    def __init__(self):
        self.lat = 0
        self.long = 0
        self.formatted_address = 0

    def google_api_call(self, address):
        return GOOGLE_API_ENDPOINT + address + '&key=' + GOOGLE_API_KEY

    def get_result(self, address):
        address = address.replace(' ', '+')

        address_response = requests.get(self.google_api_call(address))

        resp_json_payload = address_response.json()

        # TODO: Make location class example call:
        # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA
        # &key=AIzaSyCvi5z8qZyzZXRM_zXnHC3olXSEVi-PJGU
        lat_lng = resp_json_payload['results'][0]['geometry']['location']
        self.lat = lat_lng["lat"]
        self.long = lat_lng["lng"]
        self.formatted_address = resp_json_payload['results'][0]['formatted_address']
