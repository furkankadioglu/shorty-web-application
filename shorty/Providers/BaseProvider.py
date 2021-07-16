class BaseProvider(object):
    requestUrl = ""
    method = "GET"
    response = None
    name = ""

    def __init__(self) -> None:
        super().__init__()

    def getEndpoint(self):
        return self.requestUrl