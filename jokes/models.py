from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
    related_name='jokes'
)
    category = models.ForeignKey(
    'Category', on_delete=models.PROTECT, related_name='jokes'
)
    tags = models.ManyToManyField('Tag', blank=True, related_name='jokes')
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

class Tag(models.Model):
    class Meta:
        ordering = ['tag']
    tag = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:tag', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag