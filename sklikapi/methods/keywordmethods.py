
from methods import Methods, convert, Missing

class Keyword(object):
    """Keyword class

    Attributes:

        id: keyword ID

        name: keyword

        matchType: keyword match type (broad, phrase, exact, negative)

        removed: whether is removed

        status: keyword status

        disabled: whether is disabled

        cpc: keyword CPC

        url: destination URL

        created: creation date

        groupId: group ID
    """
    __slots__ = [
        "id",
        "name",
        "matchType",
        "removed",
        "status",
        "disabled",
        "cpc",
        "url",
        "created",
        "groupId",
    ]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef
#endclass

class KeywordStat(object):
    """Keyword stat class

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
        "clicks",
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

class KeywordMethods(Methods):
    @convert(Keyword)
    def checkKeyword(self, attributes):
        """Checks keyword attributes

        Arguments:

            attributes: keyword object with keyword attributes
        """
        res = self._Client__proxy.keyword.checkAttributes(
            self._Client__session, attributes)

        self.checkResult(res)
    #enddef

    @convert(Keyword)
    def createKeyword(self, attributes):
        """Creates new keyword

        Arguments:

            attributes: keyword object with keyword attributes

        Returns keyword ID
        """
        res = self._Client__proxy.keyword.create(
            self._Client__session, attributes.pop("groupId"), attributes)

        self.checkResult(res)
        return res["keywordId"]
    #enddef

    @convert(Keyword)
    def getKeyword(self, id):
        """Returns keyword attributes

        Arguments:

            id: keyword ID

        Returns keyword object
        """
        res = self._Client__proxy.keyword.getAttributes(
            self._Client__session, id)

        self.checkResult(res)
        return res["keyword"]
    #enddef

    @convert(Keyword)
    def removeKeyword(self, id):
        """Removes keyword

        Arguments:

            id: keyword ID
        """
        res = self._Client__proxy.keyword.remove(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Keyword)
    def restoreKeyword(self, id):
        """Restores removed keyword

        Arguments:

            id: keyword ID
        """
        res = self._Client__proxy.keyword.restore(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Keyword)
    def setKeyword(self, attributes):
        """Sets keyword attributes

        Arguments:

            attributes: keyword object with keyword attributes to set
        """
        res = self._Client__proxy.keyword.setAttributes(
            self._Client__session, attributes.pop("id"), attributes)

        self.checkResult(res)
    #enddef

    @convert(KeywordStat)
    def getKeywordStats(self, id, dateFrom, dateTo):
        """Returns keyword stats

        Arguments:

            id: keyword ID
            dateFrom: start date
            dateTo: end date

        Returns keyword stat object
        """
        res = self._Client__proxy.keyword.stats(
            self._Client__session, id, dateFrom, dateTo)

        self.checkResult(res)
        return res["stats"]
    #enddef

    @convert(Keyword)
    def listKeywords(self, groupId):
        """Lists keywords for group

        Arguments:

            groupId: group ID

        Returns list of keyword objects
        """
        res = self._Client__proxy.listKeywords(
            self._Client__session, groupId)

        self.checkResult(res)
        return res["keywords"]
    #enddef
#endclass
