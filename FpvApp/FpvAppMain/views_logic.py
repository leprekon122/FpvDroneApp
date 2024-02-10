"""import block"""
from django.contrib.auth.models import User
from django.db.models import Q
from .models import LessonTopics, TagsModel, Letters


class DetailInfo:  # pylint: disable=too-few-public-methods
    """Detail info by topics in LessonsPage"""

    def __init__(self, id_query):
        self.id_query = id_query

    def make_query(self):
        """function for building query"""
        query = LessonTopics.objects.filter(id=self.id_query).values()
        return query


class SearchByTitle:  # pylint: disable=too-few-public-methods
    """Filter for searching by title in lessons page """

    def __init__(self, title):
        self.title = title

    def make_query(self):
        """function for building query"""
        query = LessonTopics.objects.filter(tittle__icontains=self.title).values()
        return query

    def filter_name(self):
        """return filter name"""
        return "Search_by_date"


class FindByTagName:  # pylint: disable=too-few-public-methods
    """Searching by tag name in lessons page"""

    def __init__(self, *args):
        self.tag = [*args]
        self.data = []

    @property
    def make_query(self):
        """Making query func"""
        for el in LessonTopics.objects.values():
            if any([(el['tag_1'] in self.tag[0]), (el['tag_2'] in self.tag[0]), (el['tag_3'] in self.tag[0]),
                    (el['tag_4'] in self.tag[0]),
                    (el['tag_5'] in self.tag[0])]):
                self.data.append(el)
        return self.data

    @property
    def filter_name(self):
        """return filter name"""
        return "Search_by_tag"


class LettersLogic:
    """letters  logic class"""

    def __init__(self, read, username):
        self.read = read
        self.username = username

    def read_letters(self):
        """change status of letters"""
        Letters.objects.filter(id=self.read).update(status='read')

    def data(self):
        """return data for page"""
        data = {"model": LessonTopics.objects.all().values(),
                "letters_model": Letters.objects.filter(destination=self.username).values(),
                "flag": 0,
                "filter": 0,
                'letters_status': 1,
                "count_letters": len(Letters.objects.filter(status="unread"))
                }
        return data


class DataForPage:  # pylint: disable=too-few-public-methods
    """class for build data set for lesson page"""

    def __init__(self, username):
        self.username = username

    def data(self):
        """return data set"""
        data = {"model": LessonTopics.objects.all().values(),
                "letters_model": Letters.objects.filter(destination=self.username).values(),
                "flag": 0,
                "filter": 0,
                "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=self.username).values('id')[0]['id'],
                        status="unread"))
                }
        return data


class CountLikes:  # pylint: disable=too-few-public-methods
    """Class for counting likes"""

    def __init__(self, id_topic, like):
        self.like = int(like)
        self.id_topic = id_topic

    def repair_likes(self):
        """function for making update query"""
        LessonTopics.objects.filter(id=self.id_topic).update(like=self.like + 1)


