"""
Test cases for site model
"""

from django.test import TestCase

from ..models.site import Site

class SiteMethodTests(TestCase):
    """
    Test class for site model

    Exempted method:
    """

    def test_get_site_info_normal_cond(self):
        """
        Test get_site_info method in normal operating condition,
        namely, there is only single instance in Site table.
        """
        Site.objects.create(name='test web',
                            tagline='may there be no bug')
        self.assertEqual(Site.get_site_info(),
                         {'name': 'test web',
                          'tagline': 'may there be no bug'})

    def test_get_site_info_multiple_instance_cond(self):
        """
        Test get_site_info method in condition where multiple
        instances exist in Site table.

        Method should return the first instance.
        """
        Site.objects.create(name='test web',
                            tagline='may there be no bug')
        Site.objects.create(name='test web 2',
                            tagline='no no do not return this')
        self.assertEqual(Site.get_site_info(),
                         {'name': 'test web',
                          'tagline': 'may there be no bug'})
