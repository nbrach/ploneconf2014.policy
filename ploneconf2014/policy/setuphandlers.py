# -*- coding: utf-8 -*-


from plone import api
from ploneconf2014.policy.config import PROJECTNAME
import logging

logger = logging.getLogger(PROJECTNAME)

def remove_defaults_navs(portal):
	'''Remove defaults navegations and contents'''

	items_removable = ['news','events','Members','front-page']
	for item in items_removable:
		if hasattr(portal, item):
			try:
				api.content.delete(obj=portal[item])
				logger.info("Deleted {0} item.".format(item))
			except AttributeError:
				logger.info("No {0} item detected. Hmm... strange. Continuing.".format(item)) 

def create_defaults_contents(portal):
	pass

def setupVarious(context):

    if context.readDataFile('ploneconf2014.policy_various.txt') is None:
        return

    portal = api.portal.get()
    remove_defaults_navs(portal)
    create_defaults_contents(portal)

