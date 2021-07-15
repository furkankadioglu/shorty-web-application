
from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Engines.BaseEngine import BaseEngine

import requests
import random

class ShortLinkEngine(BaseEngine):

    name = "Shortlink Engine"

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
