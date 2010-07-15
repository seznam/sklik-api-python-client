
from methods import Methods, convert, Missing

class Campaign(object):
    """Campaign class

    Attributes:

        id: campaign ID

        name: campaign name

        dayBudget: campaign day budget

        excludedUrls: exlcluded websites

        excludedSearchServices: excluded search services

        totalBudget: campaign total budget

        totalClicks: campaign total max clicks

        adSelection: ad selection (random/weighted)

        startDate: campaign start date

        endDate: campaign end date

        status: campaign status

        context: whether show in context

        regions: campaign regions
    """
    __slots__ = [
        "id",
        "name",
        "dayBudget",
        "excludedUrls",
        "excludedSearchServices",
        "totalBudget",
        "totalClicks",
        "adSelection",
        "startDate",
        "endDate",
        "status",
        "context",
        "regions",
    ]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef
#endclass

class CampaignRegionPolygonVertex(object):
    """Campaign region polygon vertex class

    Attributes:

        latitude: vertex latitude

        longitude: vertex longitude
    """
    __slots__ = ["latitude", "longitude"]

    def __init__(self, latitude = Missing, longitude = Missing):
        self.latitude = latitude
        self.longitude = longitude
    #enddef

    def __convert__(self): pass
#endclass

class CampaignRegion(object):
    """Campaign region class

    Attributes:

        type: region type (predefined/circle/polygon)

        predefinedId: (only for "predefined" type) predefined region ID

        latitude: (only for "circle" type) circle center point latitude

        longitude: (only for "circle" type) circle center point longitude

        radius: (only for "circle" type) circle radius

        vertices: (only for "polygon" type) polygon vertices
    """
    __slots__ = ["type", "predefinedId", "latitude",
                 "longitude", "radius", "vertices"]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef

    def __convert__(self): pass
#endclass

class CampaignStat(object):
    """Campaign stat class

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

class CampaignMethods(Methods):
    @convert(Campaign)
    def checkCampaign(self, attributes):
        """Checks campaign attributes

        Arguments:

            attributes: campaign object with campaign attributes
        """
        res = self._Client__proxy.campaign.checkAttributes(
            self._Client__session, attributes)

        self.checkResult(res)
    #enddef

    @convert(Campaign)
    def createCampaign(self, attributes):
        """Creates new campaign

        Arguments:

            attributes: campaign object with campaign attributes

        Returns campaign ID
        """
        res = self._Client__proxy.campaign.create(
            self._Client__session, attributes)

        self.checkResult(res)
        return res["campaignId"]
    #enddef

    @convert(Campaign)
    def getCampaign(self, id):
        """Returns campaign attributes

        Arguments:

            id: campaign ID

        Returns campaign object
        """
        res = self._Client__proxy.campaign.getAttributes(
            self._Client__session, id)

        self.checkResult(res)

        campaign = res["campaign"]

        if "regions" in campaign and campaign["regions"] != None:
            regions = []
            for region in res["campaign"]["regions"]:
                if "vertices" in region:
                    vertices = []
                    for vertex in region["vertices"]:
                        vertices.append((vertex, CampaignRegionPolygonVertex, ))
                    #endfor
                    region["vertices"] = vertices
                #endif
                regions.append((region, CampaignRegion, ))
            #endfor
            campaign["regions"] = regions
        #endif

        return campaign
    #enddef

    @convert(Campaign)
    def removeCampaign(self, id):
        """Removes campaign

        Arguments:

            id: campaign ID
        """
        res = self._Client__proxy.campaign.remove(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Campaign)
    def restoreCampaign(self, id):
        """Restores removed campaign

        Arguments:

            id: campaign ID
        """
        res = self._Client__proxy.campaign.restore(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Campaign)
    def setCampaign(self, attributes):
        """Sets campaign attributes

        Arguments:

            attributes: campaign object with campaign attributes to set
        """
        res = self._Client__proxy.campaign.setAttributes(
            self._Client__session, attributes.pop("id"), attributes)

        self.checkResult(res)
    #enddef

    @convert(CampaignStat)
    def getCampaignStats(self, id, dateFrom, dateTo):
        """Returns campaign stats

        Arguments:

            id: campaign ID
            dateFrom: start date
            dateTo: end date

        Returns campaign stat object
        """
        res = self._Client__proxy.campaign.stats(
            self._Client__session, id, dateFrom, dateTo)

        self.checkResult(res)
        return res["stats"]
    #enddef

    @convert(Campaign)
    def listCampaigns(self, userId = None):
        """Lists campaigns for user

        Arguments:

            userId: (optional) user's ID

        Returns list of campaign objects
        """
        res = self._Client__proxy.listCampaigns(
            self._Client__session, userId)

        self.checkResult(res)
        return res["campaigns"]
    #enddef
#endclass
