# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conquers', '0003_auto_20160410_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='fields',
            field=models.FileField(upload_to='archivos'),
        ),
    ]
