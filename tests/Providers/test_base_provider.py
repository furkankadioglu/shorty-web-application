from shorty.Providers.BaseProvider import BaseProvider

class TestBaseProvider:
    
    provider = BaseProvider()

    def test_base_provider_variables(self):
        assert self.provider.response == None
        assert self.provider.name == ""
        assert self.provider.requestUrl == ""
        assert self.provider.method == "GET"
        assert self.provider.getEndpoint() == ""

    def test_get_endpoint(self):
        self.provider.requestUrl = "https://google.com"
        assert self.provider.requestUrl == "https://google.com"
        assert self.provider.getEndpoint() == "https://google.com"
