from shorty.Responses.BaseResponse import BaseResponse
import json

class BitlyResponse(BaseResponse):

    def handle(self, data):
        data = json.loads(data)
        if("link" in data):
            self.success = True
            self.data = data["link"]
            self.code = 200
        else:
            self.success = False
            self.code = 500
            self.data = None
        
        return self