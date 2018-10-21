"""
Test cases for category model
"""

from django.test import TestCase

from ..models.category import Category


class CategoryManagerTest(TestCase):
    """
    Test all methods in CategoryManager
    """

    def test_get_all_categories_normal_cond(self):
        """
        Test get_all_categories in normal procedure.

        The method is expected to return all categories in a list with
        predefined format
        """
        new = Category(name='Cat_1', url='cat')
        new.save()
        new_2 = Category(name='Cat_2', url='cat1')
        new_2.save()
        cat_list = Category.data_api.get_all_categories()
        self.assertQuerysetEqual(cat_list,
                                 [repr(i) for i in [new, new_2]],
                                 ordered=False)

    def test_get_specific_category_normal_cond(self):
        """
        Test get_specific_category in normal procedure.

        The method is expected to return category whose url is identical to
        given parameter .
        """
        new = Category(name='Cat_1', url='cat')
        new.save()
        new_2 = Category(name='Cat_2', url='cat1')
        new_2.save()
        cat = Category.data_api.get_specific_category('cat1')
        self.assertEqual(cat, new_2)
