
class Config(object):
    """Sklik API client configuration class

    Attributes:

        username: username, eg. schindleruv@seznam.cz

        password: user's password

        namespace: namespace to use, eg. http://api.sklik.cz/RPC2

        debug: whether log debug messages
    """

    __slots__ = ["username", "password", "namespace", "debug"]

    def __init__(self):
        """Creates new Sklik API client configuration class instance
        """

        self.username = ""
        self.password = ""
        self.namespace = ""
        self.debug = False
    #enddef
#endclass
