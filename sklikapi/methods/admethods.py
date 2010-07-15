
from methods import Methods, convert, Missing

class Ad(object):
    """Ad class

    Attributes:

        id: ad ID

        creative1: ad title

        creative2: ad line 1

        creative3: ad line 2

        clickthruUrl: destination URL

        clickthruText: visible URL

        removed: whether is removed

        status: ad status

        created: creation date

        groupId: group ID
    """
    __slots__ = [
        "id",
        "creative1",
        "creative2",
        "creative3",
        "clickthruUrl",
        "clickthruText",
        "removed",
        "status",
        "created",
        "groupId",
    ]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef
#endclass

class AdStat(object):
    """Ad stat class

    Attributes:

        conversions: conversion count

        transactions: transaction count

        money: money sum

        avgPosition: average position

        impressions: impression count

        clicks: click count
    """
    __slots__ = [
        "conversions",
        "transactions",
        "money",
        "avgPosition",
        "impressions",
        "clicks"
    ]

    def __init__(self):
        self.conversions = 0
        self.transactions = 0
        self.money = 0
        self.avgPosition = 0
        self.impressions = 0
        self.clicks = 0
    #enddef
#endclass

class AdMethods(Methods):
    @convert(Ad)
    def checkAd(self, attributes):
        """Checks ad attributes

        Arguments:

            attributes: ad object with ad attributes
        """
        res = self._Client__proxy.ad.checkAttributes(
            self._Client__session, attributes)

        self.checkResult(res)
    #enddef

    @convert(Ad)
    def createAd(self, attributes):
        """Creates new ad

        Arguments:

            attributes: ad object with ad attributes

        Returns ad ID
        """
        res = self._Client__proxy.ad.create(
            self._Client__session, attributes.pop("groupId"), attributes)

        self.checkResult(res)
        return res["adId"]
    #enddef

    @convert(Ad)
    def getAd(self, id):
        """Returns ad attributes

        Arguments:

            id: ad ID

        Returns ad object
        """
        res = self._Client__proxy.ad.getAttributes(
            self._Client__session, id)

        self.checkResult(res)
        return res["ad"]
    #enddef

    @convert(Ad)
    def removeAd(self, id):
        """Removes ad

        Arguments:

            id: ad ID
        """
        res = self._Client__proxy.ad.remove(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Ad)
    def restoreAd(self, id):
        """Restores removed ad

        Arguments:

            id: ad ID
        """
        res = self._Client__proxy.ad.restore(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Ad)
    def setAd(self, attributes):
        """Sets ad attributes

        Arguments:

            attributes: ad object with ad attributes to set
        """
        res = self._Client__proxy.ad.setAttributes(
            self._Client__session, attributes.pop("id"), attributes)

        self.checkResult(res)
    #enddef

    @convert(AdStat)
    def getAdStats(self, id, dateFrom, dateTo):
        """Returns ad stats

        Arguments:

            id: ad ID
            dateFrom: start date
            dateTo: end date

        Returns ad stat object
        """
        res = self._Client__proxy.ad.stats(
            self._Client__session, id, dateFrom, dateTo)

        self.checkResult(res)
        return res["stats"]
    #enddef

    @convert(Ad)
    def listAds(self, groupId):
        """Lists ads in group

        Arguments:

            groupId: group ID for listing

        Returns list of group objects
        """

        res = self._Client__proxy.listAds(
            self._Client__session, groupId)

        self.checkResult(res)
        return res["ads"]
    #enddef
#endclass
