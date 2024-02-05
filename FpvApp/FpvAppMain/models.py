"""import block"""
from django.db import models
from django.contrib.auth.models import User


class TagsModel(models.Model):
    """Models for list of tags for topics"""
    list_of_tags = (("repair", "repair"),
                    ("video", "video"),
                    ("flying", "flying"),
                    ("education", "education"),
                    ("inventing", "inventing"),
                    )
    tag = models.CharField(choices=list_of_tags, max_length=100, null=True, blank=True)
    tag_1 = models.CharField(choices=list_of_tags, max_length=100, null=True, blank=True)
    tag_2 = models.CharField(choices=list_of_tags, max_length=100, null=True, blank=True)
    tag_3 = models.CharField(choices=list_of_tags, max_length=100, null=True, blank=True)
    tag_4 = models.CharField(choices=list_of_tags, max_length=100, null=True, blank=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """class for cho0sing name of table"""
        verbose_name = 'TagsModel'
        verbose_name_plural = 'TagsModel'


class LessonTopics(models.Model):
    """Model for lessons page"""

    list_of_tags = (("repair", "repair"),
                    ("video", "video"),
                    ("flying", "flying"),
                    ("education", "education"),
                    ("inventing", "inventing"),
                    )

    objects = None
    tittle = models.CharField(max_length=255)
    pic = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_1 = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_2 = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_3 = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_4 = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_5 = models.ImageField(null=True, blank=True, upload_to='pic/')
    pic_6 = models.ImageField(null=True, blank=True, upload_to='pic/')
    add_date = models.DateTimeField(auto_now=True)
    video = models.FileField(null=True, blank=True, upload_to="video")
    text = models.TextField(null=True, blank=True)
    text_1 = models.TextField(null=True, blank=True)
    text_2 = models.TextField(null=True, blank=True)
    text_3 = models.TextField(null=True, blank=True)
    text_4 = models.TextField(null=True, blank=True)
    text_5 = models.TextField(null=True, blank=True)
    text_6 = models.TextField(null=True, blank=True)
    # tag_name_0 = models.ForeignKey(TagsModel, on_delete=models.CASCADE, blank=True, null=True)
    tag_1 = models.CharField(choices=list_of_tags, null=True, blank=True, max_length=100)
    tag_2 = models.CharField(choices=list_of_tags, null=True, blank=True, max_length=100)
    tag_3 = models.CharField(choices=list_of_tags, null=True, blank=True, max_length=100)
    tag_4 = models.CharField(choices=list_of_tags, null=True, blank=True, max_length=100)
    tag_5 = models.CharField(choices=list_of_tags, null=True, blank=True, max_length=100)

    class Meta:  # pylint: disable=too-few-public-methods
        """class for choosing name of table"""
        verbose_name = 'LessonTopics'
        verbose_name_plural = 'LessonTopics'


class Letters(models.Model):
    """class for letters"""

    status = (("unread", "unread"),
              ("read", "read")
              )

    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    destination = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status, default="unread")

    class Meta:  # pylint: disable=too-few-public-methods
        """class for choosing name of table"""
        verbose_name = 'Letters'
        verbose_name_plural = 'Letters'
