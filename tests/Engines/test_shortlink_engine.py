from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Engines.ShortLinkEngine import ShortLinkEngine
from shorty.Providers.BitlyProvider import BitlyProvider

class TestShortlinkEngine:
    engine = ShortLinkEngine()
    
    def test_default_variables(self):
        assert self.engine.name == "Shortlink Engine"
        assert self.engine.url == None
        assert self.engine.availableProviders == []
        assert self.engine.providerName == None
        assert self.engine.provider == None 
        assert self.engine.fallbackProvider == None
        assert self.engine.fallbackProviderName == None
