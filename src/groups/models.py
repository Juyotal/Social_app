from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
import misaka

from django import template
register = template.Library()


class Group (models.Model):
    name = models.CharField(max_length=200, unique= True)
    slug = models.SlugField(allow_unicode= True, unique= True)
    description = models.TextField (blank = True, default= '')
    description_html = models.TextField(editable= False, default= '', blank= True)
    members = models.ManyToManyField(User, through= 'GroupMember')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})
    
    class Meta: 
        ordering = ["name"]

class GroupMember(models.Model):
    groups = models.ForeignKey (Group, on_delete=models.CASCADE, related_name = 'memberships')
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name = 'user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('groups', 'user')