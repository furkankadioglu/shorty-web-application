from shorty.Responses.BaseResponse import BaseResponse

class TinyUrlResponse(BaseResponse):

    def handle(self, data):
        if(data[:4] == b'http'):
            self.data = data.decode("utf-8")
            self.success = True
            self.code = 200
        else: 
            self.data = None
            self.success = False
            self.code = 400
        return self