
from methods import Methods, convert

class Client(object):
    """Client class

    Attributes:

        user: user object

        foreignAccounts: list of foreign account objects
    """
    __slots__ = [
        "user",
        "foreignAccounts",
    ]

    def __init__(self):
        self.user = None
        self.foreignAccounts = []
    #enddef
#endclass

class User(object):
    """User class

    Attributes:

        id: user ID

        username: user's username with domain

        credit: user's API credit
    """
    __slots__ = [
        "username",
        "credit",
        "id",
    ]

    def __init__(self):
        self.id = None
        self.username = None
        self.credit = None
    #enddef
#endclass

class ForeignAccount(object):
    """Foreign account class

    Attributes:

        userId: user ID

        username: user's username with domain

        access: access type (r/rw)
    """
    __slots__ = [
        "userId",
        "username",
        "access",
    ]

    def __init__(self):
        self.userId = None
        self.username = None
        self.access = None
    #enddef
#endclass

class ClientMethods(Methods):
    @convert(Client)
    def getClient(self):
        """Returns client attributes

        Returns ad stat object
        """
        res = self._Client__proxy.client.getAttributes(
            self._Client__session)

        self.checkResult(res)
        return {
            "user" : (res["user"], User),
            "foreignAccounts" : (res["foreignAccounts"], ForeignAccount, )
        }
    #enddef
#endclass
