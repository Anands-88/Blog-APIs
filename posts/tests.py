from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class BlogTests(TestCase): # class BlogTests inherits from TestCase
    
    @classmethod # class method decorator, is used to declare a method in the class as class method, can be called using classname(here blogtest).classmethod() 
    def setUpTestData(cls): # cls or self or any
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1') # Can write anything
        self.assertEqual(title, 'Blog title') #
        self.assertEqual(body, 'Body content...') # 

class CommentTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):

        testuser2 = User.objects.create_user(
            username = 'testuser2', password = '123abc')
        testuser2.save()

        test_comment = Comment.objects.create(
            body = 'Body content')
        test_comment.save()

    def test_blogComment(self):
        comment = Comment.objects.get(id=1)
        body = f'{comment.body}'
        self.assertEqual(body,'Body content'))
        