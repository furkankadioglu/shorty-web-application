from shorty.Providers.BitlyProvider import BitlyProvider
import os
class TestBitlyProvider:
    
    provider = BitlyProvider()

    def test_base_provider_variables(self):
        assert self.provider.requestUrl == "https://api-ssl.bitly.com/v4/shorten"
        assert self.provider.type == "JSON"
        assert self.provider.method == "POST"
        assert self.provider.name == "Bitly"

    def test_get_request_url(self):
        assert self.provider.requestUrl == "https://api-ssl.bitly.com/v4/shorten"
        assert self.provider.getEndpoint() == "https://api-ssl.bitly.com/v4/shorten"
        assert self.provider.getRequestUrl() == "https://api-ssl.bitly.com/v4/shorten"

    def test_get_auth_token(self):
        assert self.provider.getAuthenticationToken() == os.environ.get('BITLY_AUTH_KEY')

