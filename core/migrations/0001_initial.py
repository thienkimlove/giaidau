# Generated by Django 2.0.3 on 2018-04-03 03:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', core.models.GeneralCharField(max_length=191)),
                ('content', core.models.GeneralCharField(max_length=191)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='siteslug',
            unique_together={('slug', 'content')},
        ),
    ]