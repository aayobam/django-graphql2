# Generated by Django 4.0.6 on 2022-07-28 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('-created_on',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]