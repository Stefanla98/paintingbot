from museumservice import MuseumService
from twitterservice import TwitterService

def lambda_handler(event, context):
    museum_service = MuseumService()
    twitter_service = TwitterService()

    metropolitan_painting = museum_service.get_painting_from_metropolitan_museum()

    metropolitan_twitter_request = twitter_service.upload_image(metropolitan_painting["image_url"])

    if (metropolitan_twitter_request):
        twitter_service.post_a_tweet(
            f'{metropolitan_painting["name"]}, {metropolitan_painting["artist"]}, {metropolitan_painting["year"]}',
            metropolitan_twitter_request.json()["media_id_string"]
        )
    

    rijks_painting = museum_service.get_painting_from_rijksmuseum()

    rijks_twitter_image_id = twitter_service.upload_image(rijks_painting["image_url"]).json()["media_id_string"]
    twitter_service.post_a_tweet(
        rijks_painting["name"],
        rijks_twitter_image_id
    )

    chicago_painting = museum_service.get_painting_from_art_institute_of_chicago()

    chicago_twitter_image_id = twitter_service.upload_image(chicago_painting["image_url"]).json()["media_id_string"]
    twitter_service.post_a_tweet(
        f'{chicago_painting["name"]}, {chicago_painting["artist"]}',
        chicago_twitter_image_id
    )
