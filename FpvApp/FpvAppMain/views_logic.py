"""import block"""
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


class DataForPage: # pylint: disable=too-few-public-methods
    """class for build data set for lesson page"""

    def __init__(self, username):
        self.username = username

    def data(self):
        """return data set"""
        data = {"model": LessonTopics.objects.all().values(),
                "letters_model": Letters.objects.filter(destination=self.username).values(),
                "flag": 0,
                "filter": 0,
                "count_letters": len(Letters.objects.filter(status="unread"))
                }
        return data
