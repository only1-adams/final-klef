from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import DateTimeField
from django.forms import ModelForm

from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    STATUS=(
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=200)
    status= models.CharField(max_length=100, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Post(models.Model):
    STATUS=(
        ('True', 'True'),
        ('False', 'False'),
    )

    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by=models.ManyToManyField('Moderator')
    title1=models.CharField(max_length=100)
    title2= RichTextUploadingField()
    body = RichTextUploadingField()
    created_at= models.DateTimeField(auto_now_add=True)
    image= models.ImageField(blank=True, upload_to= 'images/')
    status= models.CharField(max_length=200, choices=STATUS)
    slug=models.SlugField(null=True, unique=True)
    Music =models.FileField(blank=True)
    video= models.FileField(blank=True)
    youtube= models.CharField(max_length=2000, blank=True, default='')
    trending_songs=models.BooleanField(blank=True)
    slide1=models.BooleanField(blank=True)
    slide2=models.BooleanField(blank=True)
    slide3=models.BooleanField(blank=True)
    frontpage=models.BooleanField(blank=True)
    tags = TaggableManager()

    def __str__(self):
            return self.title1

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'image'

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})




class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')



class Moderator(models.Model):
    name = models.CharField(max_length=200)
    created_at=DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body= RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.post.title1, self.name)



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


