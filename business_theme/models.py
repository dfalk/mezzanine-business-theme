from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged, SiteRelated
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


LOREM_STRING = "Donec id elit non mi porta gravida at eget metus. "\
        "Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum "\
        "nibh, ut fermentum massa justo sit amet risus. Etiam porta sem "\
        "malesuada magna mollis euismod. Donec sed odio dui."


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(_("Heading"), max_length=200,
        default=_("Hello, world!"),
        help_text=_("The heading under the icon blurbs"))
    subheading = models.CharField(_("Subheading"), max_length=1000,
        default=_("This is a template for a simple marketing or "\
        "informational website. It includes a large callout called "\
        "a jumbotron and three supporting pieces of content. Use it "\
        "as a starting point to create something more unique."),
        help_text=_("The subheading just below the heading"))
    heading_button = models.CharField(_("Button text"), max_length=200,
        default=_("Learn more"))
    heading_link = models.CharField(_("Button link"), max_length=200,
        blank=True, default=_("#"),
        help_text=_("Optional, if provided the heading button will be visible."))
    iconbox_heading = models.CharField(_("Iconbox heading"), max_length=200,
        null=True, blank=True,
        help_text=_("Optional, if provided the iconbox heading will be visible."))
    content_heading = models.CharField(_("Content heading"), max_length=200,
        default=_("About us"))

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("business_theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("business_theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(_("Title"), max_length=200,
        default=_("Heading"))
    content = models.TextField(_("Content"),
        default=LOREM_STRING)
    link = models.CharField(_("Link"), max_length=2000, blank=True,
        help_text=_("Optional, if provided clicking the blurb will go here."))


class SitewideContent(SiteRelated):
    box_one_title = models.CharField(_("Box 1 title"), max_length=200, default=_("About"))
    box_one_content = RichTextField(_("Box 1 content"), default=LOREM_STRING)
    box_two_title = models.CharField(_("Box 2 title"), max_length=200, default=_("Contact Us"))
    box_two_content = RichTextField(_("Box 2 content"), default=LOREM_STRING)
    box_three_title = models.CharField(_("Box 3 title"), max_length=200, default=_("Social links"))
    box_three_content = RichTextField(_("Box 3 content"), default=LOREM_STRING)

    class Meta:
        verbose_name = _("Sitewide Content")
        verbose_name_plural = _("Sitewide Content")