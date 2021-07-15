from shorty.Providers.TinyUrlProvider import TinyUrlProvider
from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Engines.ShortLinkEngine import ShortLinkEngine
from shorty.Helpers.Generic import searchInObjectArray

class TestShortlinkEngine:
    engine = ShortLinkEngine()
    
    def test_default_variables(self):
        assert self.engine.name == "Shortlink Engine"
        assert type(self.engine.DEFAULT_PROVIDER) == type(BitlyProvider())
        assert self.engine.url == None
        assert self.engine.availableProviders == [type(BitlyProvider()), type(TinyUrlProvider())]
        assert self.engine.providerName == None
        assert self.engine.provider == None 
        assert self.engine.fallbackProvider == None
        assert self.engine.fallbackProviderName == None

    def test_set_link(self):
        self.engine.setLink("https://test.com")
        assert self.engine.url == "https://test.com"

    def test_set_provider_name(self):
        self.engine.setProviderName("Bitly")
        assert self.engine.providerName == "Bitly"

    def test_resolve_provider(self):
        assert type(BitlyProvider()) is type(self.engine.resolveProvider("Bitly"))

    def test_resolve_priver_use_fallback_provider(self):
        assert type(self.engine.DEFAULT_PROVIDER) is type(self.engine.resolveProvider("Bitly"))

    def test_resolve_priver_use_fallback_provider_with_incorrect_provider_name(self):
        assert type(self.engine.DEFAULT_PROVIDER) is type(self.engine.resolveProvider("INCORRECT PROVIDER NAME"))

    def test_resolve_provider_set_tinyurl_provider(self):
        assert type(TinyUrlProvider()) is type(self.engine.resolveProvider("TinyUrl"))

    def test_short_link_with_default(self):
        self.engine.shortLink("https://google.com")

        assert self.engine.url == "https://google.com"
        assert self.engine.provider == self.engine.DEFAULT_PROVIDER

    def test_short_link_with_bitly(self):
        self.engine.shortLink("https://google.com", "Bitly")

        assert self.engine.url == "https://google.com"
        assert type(self.engine.provider) == type(BitlyProvider())

    def test_short_link_with_bitly(self):
        self.engine.shortLink("https://google.com", "TinyUrl")

        assert self.engine.url == "https://google.com"
        assert type(self.engine.provider) == type(TinyUrlProvider())
