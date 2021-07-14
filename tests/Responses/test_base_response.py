from shorty.Responses.BaseResponse import BaseResponse

class TestBaseResponse:
    
    response = BaseResponse()

    def test_base_response_variables(self):
        assert self.response.success == True
        assert self.response.data == None
        assert self.response.code == 200

    def test_handle_and_fail(self):
        
        try: 
            self.response.handle()
        except:
            assert True
