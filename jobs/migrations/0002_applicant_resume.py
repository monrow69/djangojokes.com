# Generated by Django 4.2.3 on 2023-07-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', upload_to='private/resumes'),
        ),
    ]
