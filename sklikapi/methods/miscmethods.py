
from methods import Methods, convert

class SearchService(object):
    """Search service class

    Attributes:

        id: search service ID

        name: search service name
    """
    __slots__ = ["id", "name"]

    def __init__(self):
        self.id = None
        self.name = None
    #enddef
#endclass

class Region(object):
    """Region class

    Attributes:

        id: region ID

        name: region name
    """
    __slots__ = ["id", "name"]

    def __init__(self):
        self.id = None
        self.name = None
    #enddef
#endclass

class MiscMethods(Methods):
    @convert(SearchService)
    def listSearchServices(self):
        """Lists search services

        Returns list of search service objects
        """
        res = self._Client__proxy.listSearchServices(
            self._Client__session)

        self.checkResult(res)
        return res["searchServices"]
    #enddef

    @convert(Region)
    def listPredefinedRegions(self):
        """Lists predefined regions

        Returns list of region objects
        """

        res = self._Client__proxy.listPredefinedRegions(
            self._Client__session)

        self.checkResult(res)
        return res["predefinedRegions"]
    #endif
#endclass
