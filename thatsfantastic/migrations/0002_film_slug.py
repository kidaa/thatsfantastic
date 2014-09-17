# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thatsfantastic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(unique=True, null=True, max_length=140, blank=True),
            preserve_default=True,
        ),
    ]
