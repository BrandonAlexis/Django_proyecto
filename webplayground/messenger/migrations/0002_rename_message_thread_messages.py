# Generated by Django 5.1.7 on 2025-03-19 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='Message',
            new_name='messages',
        ),
    ]
