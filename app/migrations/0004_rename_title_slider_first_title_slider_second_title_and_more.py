# Generated by Django 5.0.2 on 2024-02-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_slider_separated_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='title',
            new_name='first_title',
        ),
        migrations.AddField(
            model_name='slider',
            name='second_title',
            field=models.CharField(default='ss', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='third_title',
            field=models.CharField(default='s', max_length=150),
            preserve_default=False,
        ),
    ]
