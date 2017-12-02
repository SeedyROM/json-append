import json

class NoJSONFileSpecified(BaseException):
    pass

class JSONReader:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def load(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path

        self.current_file = open(self.file_path, 'r+')


def reader(*args, **kwargs):
    return JSONReader(*args, **kwargs)
