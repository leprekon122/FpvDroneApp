"""import block"""
import random
import requests

from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import LessonTopics, TagsModel, Letters, CommentsTableMain
from .views_logic import DetailInfo, SearchByTitle, FindByTagName, LettersLogic, DataForPage, CountLikes, \
    LessonsPagePost, CreatingLetter, RewriteArticle, CreateComments, CreateResponseComment, SearchByDate, GetInfoFromIp
from rest_framework import permissions


def login_page(request):
    """Login page logic"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "FpvAppMain/main_page.html")

    return render(request, "FpvAppMain/start_page.html")


class MainPage(APIView):
    """Main page logic"""

    @staticmethod
    def get(request):
        """Main page logic get  req"""
        logic_set = DataForPage(request.user)
        data = logic_set.data()

        #ip = request.META.get('REMOTE_ADDR')
        ip = '85.209.89.166'
        api_logic = GetInfoFromIp(ip)

        return render(request, 'FpvAppMain/main_page.html', {'data': data, 'api_data': api_logic.make_req_ip})


class LessonsPage(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """LessonsPage logic"""

    @staticmethod
    def get(request):  # pylint: disable=too-few-public-methods
        """LessonsPage logic get req"""

        like = request.GET.get('like')
        dislike = request.GET.get('dislike')
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

        search_by_date = request.GET.get('date_btn')

        if search_by_date:
            date = request.GET.get('date')
            logic = SearchByDate(date=date, username=request.user)
            return render(request, 'FpvAppMain/lessons_page.html', logic.create_data_set)

        if dislike:
            id_topic = dislike.split()[1]
            ds = dislike.split()[0]
            logic_det = CountLikes(id_topic, None, dislike=ds)
            logic_det.repair_dislikes()
            logic = DetailInfo(id_topic).make_query()
            data = {"model": logic,
                    "flag": 1,
                    "filter": 0,
                    "letters_model": Letters.objects.filter(destination=request.user).values(),
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        # likes logic block
        if like:
            id_topic = like.split()[1]
            lk = like.split()[0]
            logic_det = CountLikes(id_topic, lk)
            logic_det.repair_likes()
            logic = DetailInfo(id_topic).make_query()
            data = {"model": logic,
                    "flag": 1,
                    "filter": 0,
                    "letters_model": Letters.objects.filter(destination=request.user).values(),
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

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
                    'filter': 1,
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        if remove_filter:
            data = {"model": LessonTopics.objects.all().values(),
                    "tags": TagsModel.objects.all().values(),
                    "flag": 0,
                    "filter": 0,
                    "letters_model": Letters.objects.filter(destination=request.user).values(),
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        if search_by_title:
            title = request.GET.get('find_by_title')
            logic = SearchByTitle(title)
            data = {"model": logic.make_query(),
                    "flag": 0,
                    "filter_name": logic.filter_name,
                    "filter": 1,
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread"))
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)

        if detail_info:
            logic = DetailInfo(detail_info).make_query()
            data = {"model": logic,
                    "user": str(LessonTopics.objects.filter(id=detail_info).values('author')[0]["author"]),
                    "flag": 1,
                    "filter": 0,
                    "count_letters": len(Letters.objects.filter(
                        destination_id=User.objects.filter(username=request.user).values('id')[0]['id'],
                        status="unread")),
                    "current_user": str(request.user),
                    "letters_model": Letters.objects.filter(destination=request.user).values(),
                    "all_comments": CommentsTableMain.objects.filter(which_lesson_topic=detail_info).values()
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)
        logic_set = DataForPage(request.user)
        data = logic_set.data()
        return render(request, 'FpvAppMain/lessons_page.html', data)

    @staticmethod
    def post(request):
        """function for post request in lessons page"""

        rewrite_article = request.POST.get('rewrite_article')
        save_article = request.POST.get('save_article')
        send_letters = request.POST.get('send_letters')
        rewrite_video_btn = request.POST.get('rewrite_video_btn')
        rewrite_photo = request.POST.get("rewrite_photo")
        comment_btn = request.POST.get('comment_btn')
        respond_comment = request.POST.get('respond_comment')

        if respond_comment:
            text = request.POST.get('respond_text')
            username = request.user
            id_topic = CommentsTableMain.objects.filter(id=respond_comment).values("which_lesson_topic")[0][
                'which_lesson_topic']
            logic = CreateResponseComment(user=username, text=text, id_comment=respond_comment,
                                          id_topic=id_topic)
            logic.create_response_message  # creating respond
            logic.create_ringing_letter  # creating ringing about new message
            data = logic.data_set

            return render(request, 'FpvAppMain/lessons_page.html', data)

        if comment_btn:
            text = request.POST.get('comment_text')
            username = request.user
            logic = CreateComments(comment_btn, username, text)
            logic.create_comment
            return render(request, 'FpvAppMain/lessons_page.html', logic.create_data_set)

        if rewrite_photo:
            rewrite_photo_set = {}
            for el in range(5):
                try:
                    photo = request.FILES[f"rewrite_pic_{el}"]
                    rewrite_photo_set[f"pic_{el}"] = photo
                except Exception as ex:
                    print(ex)
            logic = RewriteArticle(rewrite_photo, video=None, pic=rewrite_photo_set, current_user=str(request.user))
            logic.update_pic
            return render(request, 'FpvAppMain/lessons_page.html', logic.create_data_set())

        if rewrite_video_btn:
            vd = request.FILES['rewrite_video']
            DetailInfo(rewrite_video_btn).make_query()
            logic = RewriteArticle(rewrite_video_btn, vd, current_user=str(request.user))
            logic.update_video()

            return render(request, 'FpvAppMain/lessons_page.html', logic.create_data_set())

        if rewrite_article:
            # rewrite block
            title = request.POST.get('rewrite_title')
            text = request.POST.get('rewrite_text')
            text_1 = request.POST.get('rewrite_text_1')
            text_2 = request.POST.get('rewrite_text_2')
            text_3 = request.POST.get('rewrite_text_3')
            text_4 = request.POST.get('rewrite_text_4')

            data_for_rewrite = {}
            data_set = {'title': title,
                        'text': text, 'text_1': text_1, 'text_2': text_2,
                        'text_3': text_3, 'text_4': text_4}

            for key, value in data_set.items():
                if all([value != '', value != False]):
                    data_for_rewrite[key] = value

            for key_data, value_data in data_for_rewrite.items():
                if key_data == 'title':
                    LessonTopics.objects.filter(id=rewrite_article).update(tittle=value_data)
                if key_data == 'text':
                    LessonTopics.objects.filter(id=rewrite_article).update(text=value_data)
                if key_data == 'text_1':
                    LessonTopics.objects.filter(id=rewrite_article).update(text_1=value_data)
                if key_data == 'text_2':
                    LessonTopics.objects.filter(id=rewrite_article).update(text_2=value_data)
                if key_data == 'text_3':
                    LessonTopics.objects.filter(id=rewrite_article).update(text_3=value_data)
                if key_data == 'text_4':
                    LessonTopics.objects.filter(id=rewrite_article).update(text_4=value_data)

            data = {"model": LessonTopics.objects.filter(id=rewrite_article),
                    "flag": 1,
                    "filter": 0,
                    "count_letters": len(Letters.objects.filter(status="unread")),
                    }
            return render(request, 'FpvAppMain/lessons_page.html', data)
            # =============

        if send_letters:
            send_letters = request.POST.get
            username = request.POST.get('username')
            text_letters = request.POST.get('text_letters')
            title_letters = request.POST.get('title_letters')

            if all([title_letters, send_letters, username]):
                username = User.objects.filter(username=username).values()[0]["id"]
                current_username = request.user
                logic = CreatingLetter(username, title_letters, text_letters, current_username)

                return render(request, 'FpvAppMain/lessons_page.html', logic.create_letter)

        if save_article:
            title = request.POST.get('title')
            photo_set = []
            video = None
            if request.POST.get('video'):
                video = request.FILES['video']
            photo = request.POST.get('photo')
            for el in range(int(photo)):
                num = el + 1
                pic = request.FILES[f"pic_{num}"]
                photo_set.append(pic)
            add_date = request.POST.get('add_date')
            text = request.POST.get('text')
            text_1 = request.POST.get('text_1')
            text_2 = request.POST.get('text_2')
            text_3 = request.POST.get('text_3')
            text_4 = request.POST.get('text_4')
            tag_1 = request.POST.get('tag_1')
            tag_2 = request.POST.get('tag_2')
            tag_3 = request.POST.get('tag_3')
            tag_4 = request.POST.get('tag_4')
            tag_5 = request.POST.get('tag_5')
            author = request.user

            create_article = LessonsPagePost(title, photo_set, video, photo, add_date, text, text_1, text_2, text_3,
                                             text_4,
                                             tag_1, tag_2, tag_3, tag_4, tag_5, author)

            return render(request, 'FpvAppMain/lessons_page.html', create_article.create_article)

        return render(request, 'FpvAppMain/lessons_page.html')
