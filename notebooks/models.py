from django.db import models
from django.db.models.deletion import SET_NULL
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note_topic = models.CharField(max_length=200, blank=False)
    note_body = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    
    
    class Meta:
     ordering = ('-created_at', )
    
    
    def __str__(self) -> str:
        return self.note_topic
        
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.note_topic)
        super(Notes, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
         return reverse('notes:note-detail', kwargs={'slug' : self.slug})
