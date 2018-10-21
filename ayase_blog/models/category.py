"""
Category

Category defines a group of articles which have similar theme.
"""
from django.db import models


class CategoryManager(models.Manager):
    """
    Category Manager

    Augment the default manager class for category
    """

    def _get_queryset(self):
        return super(CategoryManager, self).get_queryset().all()

    def get_all_categories(self):
        """
        Retrieve all categories

        Return:
            List containing all categories
        """
        result = self._get_queryset()
        return result

    def get_specific_category(self, url):
        """
        Retrieve category specified by url

        Arguments:
            url     URL assigned to category
        """
        result = self._get_queryset().get(url=url)
        return result


class Category(models.Model):
    """
    Category class

    Category defines a group of articles which have similar theme.

    Attributes:
        categoryId  UID for a category (Primary key)
        name        Name used to display to users
        url         String used to retrieve the category by url
                    ex. /category/url
    """
    categoryId = models.AutoField(primary_key=True)
    name = models.CharField('name of category', max_length=10)
    url = models.CharField('URL of Linked Page', max_length=80, unique=True)
    data_api = CategoryManager()

    def __str__(self):
        return self.name

    def get_info(self):
        """
        Get a dict containing all data attribute
        return:
        """
        return {'id': self.categoryId,
                'name': self.name,
                'url': self.url
                }
