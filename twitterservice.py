from requests_oauthlib import OAuth1
import requests
import os


class TwitterService:

    oauth = OAuth1(
        os.getenv("twitter_consumerkey"),
        client_secret=os.getenv("twitter_consumersecret"),
        resource_owner_key=os.getenv("twitter_accesstoken"),
        resource_owner_secret=os.getenv("twitter_tokensecret"),
    )

    def upload_image(self, image_url):
        """ Loads the image in binary and uploads it as media to
            through the Twitter API """

        raw_image = requests.get(image_url).content

        return requests.post(
            os.getenv("twitter_mediauploadapi"),
            files={
                "media": raw_image
            },
            auth=self.oauth
        )

    def post_a_tweet(self, text, image_id):
        """ Posts a tweet through the Twitter API """

        return requests.post(
            os.getenv("twitter_tweetsapi"),
            json={
                "text": text,
                "media": {
                    "media_ids": [image_id]
                }
            },
            auth=self.oauth
        )
