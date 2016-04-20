# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conquers', '0005_auto_20160411_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='name',
            field=models.CharField(default='Nombre del Logro', max_length=100),
        ),
    ]
