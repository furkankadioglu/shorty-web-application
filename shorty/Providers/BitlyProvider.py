from shorty.Providers.BaseProvider import BaseProvider
import os
class BitlyProvider(BaseProvider):
    requestUrl = "https://api-ssl.bitly.com/v4/shorten"
    type = "JSON"
    method = "POST"
    name = "Bitly"

    def getRequestUrl(self):
        return self.getEndpoint()

    def getAuthenticationToken(self):
        return os.environ.get('BITLY_AUTH_KEY')
