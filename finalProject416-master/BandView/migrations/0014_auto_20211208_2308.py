# Generated by Django 3.2.9 on 2021-12-09 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BandView', '0013_merge_0011_auto_20211208_1255_0012_auto_20211208_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='profilePic',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='profilePic',
        ),
    ]