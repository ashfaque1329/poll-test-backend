from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class Poll(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    #slug_poll = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    '''def save(self, *args, **kwargs):
        self.slug_poll = slugify(self.title)
        super(Poll, self).save(*args, **kwargs)'''

    class Meta:
        verbose_name_plural = 'Polls'


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(
        Poll, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #slug_option = models.SlugField(blank=True)

    def __str__(self):
        return self.option_text

    '''def save(self, *args, **kwargs):
        self.slug_option = slugify(self.option_text)
        super(Option, self).save(*args, **kwargs)'''

    class Meta:
        verbose_name_plural = 'Options'
