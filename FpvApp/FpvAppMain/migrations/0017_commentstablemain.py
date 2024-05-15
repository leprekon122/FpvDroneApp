# Generated by Django 4.2.8 on 2024-05-12 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FpvAppMain', '0016_letters_whose'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsTableMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_of_comment', models.TextField()),
                ('date_of_comment', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CommentsTableMain',
                'verbose_name_plural': 'CommentsTableMain',
            },
        ),
    ]
