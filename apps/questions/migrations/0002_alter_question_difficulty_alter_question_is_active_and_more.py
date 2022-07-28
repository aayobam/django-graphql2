# Generated by Django 4.0.6 on 2022-07-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Fundamental1'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='technique',
            field=models.CharField(choices=[(0, 'Multiple Choice')], default=0, max_length=255),
        ),
    ]