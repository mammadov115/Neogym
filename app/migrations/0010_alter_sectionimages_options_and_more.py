# Generated by Django 5.0.2 on 2024-03-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_sectionimages_image_alter_slider_bg_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionimages',
            options={'ordering': ['id'], 'verbose_name_plural': 'Section Images'},
        ),
        migrations.RemoveField(
            model_name='sectionimages',
            name='image',
        ),
        migrations.RemoveField(
            model_name='sectionimages',
            name='title',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='bg_image',
        ),
        migrations.AddField(
            model_name='sectionimages',
            name='healthy_section',
            field=models.ImageField(null=True, upload_to='SectionImages/HeathySection', verbose_name='Healthy Section'),
        ),
        migrations.AddField(
            model_name='sectionimages',
            name='hero_section',
            field=models.ImageField(null=True, upload_to='SectionImages/HeroSection', verbose_name='Hero Section'),
        ),
        migrations.AddField(
            model_name='sectionimages',
            name='trainer_section',
            field=models.ImageField(null=True, upload_to='SectionImages/TrainerSection', verbose_name='Trainer Section'),
        ),
        migrations.AddField(
            model_name='sectionimages',
            name='us_section',
            field=models.ImageField(null=True, upload_to='SectionImages/UsSection', verbose_name='Us Section'),
        ),
    ]