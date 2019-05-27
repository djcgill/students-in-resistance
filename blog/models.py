from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Post(models.Model):
    """Blog post model"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # TODO: Change to user model when user app implemented
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE, default=-1)
    category = models.MantToManyField('Category', related_name='posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostImage(models.Model):
    """Blog post images"""
    post = models.ForeignKey(Post, default=None)
    image = models.ImageField(upload_to=get_image_filename, verbose_name="Image")

class Category(models.Model):
    """Post categories"""
    name = models.CharField(max_length=20)

class Issue(models.Model):
    """Table for zine issue"""
    isuue_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.issue_number)

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "images/%s-%s" % (slug, filename) 
