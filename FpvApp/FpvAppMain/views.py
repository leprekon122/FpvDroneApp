"""import block"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import LessonTopics, TagsModel, Letters
from .views_logic import DetailInfo, SearchByTitle, FindByTagName, LettersLogic, DataForPage


def login_page(request):
    """Login page logic"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main_page')

    return render(request, "FpvAppMain/start_page.html")


class MainPage(APIView):
    """Main page logic"""

    @staticmethod
    def get(request):
        """Main page logic get  req"""

        logic_set = DataForPage(request.user)
        data = logic_set.data()

        return render(request, 'FpvAppMain/main_page.html', data)


class LessonsPage(APIView):
    """LessonsPage logic"""

    @staticmethod
    def get(request):
        """LessonsPage logic get req"""
        detail_info = request.GET.get('detail')
        search_by_title = request.GET.get('search_by_title')
        remove_filter = request.GET.get('remove_filter')
        read = request.GET.get('read')

        # ===find by tags===
        tag_1 = request.GET.get('tag_1')
        tag_2 = request.GET.get('tag_2')
        tag_3 = request.GET.get('tag_3')
        tag_4 = request.GET.get('tag_4')
        tag_5 = request.GET.get('tag_5')
        # ===================

        if read:
            logic = LettersLogic(username=request.user, read=read)
            logic.read_letters()

            return render(request, 'FpvAppMain/lessons_page.html', logic.data())

        if any([tag_1, tag_2, tag_3, tag_4, tag_5]):
            data = [tag_1, tag_2, tag_3, tag_4, tag_5]
            for elem in range(5):
                try:
                    data.remove(None)
                except Exception:
                    pass
            logic = FindByTagName(data)
            data = {'model': logic.make_query,
                    'flag': 0,
                    "filter_name": logic.filter_name,
                    'filter': 1
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        if remove_filter:
            data = {"model": LessonTopics.objects.all().values(),
                    "tags": TagsModel.objects.all().values(),
                    "flag": 0,
                    "filter": 0,
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        if search_by_title:
            title = request.GET.get('find_by_title')
            logic = SearchByTitle(title)
            data = {"model": logic.make_query(),
                    "flag": 0,
                    "filter_name": logic.filter_name,
                    "filter": 1}
            return render(request, 'FpvAppMain/lessons_page.html', data)
        if detail_info:
            logic = DetailInfo(detail_info).make_query()
            data = {"model": logic,
                    "flag": 1,
                    "filter": 0,
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)
        logic_set = DataForPage(request.user)
        data = logic_set.data()
        return render(request, 'FpvAppMain/lessons_page.html', data)

    @staticmethod
    def post(request):
        """function for post request in lessons page"""

        send_letters = request.POST.get
        username = request.POST.get('username')
        text_letters = request.POST.get('text_letters')
        title_letters = request.POST.get('title_letters')

        if all([title_letters, send_letters, username]):
            username = User.objects.filter(username=username).values()[0]["id"]
            Letters.objects.create(title=title_letters, text=text_letters, destination_id=username)
            data = {"model": LessonTopics.objects.all().values(),
                    "letters_model": Letters.objects.filter(destination=request.user).values(),
                    "flag": 0,
                    "filter": 0,
                    'letters_status': 1,
                    "count_letters": len(Letters.objects.filter(status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        title = request.POST.get('title')
        photo_set = []
        video = request.FILES['video']
        photo = request.POST.get('photo')
        for el in range(int(photo)):
            num = el + 1
            pic = request.FILES[f"pic_{num}"]
            photo_set.append(pic)
        add_date = request.POST.get('add_date')
        text = request.POST.get('text')
        # text_1 = request.POST.get('text_1')
        # text_2 = request.POST.get('text_2')
        # text_3 = request.POST.get('text_3')
        # text_4 = request.POST.get('text_4')
        # text_5 = request.POST.get('text_5')
        # text_6 = request.POST.get('text_6')
        tag_1 = request.POST.get('tag_1')
        tag_2 = request.POST.get('tag_2')
        tag_3 = request.POST.get('tag_3')
        tag_4 = request.POST.get('tag_4')
        tag_5 = request.POST.get('tag_5')

        if len(photo_set) == 1:
            LessonTopics.objects.create(tittle=title, video=video, pic=photo_set[0],
                                        add_date=add_date, text=text,
                                        tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5)
        if len(photo_set) == 2:
            LessonTopics.objects.create(tittle=title, video=video, pic=photo_set[0], pic_1=photo_set[1],
                                        add_date=add_date, text=text,
                                        tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5)
        if len(photo_set) == 3:
            LessonTopics.objects.create(tittle=title, video=video, pic=photo_set[0], pic_1=photo_set[1],
                                        pic_2=photo_set[2], add_date=add_date, text=text,
                                        tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5)
        if len(photo_set) == 4:
            LessonTopics.objects.create(tittle=title, video=video, pic=photo_set[0], pic_1=photo_set[1],
                                        pic_2=photo_set[2], pic_3=photo_set[3], add_date=add_date, text=text,
                                        tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5)
        if len(photo_set) == 5:
            LessonTopics.objects.create(tittle=title, video=video, pic=photo_set[0], pic_1=photo_set[1],
                                        pic_2=photo_set[2], pic_3=photo_set[3], pic_4=photo_set[4],
                                        add_date=add_date, text=text, tag_1=tag_1, tag_2=tag_2, tag_3=tag_3,
                                        tag_4=tag_4, tag_5=tag_5)

        data = {"model": LessonTopics.objects.all().values(),
                "flag": 0,
                "filter": 0,
                "count_letters": len(Letters.objects.filter(status="unread"))
                }
        return render(request, 'FpvAppMain/lessons_page.html', data)
