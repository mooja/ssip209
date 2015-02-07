from django.db import models

# Register your models here.
from django.db import models
from autoslug import AutoSlugField


class MemberNewsEntry(models.Model):
    """ A very simple news entry model """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    is_published = models.BooleanField('published', default=False)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Member Submitted News Entries"
