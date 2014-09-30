from django.utils.deconstruct import deconstructible
from django.db import models
from autoslug import AutoSlugField


@deconstructible
class Member(models.Model):
    """ Basic blog post """

    # basic information
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    birthday = models.DateField(null=True)

    # contact information
    town = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=400, null=True)
    email = models.EmailField(max_length=200, null=True)
    homephone = models.CharField(max_length=20, null=True)
    cellphone = models.CharField(max_length=20, null=True)

    # prefernces
    hobbies = models.CharField(max_length=500, null=True)
    canhelp = models.CharField(max_length=500, null=True)
    needhelp = models.CharField(max_length=500, null=True)

    slug = AutoSlugField(populate_from='first_name', max_length=200, unique=True)
    c_date = models.DateTimeField('date added', auto_now_add=True)

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['last_name']
