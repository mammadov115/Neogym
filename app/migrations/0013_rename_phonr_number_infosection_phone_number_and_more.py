# Generated by Django 5.0.2 on 2024-03-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_contactsection_sectionimages_contact_section_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infosection',
            old_name='phonr_number',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='sectionimages',
            name='contact_section',
            field=models.ImageField(null=True, upload_to='SectionImages/ContactSection/', verbose_name='Contact Section'),
        ),
    ]