from shorty.Responses.TinyUrlResponse import TinyUrlResponse

class TestTinyUrlResponse:
    
    response = TinyUrlResponse()

    def test_tinyurl_handle_function_with_dummy_data(self):
        data = b'https://tinyurl.com/n9wdyh7'

        self.response.handle(data)

        assert self.response.success == True
        assert self.response.code == 200
        assert self.response.data == "https://tinyurl.com/n9wdyh7"

    def test_bitly_handle_function_with_dummy_data_and_fail(self):
        data = '''Error'''

        self.response.handle(data)

        assert self.response.success == False
        assert self.response.code == 400
        assert self.response.data == None