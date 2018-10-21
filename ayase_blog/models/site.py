"""
Site

Information relevant to whole site
"""

from django.db import models
import markdown

class Site(models.Model):
    """
    Site information

    Attributes:
        name        Name of site
        tagline     A short slogan of your site
        about       About page content in markdown notation
    """

    name = models.CharField(max_length=100)
    tagline = models.TextField()
    about = models.TextField()

    @classmethod
    def get_site_info(cls):
        """
        Get site information

        Return:
            site information packaged in dict

        Note:
            Because of no constraint to limit the number of instance
            in this table, the method only returns instance whose
            primary key equals 1. Therefore, if multiple instances
            exist, the first instance is valid.
        """
        site = cls.objects.get(pk=1)
        return {'name': site.name,
                'tagline': site.tagline}

    @classmethod
    def get_about(cls):
        """
        Get HTML version of content of about page

        Return:
             HTML version of content of about page

        Note:
            Because of no constraint to limit the number of instance
            in this table, the method only returns instance whose
            primary key equals 1. Therefore, if multiple instances
            exist, the first instance is valid.
        """
        site = cls.objects.get(pk=1)
        return markdown.markdown(site.about, output_format='html5')
