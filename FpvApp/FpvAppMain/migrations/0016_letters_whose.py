# Generated by Django 4.2.8 on 2024-02-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FpvAppMain', '0015_alter_lessontopics_dislike_alter_lessontopics_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='letters',
            name='whose',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
