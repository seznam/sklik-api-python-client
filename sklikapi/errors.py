
class SklikApiError(Exception):
    """Base Sklik API error exception class
    """

    pass
#endclass

class SklikApiWarning(Warning):
    """Base Sklik API warning exception class
    """

    pass
#endclass

class NotFoundError(SklikApiError):
    """Sklik API not found error exception
    """

    pass
#endclass

class ArgumentError(SklikApiError):
    """Sklik API argument error exception
    """

    __slots__ = ["__errors"]

    def __init__(self, message, errors):
        SklikApiError.__init__(self, message)
        self.__errors = errors
    #enddef

    def errors(self):
        return self.__errors
    #enddef
#endclass

class InvalidDataError(SklikApiError):
    """Sklik API invalid data error exception
    """

    __slots__ = ["__errors"]

    def __init__(self, message, errors):
        SklikApiError.__init__(self, message)
        self.__errors = errors
    #enddef

    def errors(self):
        return self.__errors
    #enddef
#endclass

class AuthenticationError(SklikApiError):
    """Sklik API authentication error exception
    """

    pass
#endclass

class SessionError(SklikApiError):
    """Sklik API session error exception
    """

    pass
#endclass

class AccessError(SklikApiError):
    """Skik API access error exception
    """

    pass
#endclass

class NoActionWarning(SklikApiWarning):
    """Sklik API no action error exception
    """

    pass
#endclass
