from django.db import models
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog_profile(models.Model):
    title=models.CharField(max_length=200)
    description= models.CharField(max_length=255, null=True)
    keywords= models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=400)
    instagram = models.CharField(blank=True, max_length=400)
    twitter = models.CharField(blank=True, max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    privay = RichTextUploadingField(blank=True)
    about_klef = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title 


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Pending', 'Pending'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']