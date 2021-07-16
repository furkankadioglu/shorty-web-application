class BaseResponse(object):
    success = True
    data = None
    code = 200

    def handle(self):
        # Couldn't find any way to create an abstract class, I guess this is the python way
        raise NotImplementedError("Handle should be overrided!")