# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('status', models.CharField(default=b'created', max_length=140, choices=[(b'draft_started', b'Draft Started'), (b'draft_finished', b'Draft Finished'), (b'created', b'Created'), (b'published', b'Published'), (b'expired_auto', b'Expired Auto'), (b'expired_manual', b'Expired Manual'), (b'deleted', b'deleted'), (b'replaced', b'replaced')])),
                ('location', models.CharField(default=b'DEFAULT VALUE', max_length=140)),
                ('brand', models.CharField(max_length=140)),
                ('model', models.CharField(max_length=140)),
                ('model_year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('type', models.CharField(default=b'suv', max_length=140, choices=[(b'small_car', b'Small Car'), (b'medium_car', b'Medium Car'), (b'large_car', b'Large Car'), (b'executive_car', b'Executive Car'), (b'luxury_car', b'Luxury Car'), (b'sports_coupes', b'Sports Coupes'), (b'multipurpose_car', b'Multipurpose Car'), (b'suv', b'SUV'), (b'family_bus', b'Family Bus')])),
                ('gear_box', models.CharField(default=b'automatic', max_length=140, choices=[(b'automatic', b'Automatic'), (b'manual', b'Manual')])),
                ('fuel', models.CharField(default=b'petrol', max_length=140, choices=[(b'petrol', b'Petrol'), (b'diesel', b'Diesel'), (b'electronic', b'Electronic'), (b'hybrid', b'Hybrid')])),
                ('description', models.CharField(max_length=2048)),
                ('price', models.IntegerField()),
                ('submit_time', models.DateTimeField(verbose_name=b'submit time')),
                ('publish_time', models.DateTimeField()),
                ('verified_media', models.IntegerField(default=0, choices=[(0, b'Nej'), (1, b'Ja')])),
                ('last_update_time', models.DateTimeField()),
                ('expire_time', models.DateTimeField()),
                ('filename', models.CharField(default=b'20160904/1.jpg', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'image', max_length=140, choices=[(b'image', b'Image'), (b'youtube', b'Video'), (b'audio', b'Audio')])),
                ('filename', models.CharField(default=b'', max_length=140)),
                ('announce_id', models.ForeignKey(to='main.Announce')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'created', max_length=140, choices=[(b'created', b'Created'), (b'validated', b'Validated'), (b'deleted', b'Deleted')])),
                ('password_hash', models.CharField(max_length=140)),
                ('email', models.EmailField(unique=True, max_length=140)),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('role', models.CharField(default=b'announcer', max_length=140, choices=[(b'announcer', b'Announcer'), (b'normal_admin', b'Normal Admin'), (b'super_admin', b'Super Admin')])),
                ('address', models.CharField(max_length=140)),
                ('city', models.CharField(max_length=140)),
                ('county', models.CharField(max_length=140)),
                ('phone_number', models.CharField(max_length=140)),
                ('birth', models.CharField(max_length=140)),
                ('reg_date', models.DateTimeField(verbose_name=b'date registered')),
            ],
        ),
        migrations.AddField(
            model_name='announce',
            name='owner_id',
            field=models.ForeignKey(default=1, to='main.User'),
        ),
    ]
