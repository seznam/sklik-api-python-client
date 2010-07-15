
from errors import SklikApiError, AuthenticationError, ArgumentError
from xmlrpclib import ServerProxy
from methods import AdMethods, CampaignMethods, ClientMethods, \
                    ConversionMethods, GroupMethods, KeywordMethods, \
                    MiscMethods

class Client(AdMethods, CampaignMethods, ClientMethods, \
             ConversionMethods, GroupMethods, KeywordMethods, \
             MiscMethods):
    """Sklik API client class
    """

    __slots__ = ["__config", "__proxy", "__session"]

    def __init__(self, config = None):
        """Creates new Sklik API client instance

        Keyword arguments:

            config: sklik API client configuration instance
        """

        self.__session = None

        if not config:
            raise SklikApiError("No config given")
        #endif
        self.__config = config

        self.__proxy = ServerProxy(self.__config.namespace, allow_none = True)

        res = self.__proxy.client.login(
            self.__config.username,
            self.__config.password)

        if res["status"] == 400:
            raise ArgumentError(res["statusMessage"], res["errors"])
        elif res["status"] == 401:
            raise AuthenticationError(res["statusMessage"])
        elif res["status"] != 200:
            raise SklikApiError(res["statusMessage"])
        #endif

        self.__session = res["session"]
    #enddef

    def __del__(self):
        """Logs out
        """

        if self.__session == None:
            return
        #endif

        res = self.__proxy.client.logout(self.__session)

        if res["status"] == 400:
            raise ArgumentError(res["statusMessage"], res["errors"])
        elif res["status"] == 401:
            raise AuthenticationError(res["statusMessage"])
        elif res["status"] != 200:
            raise SklikApiError(res["statusMessage"])
        #endif
    #enddef
#endclass
