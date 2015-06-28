from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=2555)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)