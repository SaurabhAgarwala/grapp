# Generated by Django 2.0.5 on 2018-08-20 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grievances', '0004_auto_20180821_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='comments',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]