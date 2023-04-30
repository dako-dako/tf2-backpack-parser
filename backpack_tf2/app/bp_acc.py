from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class Account:
    """Account class is responsible for initiating OAuth2 connection."""

    def __init__(self, client_id, client_secret, api_key):
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url="https://backpack.tf/oauth/access_token",
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        self.token = token
