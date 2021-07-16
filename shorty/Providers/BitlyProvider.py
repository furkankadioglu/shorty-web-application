from shorty.Providers.BaseProvider import BaseProvider
from shorty.Responses.BitlyResponse import BitlyResponse
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

    def handleResponse(self, response):
        responseStructure = BitlyResponse()
        apiResponse = responseStructure.handle(response.content)
        return apiResponse

    def prepareRequest(self, url):

        headers = {
            'Authorization': f'Bearer {self.getAuthenticationToken()}',
            'Content-Type': 'application/json',
        }

        data = { 
            "long_url": url, 
            "domain": "bit.ly" 
        }

        return {
            "headers": headers,
            "json": data,
            "params": None,
            "type": self.type
        }
