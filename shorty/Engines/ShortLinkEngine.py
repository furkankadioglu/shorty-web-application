
from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Engines.BaseEngine import BaseEngine

import requests
import random

class ShortLinkEngine(BaseEngine):

    name = "Shortlink Engine"

    DEFAULT_PROVIDER = BitlyProvider()

    url = None

    availableProviders = []

    providerName = None
    provider = None

    fallbackProvider = None
    fallbackProviderName = None


    def __init__(self) -> None:
        super().__init__()

        self.availableProviders = [
        ]

    def setLink(self,URL):
        self.url = URL

    def setProviderName(self, providerName):
        self.providerName = providerName