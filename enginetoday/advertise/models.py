from django.db import models

from enginetoday.image.fields import AjaxImageField


class Advertise(models.Model):
    image = AjaxImageField()
    thumbnail = AjaxImageField(upload_to='thumbnails', max_height=200,
                               max_width=200, crop=False)

    def __unicode__(self):
        return unicode(self.thumbnail)

    def __str__(self):
        return str(self.thumbnail)

    @property
    def url(self):
        return self.thumbnail.url

    @property
    def path(self):
        return self.thumbnail.path
