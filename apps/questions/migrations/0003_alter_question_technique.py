# Generated by Django 4.0.6 on 2022-07-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_question_difficulty_alter_question_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='technique',
            field=models.IntegerField(choices=[(0, 'Multiple Choice')], default=0),
        ),
    ]
