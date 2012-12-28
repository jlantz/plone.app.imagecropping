from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper, \
    RegistryEditForm
#from five import grok
from plone.z3cform import layout
from zope import schema
from zope.component import getUtility
from zope.interface.interface import Interface
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.utils import getToolByName
from plone.app.imagecropping import imagecroppingMessageFactory as _
#from plone.namedfile.interfaces import IAvailableSizes

#@grok.provider(IContextSourceBinder)
#def availableScales(context):
#    getAvailableSizes = queryUtility(IAvailableSizes)
#    import pdb; pdb.set_trace()
#    return getAvailableSizes().keys()
#    scales = []
#    for scale, wh in getAvailableSizes().items():
#        terms.append(SimpleVocabulary.createTerm(scale, str(scale), scale))
#    return SimpleVocabulary(scales)

class ISettings(Interface):
    """ Define settings data structure """

    large_size = schema.TextLine(
        title=_(u"Crop Editor Large Size"),
        description=_(u"width:height"),
        required=False,
        default=u"768:768",
    )

    min_size = schema.TextLine(
        title=_(u"Minimum Crop Area Size"),
        description=_(u"width:height"),
        required=False,
        default=u"50:50"
    )
    
    excluded_scales = schema.TextLine(
        title=_(u"Excluded Scales"),
        description=_(u"Comma separated list of scale names to exclude from the cropping editor"),
        required=False,
    )


class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    label = _(u"Image Cropping Settings")


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
