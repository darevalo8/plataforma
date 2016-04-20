# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conquers', '0002_activity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='fields',
            field=models.FileField(upload_to=''),
        ),
    ]
