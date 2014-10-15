from markdown import markdown
from django.db import models
from autoslug import AutoSlugField


class NewsEntry(models.Model):

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    is_published = models.BooleanField('published', default=False)
    text = models.TextField(blank=True)
    text_html = models.TextField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.text_html = markdown(self.text, ['markdown.extensions.extra'])
        super(NewsEntry, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "News Entries"
