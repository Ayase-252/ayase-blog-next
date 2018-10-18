"""
Test cases for models in post.py

This file contains test cases for models in post.py.
"""
from datetime import timedelta
import unittest

from django.test import TestCase
from django.utils import timezone

from ..models.category import Category
from ..models.post import Post, CallOut


class PostMethodTests(TestCase):
    """
    Test class for Post model

    Exempted method:
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up a test category for the sake of test
        """
        cls.test_cat = Category(name='test', url='test')
        cls.test_cat.save()

    def test_get_content_code_block_test(self):
        """
        Test whether markdown interpreter to deal with code block
        correctly.

        Input:'    int\n'
              '    main'
        Expected output: After '\n' is stripped
                        '<pre><code>intmain</code></pre>'
        """
        test_post = Post(title='test',
                         tags='',
                         category=self.test_cat,
                         content='    int\n'
                                 '    main')
        self.assertEqual(test_post.get_content().replace('\n', ''),
                         '<pre><code>intmain</code></pre>',
                         msg=None)

    def test_get_formatted_post(self):
        """
        Test whether get_formatted_post correctly return the
        well-formatted post
        """
        category = Category(name='h1',
                            url='')
        category.save()
        time = timezone.now()
        post = Post(title='Hello world',
                    tags='tag1,中文测试1',
                    date=time,
                    content='',  # Not for test
                    category=category)

        self.assertEqual(post.get_formatted_post(), {
            'title': 'Hello world',
            'tags': ['tag1', '中文测试1'],
            'date': time,
            'content': '',
            'category': 'h1'
        })

    def test_get_plain_content_withTags(self):
        """
        Test whether getPlainContent can correctly strip the html tags in
        content
        In the case, there ARE block element tags in content
        """
        post = Post(title='test',
                    content='This is block1\nThis is block2')
        self.assertEqual(post.get_plain_content(),
                         'This is block1\nThis is block2')

    def test_get_first_paragraph(self):
        """
        Test whether the first paragraph of post is correctly retrieved.
        Inline tags should be intact.
        """
        post = Post(title='test',
                    content='This is a `inline code`\n\nThis is second \
                    paragraph and should not be retrieved')
        self.assertEqual(
            post.get_first_paragraph(),
            r'This is a <code>inline code</code>')

    def test_get_post_no_callout_condition(self):
        """
        Test get_post in condition that post is not attached with a callout
        """
        time = timezone.now()
        post = Post(postId=1,
                    title='title',
                    tags='tag1,tag2',
                    date=time,
                    category=self.test_cat,
                    content='h1'
                    )
        self.assertEqual(post.get_post(), {
            'id': 1,
            'title': 'title',
            'tags': ['tag1', 'tag2'],
            'date': time,
            'category': 'test',
            'content': '<p>h1</p>',
            'callout': None
        })

    def test_get_post_with_callout_condition(self):
        """
        Test get_post in condition that post is attached with a callout
        """
        time = timezone.now()
        callout = CallOut(level='N', title='test callout', content='none')
        callout.save()
        post = Post(postId=1,
                    title='title',
                    tags='tag1,tag2',
                    date=time,
                    category=self.test_cat,
                    content='h1',
                    callout=callout
                    )
        self.assertEqual(post.get_post(), {
            'id': 1,
            'title': 'title',
            'tags': ['tag1', 'tag2'],
            'date': time,
            'category': 'test',
            'content': '<p>h1</p>',
            'callout': {
                'level': 'N',
                'title': 'test callout',
                'content': 'none'

            }

        })


class PostManagerTests(TestCase):
    """
    Test class for Post manager
    """

    @classmethod
    def setUpTestData(cls):
        cls.time = timezone.now()
        cls.cat_1 = Category(name='test_1', url='test-1')
        cls.cat_2 = Category(name='test_2', url='test-2')
        cls.cat_1.save()
        cls.cat_2.save()
        cls.post_1 = Post(title='title1',
                          tags='tag1,tag2',
                          date=cls.time  - timedelta(days=1),
                          category=cls.cat_1,
                          content='test content')
        cls.post_2 = Post(title='title2',
                          tags='tag1',
                          date=cls.time,
                          category=cls.cat_1,
                          content='test content')
        cls.post_1.save()
        cls.post_2.save()

    def test_get_posts_by_category(self):
        post_list = Post.data_api.get_posts_by_category(self.cat_1.url)
        self.assertQuerysetEqual(post_list,
                                 [repr(i) for i in [self.post_2, self.post_1]])
        
        post_list = Post.data_api.get_posts_by_category(self.cat_2.url)
        self.assertQuerysetEqual(post_list,
                                 [])
        
        post_list = Post.data_api.get_posts_by_category(self.cat_1.url,
                                                        limit=1)
        self.assertQuerysetEqual(post_list, [repr(self.post_2)])


    @unittest.skip('assertRaises methods is relatively complex, '
                   'time is needed to master it')
    def test_get_posts_by_category_limit_cond_negative_case(self):
        """
        Get posts_by_category_ should raise a ValueError when a
        negative number is passed to limit
        """
        # self.assertRaises(ValueError, Post.data_api.get_posts_by_category,
        #                   (self.cat_1.url, limit=-2))
        pass

    def test_get_post_by_post_id(self):
        """
        get_post_by_post_id should return the post whose id is given
        """
        post = Post.data_api.get_post_by_post_id(1)
        self.assertEqual(post, self.post_1)

    def test_get_posts_all_posts(self):
        """
        get_posts should return all posts in database in order of descending
        date in condition that limit karg is not given.
        """
        posts = Post.data_api.get_posts()
        self.assertQuerysetEqual(posts, [repr(i) for i in [self.post_2,
                                                           self.post_1]])

    def test_get_posts_limited_posts(self):
        """
        get_posts should return posts up to limit specified.
        """
        posts = Post.data_api.get_posts(limit=1)
        self.assertQuerysetEqual(posts, [repr(self.post_2)])

    def test_get_posts_given_by_from_id_with_limit(self):
        posts = Post.data_api.get_posts_by_from(2, 1)
        self.assertQuerysetEqual(posts, [repr(self.post_2)])

        posts = Post.data_api.get_posts_by_from(2, 2)
        self.assertQuerysetEqual(posts, [repr(i) for i in [self.post_2, self.post_1]])

        posts = Post.data_api.get_posts_by_from(2, 3)
        self.assertQuerysetEqual(posts, [repr(i) for i in [self.post_2, self.post_1]])


class CalloutMethodTests(TestCase):
    """
    Test class for Callout model
    """

    def test_get_callout_info_normal_cond(self):
        """
        Test get_callout_info under normal procedure
        """
        callout = CallOut(level='W', title='Draft', content='This is a draft')
        self.assertEqual(
            callout.get_callout_info(),
            {
                'level': 'W',
                'title': 'Draft',
                'content': 'This is a draft'
            })
