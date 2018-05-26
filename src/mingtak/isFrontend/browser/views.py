# -*- coding: utf-8 -*-
from mingtak.isFrontend import _
from Products.Five.browser import BrowserView
from plone import api
from zope.component import queryUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer


class IsFrontend(BrowserView):

    def __call__(self, currentView):
        request = self.request
        portal = api.portal.get()

        normalizer = queryUtility(IIDNormalizer)
        permissions = []
        for permission, roles in getattr(currentView, '__ac_permissions__', tuple()):
            permissions.append(normalizer.normalize(permission))
        if 'none' in permissions or 'view' in permissions:
            return True
        else:
            return False
