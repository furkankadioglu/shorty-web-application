
from shorty.Providers.BaseProvider import BaseProvider
from shorty.Providers.BitlyProvider import BitlyProvider
from shorty.Providers.TinyUrlProvider import TinyUrlProvider
from shorty.Engines.BaseEngine import BaseEngine
from shorty.Helpers.Generic import searchInObjectArray

from flask import jsonify
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

       # TO DO: Service Container architecture would be great here.
        # Unfortunately I couldn't find any example for this on python language.
        # Needs more time for to do this feature. Maybe next time! 

        self.availableProviders = [
            type(BitlyProvider()),
            type(TinyUrlProvider()),
        ]

    def setLink(self,URL):
        self.url = URL

    def setProviderName(self, providerName):
        self.providerName = providerName
        self.resolveProvider(providerName)

    def shortLink(self, url = None, providerName = None):

        if url != None:
            self.setLink(url)
        
        self.setProviderName(providerName)

        response = self.shortUrlRequest(url)

        if(response.success == True):
            return jsonify({"url": url, "link": response.data}), 200
        else:
            return jsonify({}), response.code

    def shortUrlRequest(self, url):
        requestData = self.provider.prepareRequest(url)
        response = requests.request(self.provider.method, url=self.provider.getRequestUrl(), headers=requestData["headers"], json=requestData["json"], params=requestData["params"], timeout=20)
        return self.provider.handleResponse(response)

    def resolveProvider(self, providerName = None) -> BaseProvider:
        provider = searchInObjectArray(self.availableProviders, lambda x: x.name == providerName)
    
        if(provider == False or provider == None):
            self.provider = self.DEFAULT_PROVIDER
        else: 
            provider = provider()
            self.provider = provider

        self.fallbackProvider = self.setFallbackProvider()
        return self.provider

    def setFallbackProvider(self, providerName = None) -> BaseProvider:
        temporaryAvailableProviders = self.availableProviders

        if self.provider in temporaryAvailableProviders:
            temporaryAvailableProviders.remove(type(self.provider))
            
        return random.choice(temporaryAvailableProviders)
