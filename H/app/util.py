import abc
from time import time
from hashlib import md5

class FileName(abc.ABC):

    _value = None

    # TODO

    def __init__(self, src):
        self._src = src

    def  __repr__(self):
        if self._value is None:
            self._value = md5((self._src + str(time())).encode('utf-8')).hexdigest()
        return self._value

    def __call__(self, ):
        1

FileName.register(str)
# FileName.register(unicode)

HASHED = FileName(src)

'fghtgfn' / HASHED
