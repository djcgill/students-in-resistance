from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from blog import models as m
from blog.models import Post, Issue, PostImage

class ModelTests(TestCase):
    def test_get_image_filename(self):
        """Testing getting image filename for upload"""
        #Arrange
        user = User.objects.create_user('testuser', 'testuser@unittest', 'testpass')
        test_post = Post(author=user,
                        issue=Issue(issue_number=1),
                        title='Test Post',
                        text='Unittest'
                        )
        test_PostImage = PostImage(post=test_post)
        filename='test_image.jpg'
        expected = 'images/test-post-test_image.jpg'

        #Act
        image_file_name = m.get_image_filename(test_PostImage, filename)

        #Assert
        self.assertEqual(expected, image_file_name)

    def test_upload_image()
        #TODO: Add tests for image uploads
        pass

