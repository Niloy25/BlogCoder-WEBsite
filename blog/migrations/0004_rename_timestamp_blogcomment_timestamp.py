# Generated by Django 3.2.5 on 2021-08-24 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='timestamp',
            new_name='timeStamp',
        ),
    ]