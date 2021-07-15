from shorty.Responses.BitlyResponse import BitlyResponse

class TestBitlyResponse:
    
    response = BitlyResponse()

    def test_bitly_handle_function_with_dummy_data(self):
        data = '''{
        "created_at": "2021-07-11T11:53:35+0000",
        "id": "bit.ly/2TR00bO",
        "link": "https://bit.ly/2TR00bO",
        "custom_bitlinks": [],
        "long_url": "https://furkankadioglu.com/",
        "archived": false,
        "tags": [],
        "deeplinks": [],
        "references": {
            "group": "https://api-ssl.bitly.com/v4/groups/Bl7b1MrGV8A"
            }
        }'''

        self.response.handle(data)

        assert self.response.success == True
        assert self.response.code == 200
        assert self.response.data == "https://bit.ly/2TR00bO"

    def test_bitly_handle_function_with_dummy_data_and_fail(self):
        data = '''{}'''

        self.response.handle(data)

        assert self.response.success == False
        assert self.response.code == 500
        assert self.response.data == None