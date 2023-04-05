import requests
import random

import os

class MuseumService:

    def get_painting_from_metropolitan_museum(self):
        """ Obtains a random painting from the Metropolitan Museum of Art """

        api_endpoint = os.getenv("metropolitan_api")

        response = requests.get(api_endpoint).json()

        rand = random.randint(0, len(response["objectIDs"]))

        response2 = requests.get(f'{api_endpoint}/{response["objectIDs"][rand]}').json()

        if response2["primaryImage"]:
            return {
                "name": response2["title"],
                "artist": response2["artistAlphaSort"],
                "year": response2["objectDate"],
                "image_url": response2["primaryImage"],
            }
        else:
            return self.get_painting_from_metropolitan_museum()

    def get_painting_from_rijksmuseum(self):
        """ Obtains a random painting from Rijksmuseum """

        api_endpoint = os.getenv("rijksmuseum_api")

        response = requests.get(api_endpoint).json()

        rand = random.randint(0, len(response["artObjects"]))

        return {
            "name": response["artObjects"][rand]["longTitle"],
            "image_url": response["artObjects"][rand]["webImage"]["url"],
        }

    def get_painting_from_art_institute_of_chicago(self):
        """ Obtains a random paintin from the Art Institute of Chicago """

        api_endpoint = os.getenv("chicagoinstitute_api")
        params = {
            "limit": 1
        }

        response = requests.get(api_endpoint, params).json()

        rand = random.randint(1, response["pagination"]["total_pages"])

        params = {
            "page": rand,
            "limit": 1,
            "fields": "title,image_id,artist_title,artist_display"
        }

        response = requests.get(api_endpoint, params).json()

        return {
            "name": response["data"][0]["title"],
            "artist": response["data"][0]["artist_title"],
            "image_url": f'{response["config"]["iiif_url"]}/{response["data"][0]["image_id"]}/full/843,/0/default.jpg',
        }
