# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enginetoday.image.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', enginetoday.image.fields.AjaxImageField()),
                ('thumbnail', enginetoday.image.fields.AjaxImageField()),
            ],
        ),
    ]
