
from methods import Methods, convert, Missing

class Group(object):
    """Group class

    Attributes:

        id: group ID

        name: group name

        campaignId: campaign ID

        status: campaign status

        removed: whether is removed

        cpc: group CPC

        cpcContext: group CPC for context

        created: creation date
    """
    __slots__ = [
        "id",
        "name",
        "campaignId",
        "status",
        "removed",
        "cpc",
        "cpcContext",
        "created",
    ]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef
#endclass

class GroupStat(object):
    """Group stat class

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

class GroupMethods(Methods):
    @convert(Group)
    def checkGroup(self, attributes):
        """Checks group attributes

        Arguments:

            attributes: group object with group attributes
        """
        res = self._Client__proxy.group.checkAttributes(
            self._Client__session, attributes)

        self.checkResult(res)
    #enddef

    @convert(Group)
    def createGroup(self, attributes):
        """Creates new group

        Arguments:

            attributes: group object with group attributes

        Returns group ID
        """
        res = self._Client__proxy.group.create(
            self._Client__session, attributes.pop("campaignId"), attributes)

        self.checkResult(res)
        return res["groupId"]
    #enddef

    @convert(Group)
    def getGroup(self, id):
        """Returns group attributes

        Arguments:

            id: group ID

        Returns group object
        """
        res = self._Client__proxy.group.getAttributes(
            self._Client__session, id)

        self.checkResult(res)
        return res["group"]
    #enddef

    @convert(Group)
    def removeGroup(self, id):
        """Removes group

        Arguments:

            id: group ID
        """
        res = self._Client__proxy.group.remove(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Group)
    def restoreGroup(self, id):
        """Restores removed group

        Arguments:

            id: group ID
        """
        res = self._Client__proxy.group.restore(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Group)
    def setGroup(self, attributes):
        """Sets group attributes

        Arguments:

            attributes: group object with group attributes to set
        """
        res = self._Client__proxy.group.setAttributes(
            self._Client__session, attributes.pop("id"), attributes)

        self.checkResult(res)
    #enddef

    @convert(GroupStat)
    def getGroupStats(self, id, dateFrom, dateTo):
        """Returns group stats

        Arguments:

            id: group ID
            dateFrom: start date
            dateTo: end date

        Returns group stat object
        """
        res = self._Client__proxy.group.stats(
            self._Client__session, id, dateFrom, dateTo)

        self.checkResult(res)
        return res["stats"]
    #enddef

    @convert(Group)
    def listGroups(self, campaignId):
        """Lists groups for campaign

        Arguments:

            campaignId: campaign ID

        Returns list of group objects
        """
        res = self._Client__proxy.listGroups(
            self._Client__session, campaignId)

        self.checkResult(res)
        return res["groups"]
    #enddef
#endclass
