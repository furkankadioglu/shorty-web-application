from shorty.Providers.TinyUrlProvider import TinyUrlProvider
class TestTinyurlProvider:
    
    provider = TinyUrlProvider()

    def test_base_provider_variables(self):
        assert self.provider.requestUrl == "https://tinyurl.com/api-create.php"
        assert self.provider.type == "TEXT"
        assert self.provider.method == "GET"
        assert self.provider.name == "TinyUrl"

    def test_get_request_url(self):
        assert self.provider.requestUrl == "https://tinyurl.com/api-create.php"
        assert self.provider.getEndpoint() == "https://tinyurl.com/api-create.php"
        assert self.provider.getRequestUrl() == "https://tinyurl.com/api-create.php"


