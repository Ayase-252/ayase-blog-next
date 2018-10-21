"""
Library of Utility Functions

This module contains some utility functions.
"""

import re

from .models.site import Site
from .models.category import Category


def strip_html_tags(text):
    """
    Strip HTML tags from text generated from Markdown script

    :param text: text in HTML
    :return: text without HTML Tags
    """
    htmlPattern = re.compile(r'<\w+>|</\w+>')
    return htmlPattern.sub('', text)


def get_common_context(page_title=None):
    """
    Get common context for rendering template, such as site name and columns
    for navigation.
    """
    context = {
        'site': Site.get_site_info(),
        'categories': [i.get_info()
                       for i in Category.data_api.get_all_categories()]
        }
    if page_title is not None:
        context['page_title'] = page_title
    return context
