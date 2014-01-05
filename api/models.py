from django.db import models

class APIConnection(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    slug_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    headers = models.TextField(null=True, blank=True)
    params = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s-%s' % (self.name, self.slug_name)
