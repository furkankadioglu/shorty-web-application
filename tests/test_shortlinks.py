from shorty.Providers.TinyUrlProvider import TinyUrlProvider
from shorty.Providers.BitlyProvider import BitlyProvider
import json
import requests_mock

class TestShortlinks:
    
    def test_get_shortlinks_not_allowed(self,get):
        assert get("/shortlinks").status == "405 METHOD NOT ALLOWED"

    def test_post_shortlinks_allowed(self,post):
        assert post("/shortlinks").status != "405 METHOD NOT ALLOWED"

    def test_shortlink_endpoint_with_default_provider(self, post):
        with requests_mock.Mocker() as mock:
            mock.post(BitlyProvider().getRequestUrl(), json={"created_at": "2021-07-11T11:53:35+0000",  "id": "bit.ly/2TR00bO",  "link": "https://bit.ly/2TR00bO",  "custom_bitlinks": [],  "long_url": "https://google.com",  "archived": False,  "tags": [],  "deeplinks": [],  "references": {  "group": "https://api-ssl.bitly.com/v4/groups/Bl7b1MrGV8A"  }})

            mimetype = 'application/json'
            headers = {
                'Content-Type': mimetype,
                'Accept': mimetype
            }
            data = {
                "url": "https://google.com"
            }

            response = post("/shortlinks", data=json.dumps(data), headers=headers)

            assert response.json["link"] != None
            assert response.json["link"] == "https://bit.ly/2TR00bO"
            assert response.json["url"] == "https://google.com"
            assert response.status == "200 OK"

    def test_shortlink_endpoint_without_parameters_and_fail(self, post):
        with requests_mock.Mocker() as mock:
            mock.post(BitlyProvider().getRequestUrl(), json={"created_at": "2021-07-11T11:53:35+0000",  "id": "bit.ly/2TR00bO",  "link": "https://bit.ly/2TR00bO",  "custom_bitlinks": [],  "long_url": "https://google.com",  "archived": False,  "tags": [],  "deeplinks": [],  "references": {  "group": "https://api-ssl.bitly.com/v4/groups/Bl7b1MrGV8A"  }})

            mimetype = 'application/json'
            headers = {
                'Content-Type': mimetype,
                'Accept': mimetype
            }
            data = {
            }

            response = post("/shortlinks", data=json.dumps(data), headers=headers)

            assert response.json["success"] == False
            assert response.status == "400 BAD REQUEST"

    def test_shortlink_endpoint_with_bitly_provider(self, post):
        with requests_mock.Mocker() as mock:
            mock.post(BitlyProvider().getRequestUrl(), json={"created_at": "2021-07-11T11:53:35+0000",  "id": "bit.ly/2TR00bO",  "link": "https://bit.ly/2TR00bO",  "custom_bitlinks": [],  "long_url": "https://google.com",  "archived": False,  "tags": [],  "deeplinks": [],  "references": {  "group": "https://api-ssl.bitly.com/v4/groups/Bl7b1MrGV8A"  }})

            mimetype = 'application/json'
            headers = {
                'Content-Type': mimetype,
                'Accept': mimetype
            }
            data = {
                "url": "https://google.com",
                "provider": "Bitly"
            }

            response = post("/shortlinks", data=json.dumps(data), headers=headers)

            assert response.json["link"] != None
            assert response.json["link"] == "https://bit.ly/2TR00bO"
            assert response.json["url"] == "https://google.com"
            assert response.status == "200 OK"


    def test_shortlink_endpoint_with_tinyurl_provider(self, post):
        with requests_mock.Mocker() as mock:
            mock.get(TinyUrlProvider().getRequestUrl(), text="https://tinyurl.com/n9wdyh7")

            mimetype = 'application/json'
            headers = {
                'Content-Type': mimetype,
                'Accept': mimetype
            }
            data = {
                "url": "https://google.com",
                "provider": "TinyUrl"
            }

            response = post("/shortlinks", data=json.dumps(data), headers=headers)

            assert response.json["link"] != None
            assert response.json["link"] == "https://tinyurl.com/n9wdyh7"
            assert response.json["url"] == "https://google.com"
            assert response.status == "200 OK"


    def test_shortlink_endpoint_with_tinyurl_provider_and_wrong_url_failure(self, post):

        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            "url": "helloworlditsnotanurl",
            "provider": "TinyUrl"
        }

        response = post("/shortlinks", data=json.dumps(data), headers=headers)
        assert response.status == "400 BAD REQUEST"


    def test_shortlink_with_incorrect_params_and_fail(self, post):

        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        data = {
            "url": "helloworlditsnotanurl",
            "provider": "WrongProvider"
        }

        response = post("/shortlinks", data=json.dumps(data), headers=headers)
        assert response.status == "500 INTERNAL SERVER ERROR"


    def test_shortlink_with_incorrect_provider_and_run_with_fallback_scenario(self, post):
        with requests_mock.Mocker() as mock:
            mock.post(BitlyProvider().getRequestUrl(), json={"created_at": "2021-07-11T11:53:35+0000",  "id": "bit.ly/2TR00bO",  "link": "https://bit.ly/2TR00bO",  "custom_bitlinks": [],  "long_url": "https://google.com",  "archived": False,  "tags": [],  "deeplinks": [],  "references": {  "group": "https://api-ssl.bitly.com/v4/groups/Bl7b1MrGV8A"  }})
            mimetype = 'application/json'
            headers = {
                'Content-Type': mimetype,
                'Accept': mimetype
            }
            data = {
                "url": "https://google.com",
                "provider": "WrongProvider"
            }

            response = post("/shortlinks", data=json.dumps(data), headers=headers)
            assert response.status == "200 OK"
            assert response.json["link"] == "https://bit.ly/2TR00bO"
            assert response.json["url"] == "https://google.com"