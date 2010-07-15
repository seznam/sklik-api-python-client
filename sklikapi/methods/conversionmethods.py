
from methods import Methods, convert, Missing

class Conversion(object):
    """Conversion class

    Attributes:

        id: conversion ID

        name: conversion name

        conversionTypeId: conversion type ID

        proto: protocol (http/https)

        color: conversion code color

        value: conversion value

        userId: user ID
    """
    __slots__ = [
        "id",
        "name",
        "conversionTypeId",
        "proto",
        "color",
        "value",
        "userId",
    ]

    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, Missing)
        #endfor
    #enddef
#endclass

class ConversionType(object):
    """Conversion type class

    Attributes:

        id: conversion type ID

        name: conversion type name
    """
    __slots__ = [
        "id",
        "name",
    ]

    def __init__(self):
        self.id = None
        self.name = None
    #enddef
#endclass

class ConversionMethods(Methods):
    @convert(Conversion)
    def checkConversion(self, attributes):
        """Checks conversion attributes

        Arguments:

            attributes: conversion object with conversion attributes
        """
        res = self._Client__proxy.conversion.checkAttributes(
            self._Client__session, attributes)

        self.checkResult(res)
    #enddef

    @convert(Conversion)
    def createConversion(self, attributes):
        """Creates new conversion

        Arguments:

            attributes: conversion object with conversion attributes

        Returns conversion ID
        """
        res = self._Client__proxy.conversion.create(
            self._Client__session, attributes)

        self.checkResult(res)
        return res["conversionId"]
    #enddef

    @convert(Conversion)
    def getConversion(self, id):
        """Returns conversion attributes

        Arguments:

            id: conversion ID

        Returns conversion object
        """
        res = self._Client__proxy.conversion.getAttributes(
            self._Client__session, id)

        self.checkResult(res)
        return res["conversion"]
    #enddef

    @convert(Conversion)
    def removeConversion(self, id):
        """Removes conversion

        Arguments:

            id: conversion ID
        """
        res = self._Client__proxy.conversion.remove(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Conversion)
    def restoreConversion(self, id):
        """Restores removed conversion

        Arguments:

            id: conversion ID
        """
        res = self._Client__proxy.conversion.restore(
            self._Client__session, id)

        self.checkResult(res)
    #enddef

    @convert(Conversion)
    def setConversion(self, attributes):
        """Sets conversion attributes

        Arguments:

            attributes: conversion object with conversion attributes to set
        """
        res = self._Client__proxy.conversion.setAttributes(
            self._Client__session, attributes.pop("id"), attributes)

        self.checkResult(res)
    #enddef

    @convert(ConversionType)
    def listConversionTypes(self):
        """Lists conversion types

        Returns list of conversion type objects
        """
        res = self._Client__proxy.listConversionTypes(
            self._Client__session)

        self.checkResult(res)
        return res["conversionTypes"]
    #enddef

    @convert(Conversion)
    def listConversions(self, userId = None):
        """Lists conversions for user

        Arguments:

            userId: (optional) user's ID

        Returns list of conversion objects
        """
        res = self._Client__proxy.listConversions(
            self._Client__session, userId)

        self.checkResult(res)
        return res["conversions"]
    #enddef
#endclass
