from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})