"""
Test cases for ayaselibs.py
"""

from django.test import TestCase

from . import ayaselibs as libs
from .models.site import Site
from .models.category import Category


class UtilityFunctionTest(TestCase):
    """
    Test utility functions in ayaselib.py
    """
    def test_get_common_context(self):
        """
        get_common_context should return a dict containing all info required
        to render base template.
        """
        site_info = Site(name='test', tagline='Hello world')
        col_1 = Category(name='col_1', url='col-1')
        col_2 = Category(name='col_2', url='col-2')
        site_info.save()
        Category.save(col_1, col_2)
        self.assertEqual(libs.get_common_context(), {
            'site': Site.get_site_info(),
            'categories': [i.get_info()
                           for i in Category.data_api.get_all_categories()]
        })

    def test_get_common_context_with_title(self):
        """
        get_common_context is expected to return a containing all info required
        to render base template. If page_title karg is passed, the dict should
        contain a key-value pair ('page_title', page_title).
        """
        site_info = Site(name='test', tagline='Hello world')
        col_1 = Category(name='col_1', url='col-1')
        col_2 = Category(name='col_2', url='col-2')
        site_info.save()
        Category.save(col_1, col_2)
        self.assertEqual(libs.get_common_context('hello world'), {
            'site': Site.get_site_info(),
            'categories': [i.get_info()
                           for i in Category.data_api.get_all_categories()],
            'page_title': 'hello world'
        })
