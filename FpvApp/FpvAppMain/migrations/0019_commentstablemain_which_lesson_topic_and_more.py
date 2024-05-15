# Generated by Django 4.2.8 on 2024-05-12 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FpvAppMain', '0018_alter_commentstablemain_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentstablemain',
            name='which_lesson_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FpvAppMain.lessontopics'),
        ),
        migrations.AlterField(
            model_name='commentstablemain',
            name='date_of_comment',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentstablemain',
            name='text_of_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentstablemain',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
