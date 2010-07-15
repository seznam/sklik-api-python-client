
from ..errors import SklikApiError, ArgumentError, NotFoundError, \
                     InvalidDataError, AccessError, \
                     SklikApiWarning, NoActionWarning
from warnings import warn
from types import DictType, ListType, TupleType
from datetime import datetime
from time import mktime, strptime
from xmlrpclib import DateTime

class Missing(object):
    """Missing class

    Indicates missing value
    """

    def __repr__(self):
        return "Missing"
    #enddef

    def __str__(self):
        return "Missing"
    #enddef
#endclass

Missing = Missing()

class Methods(object):
    def checkResult(self, res):
        if "session" in res:
            self._Client__session = res["session"]
        #endif

        if res["status"] == 200:
            return
        elif res["status"] == 400:
            raise ArgumentError(res["statusMessage"], res["errors"])
        elif res["status"] == 401:
            raise SessionError(res["statusMessage"])
        elif res["status"] == 403:
            raise AccessError(res["statusMessage"])
        elif res["status"] == 404:
            raise NotFoundError(res["statusMessage"])
        elif res["status"] == 406:
            raise InvalidDataError(res["status"], res["errors"])
        elif res["status"] == 206:
            warn(res["statusMessage"], SklikApiWarning)
            return
        elif res["status"] == 409:
            warn(res["statusMessage"], NoActionWarning)
        else:
            raise SklikApiError(res["statusMessage"])
        #endif
    #enddef

    def convIn(self, objType, data, keepDict = False):
        has = hasattr(data, "__convert__")

        if has or isinstance(data, objType):
            if has:
                objType = data.__class__
            #endif

            if keepDict:
                return dict([
                    (key, self.convIn(objType, value), ) \
                        for key, value in data.iteritems() if value != Missing])
            #endif

            result = {}
            for attr in objType.__slots__:
                value = getattr(data, attr)
                if value != Missing:
                    result[attr] = self.convIn(objType, value)
                #endif
            #endfor
            return result
        elif isinstance(data, datetime):
            return DateTime(int(mktime(data.timetuple())))
        elif isinstance(data, ListType):
            return [self.convIn(objType, value) for value in data]
        elif isinstance(data, TupleType):
            return tuple([self.convIn(objType, value) for value in data])
        else:
            return data
        #endif
    #enddef

    def convOut(self, objType, data):
        if isinstance(data, DateTime):
            return datetime(*strptime(data.value[:-5], "%Y%m%dT%H:%M:%S")[:6])
        elif isinstance(data, DictType):
            result = objType()
            for attr in objType.__slots__:
                setattr(result, attr, self.convOut(objType, data.get(attr, Missing)))
            #endfor
            return result
        elif isinstance(data, ListType):
            return [self.convOut(objType, value) for value in data]
        elif isinstance(data, TupleType):
            return self.convOut(data[1], data[0])
        else:
            return data
        #endif
    #enddef
#endclass

def convert(objType):
    def function(f):
        result = lambda self, *args, **kwargs: self.convOut(
            objType, f(
                self,
                *self.convIn(objType, args),
                **self.convIn(objType, kwargs, keepDict = True)))

        result.__doc__ = f.__doc__
        return result
    #enddef
    return function
#enddef