class LessonsPagePost:  # pylint: disable=too-few-public-methods
    """class for working with post request from lessons page"""

    def __init__(self, title, photo_set, video, photo, add_date, text, text_1, text_2, text_3, text_4, tag_1, tag_2,
                 tag_3, tag_4, tag_5, author):
        self.title = title
        self.photo_set = photo_set
        self.video = video
        self.photo = photo
        self.add_date = add_date
        self.text = text
        self.text_1 = text_1
        self.text_2 = text_2
        self.text_3 = text_3
        self.text_4 = text_4
        self.tag_1 = tag_1
        self.tag_2 = tag_2
        self.tag_3 = tag_3
        self.tag_4 = tag_4
        self.tag_5 = tag_5
        self.author = author

    @property
    def create_article(self):
        """function for creating article  in LessonTopics model"""
        if int(self.photo) == 0:
            LessonTopics.objects.create(tittle=self.title, video=self.video, add_date=self.add_date, text=self.text,
                                        text_1=self.text_1, text_2=self.text_2, text_3=self.text_3, text_4=self.text_4,
                                        tag_1=self.tag_1, tag_2=self.tag_2, tag_3=self.tag_3, tag_4=self.tag_4,
                                        tag_5=self.tag_5, author=self.author)
        if len(self.photo_set) == 1:
            LessonTopics.objects.create(tittle=self.title, video=self.video, pic=self.photo_set[0],
                                        add_date=self.add_date, text=self.text, text_1=self.text_1, text_2=self.text_2,
                                        text_3=self.text_3, text_4=self.text_4, tag_1=self.tag_1, tag_2=self.tag_2,
                                        tag_3=self.tag_3, tag_4=self.tag_4, tag_5=self.tag_5, author=self.author)
        if len(self.photo_set) == 2:
            LessonTopics.objects.create(tittle=self.title, video=self.video, pic=self.photo_set[0],
                                        pic_1=self.photo_set[1], add_date=self.add_date, text=self.text,
                                        text_1=self.text_1, text_2=self.text_2, text_3=self.text_3, text_4=self.text_4,
                                        tag_1=self.tag_1, tag_2=self.tag_2, tag_3=self.tag_3, tag_4=self.tag_4,
                                        tag_5=self.tag_5, author=self.author)
        if len(self.photo_set) == 3:
            LessonTopics.objects.create(tittle=self.title, video=self.video, pic=self.photo_set[0],
                                        pic_1=self.photo_set[1], pic_2=self.photo_set[2], add_date=self.add_date,
                                        text=self.text, text_1=self.text_1, text_2=self.text_2, text_3=self.text_3,
                                        text_4=self.text_4, tag_1=self.tag_1, tag_2=self.tag_2, tag_3=self.tag_3,
                                        tag_4=self.tag_4, tag_5=self.tag_5, author=self.author)
        if len(self.photo_set) == 4:
            LessonTopics.objects.create(tittle=self.title, video=self.video, pic=self.photo_set[0],
                                        pic_1=self.photo_set[1], pic_2=self.photo_set[2], pic_3=self.photo_set[3],
                                        add_date=self.add_date, text=self.text, text_1=self.text_1, text_2=self.text_2,
                                        text_3=self.text_3, text_4=self.text_4, tag_1=self.tag_1, tag_2=self.tag_2,
                                        tag_3=self.tag_3, tag_4=self.tag_4, tag_5=self.tag_5, author=self.author)
        if len(self.photo_set) == 5:
            LessonTopics.objects.create(tittle=self.title, video=self.video, pic=self.photo_set[0],
                                        pic_1=self.photo_set[1], pic_2=self.photo_set[2], pic_3=self.photo_set[3],
                                        pic_4=self.photo_set[4], add_date=self.add_date, text=self.text,
                                        text_1=self.text_1, text_2=self.text_2, text_3=self.text_3, text_4=self.text_4,
                                        tag_1=self.tag_1, tag_2=self.tag_2, tag_3=self.tag_3, tag_4=self.tag_4,
                                        tag_5=self.tag_5, author=self.author)

        data = {"model": LessonTopics.objects.all().values(),
                "flag": 0,
                "filter": 0,
                "count_letters": len(Letters.objects.filter(status="unread")),
                }

        return data


class CreatingLetter:  # pylint: disable=too-few-public-methods

    def __init__(self, username, title_letters, text_letters, current_username):
        self.username = username
        self.title_letters = title_letters
        self.text_letters = text_letters
        self.current_username = current_username

    @property
    def create_letter(self):
        """Make create query in model"""

        Letters.objects.create(title=self.title_letters, text=self.text_letters, destination_id=self.username,
                               whose=self.current_username)

        data = {"model": LessonTopics.objects.all().values(),
                "letters_model": Letters.objects.filter(destination=self.current_username).values(),
                "flag": 0,
                "filter": 0,
                'letters_status': 1,
                "count_letters": len(Letters.objects.filter(status="unread"))
                }

        return data
