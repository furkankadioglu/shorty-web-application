
from shorty.Providers.BaseProvider import BaseProvider
from shorty.Responses.TinyUrlResponse import TinyUrlResponse

class TinyUrlProvider(BaseProvider):
    requestUrl = "https://tinyurl.com/api-create.php"
    type = "TEXT"
    method = "GET"
    name = "TinyUrl"

    def getRequestUrl(self):
        return self.getEndpoint()
    
    def handleResponse(self, response):
        responseStructure = TinyUrlResponse()
        apiResponse = responseStructure.handle(response.content)
        return apiResponse

    def prepareRequest(self, url):

        headers = {
        }

        data = { 
            "url": url,
        }

        return {
            "headers": headers,
            "params": data,
            "json": None,
            "type": self.type
        }
