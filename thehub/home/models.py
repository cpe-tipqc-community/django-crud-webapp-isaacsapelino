from django.db import models
from login.models import Profile
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)
	desc = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, null=True, blank=True)
	post = models.TextField()
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date_posted = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=255, unique=True)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
