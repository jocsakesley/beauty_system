# Generated by Django 3.2.6 on 2021-08-24 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210824_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': 'Business', 'verbose_name_plural': 'Business'},
        ),
        migrations.AlterModelOptions(
            name='professional',
            options={'verbose_name': 'Professional'},
        ),
    ]
