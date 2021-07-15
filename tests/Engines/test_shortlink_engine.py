from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Engines.ShortLinkEngine import ShortLinkEngine

class TestShortlinkEngine:
    engine = ShortLinkEngine()
    
    def test_default_variables(self):
        assert self.engine.name == "Shortlink Engine"
        assert type(self.engine.DEFAULT_PROVIDER) == type(BitlyProvider())
        assert self.engine.url == None
        assert self.engine.availableProviders == []
        assert self.engine.providerName == None
        assert self.engine.provider == None 
        assert self.engine.fallbackProvider == None
        assert self.engine.fallbackProviderName == None

    def test_set_link(self):
        self.engine.setLink("https://test.com")
        assert self.engine.url == "https://test.com"

    def test_set_providerName(self):
        self.engine.setProviderName("Bitly")
        assert self.engine.providerName == "Bitly"