# Generated by Django 4.2.8 on 2024-02-07 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FpvAppMain', '0012_letters_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessontopics',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]