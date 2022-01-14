import textwrap

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import SearchForm
from .models import News
from django.views.generic import DetailView
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.




class Index(View):

    def get(self, request, *args, **kwargs):
        main_news = News.objects.exclude(type__startswith='Слайдер').order_by('-id')[:4]
        bottom_news = News.objects.exclude(type__startswith='Слайдер').exclude(id=1).order_by('-id')[4:]
        slider_finances = News.objects.filter(type="Слайдер_Финансы")
        slider_finances_text = slider_finances[0].content[:280]+'...'
        slider_politics = News.objects.filter(type="Слайдер_Политика")
        slider_politics_text = slider_politics[0].content[:280] + '...'
        slider_sport = News.objects.filter(type="Слайдер_Спорт")
        slider_sport_text = slider_sport[0].content[:280] + '...'
        slider_chelyabinsk = News.objects.filter(type="Слайдер_Челябинск")
        slider_chelyabinsk_text = slider_chelyabinsk[0].content[:280] + '...'
        slider_covid = News.objects.filter(type="Слайдер_COVID-19")
        slider_covid_text = slider_covid[0].content[:280] + '...'

        form = SearchForm()

        return render(request, 'main/index.html', {'main_news': main_news, 'slider_finances': slider_finances,
                                                   'bottom_news': bottom_news, 'form': form,
                                                   'slider_finances_text': slider_finances_text,
                                                   'slider_politics': slider_politics, 'slider_politics_text': slider_politics_text,
                                                   'slider_sport': slider_sport, 'slider_sport_text': slider_sport_text,
                                                   'slider_chelyabinsk': slider_chelyabinsk, 'slider_chelyabinsk_text': slider_chelyabinsk_text,
                                                   'slider_covid': slider_covid, 'slider_covid_text': slider_covid_text})


    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all().exclude(type__startswith='Слайдер')
            for element in another_array:
                if (search.lower() in element.title.lower()):
                    searched_news.append(element)



            searched_news_main = searched_news[:4]
            searched_news_bottom = searched_news[4:]


            return render(request, 'main/search_result_page.html', {'searched_news_main':searched_news_main,
                                                                    'searched_news_bottom':searched_news_bottom})

        else:
            main_news = News.objects.exclude(type__startswith='Слайдер').order_by('-id')[:4]
            bottom_news = News.objects.exclude(type__startswith='Слайдер').exclude(id=1).order_by('-id')[4:]
            slider_finances = News.objects.filter(type="Слайдер_Финансы")
            slider_finances_text = slider_finances[0].content[:300] + '...'
            slider_politics = News.objects.filter(type="Слайдер_Политика")
            slider_politics_text = slider_politics[0].content[:300] + '...'
            slider_sport = News.objects.filter(type="Слайдер_Спорт")
            slider_sport_text = slider_sport[0].content[:300] + '...'
            slider_chelyabinsk = News.objects.filter(type="Слайдер_Челябинск")
            slider_chelyabinsk_text = slider_chelyabinsk[0].content[:300] + '...'
            slider_covid = News.objects.filter(type="Слайдер_COVID-19")
            slider_covid_text = slider_covid[0].content[:300] + '...'

            form = SearchForm()

            return render(request, 'main/index.html', {'main_news': main_news, 'slider_finances': slider_finances,
                                                       'bottom_news': bottom_news, 'form': form,
                                                       'slider_finances_text': slider_finances_text,
                                                       'slider_politics': slider_politics,
                                                       'slider_politics_text': slider_politics_text,
                                                       'slider_sport': slider_sport,
                                                       'slider_sport_text': slider_sport_text,
                                                       'slider_chelyabinsk': slider_chelyabinsk,
                                                       'slider_chelyabinsk_text': slider_chelyabinsk_text,
                                                       'slider_covid': slider_covid,
                                                       'slider_covid_text': slider_covid_text})





class ArticleDetailView(DetailView):
    model = News
    template_name = 'main/article_view.html'
    context_object_name = 'article'



class FinancesPage(View):

    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(type='Финансы').order_by('-id')[:4]
        bottom_news = News.objects.filter(type='Финансы').order_by('-id')[4:]
        form = SearchForm()


        return render(request, 'main/finances_page.html', {'main_news': main_news, 'bottom_news': bottom_news,
                                                       'form': form})


    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all()
            for element in another_array:
                if (search in element.title):
                    searched_news.append(element)



            return render(request, 'main/search_result_page.html', {'searched_news':searched_news})

        else:
            main_news = News.objects.filter(type='Финансы').order_by('-id')[:4]
            bottom_news = News.objects.filter(type='Финансы').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/finances_page.html',
                          {'main_news': main_news, 'bottom_news': bottom_news, 'form': form})


class PoliticsPage(View):

    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(type='Политика').order_by('-id')[:4]
        bottom_news = News.objects.filter(type='Политика').order_by('-id')[4:]
        form = SearchForm()


        return render(request, 'main/politics_page.html', {'main_news': main_news, 'bottom_news': bottom_news, 'form': form})


    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all()
            for element in another_array:
                if (search in element.title):
                    searched_news.append(element)



            return render(request, 'main/search_result_page.html', {'searched_news':searched_news})

        else:
            main_news_politics = News.objects.filter(type='Политика').order_by('-id')[:4]
            bottom_news_politics = News.objects.filter(type='Политика').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/politics_page.html',
                          {'main_news': main_news_politics, 'bottom_news': bottom_news_politics, 'form': form, 'head':head})

class SportPage(View):

        def get(self, request, *args, **kwargs):
            main_news = News.objects.filter(type='Спорт').order_by('-id')[:4]
            bottom_news = News.objects.filter(type='Спорт').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/sport_page.html',
                          {'main_news': main_news, 'bottom_news_politics': bottom_news,
                           'form': form})

        def post(self, request, *args, **kwargs):
            form = SearchForm(request.POST)
            if form.is_valid():
                search = form.save()
                searched_news = []
                another_array = News.objects.all()
                for element in another_array:
                    if (search in element.title):
                        searched_news.append(element)

                return render(request, 'main/search_result_page.html', {'searched_news': searched_news})

            else:
                main_news = News.objects.filter(type='Спорт').order_by('-id')[:4]
                bottom_news = News.objects.filter(type='Спорт').order_by('-id')[4:]
                form = SearchForm()


                return render(request, 'main/sport_page.html',
                              {'main_news': main_news, 'bottom_news': bottom_news,
                               'form': form})


class NewsPage(View):

    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(type='Новости').order_by('-id')[:4]
        bottom_news = News.objects.filter(type='Новости').order_by('-id')[4:]
        form = SearchForm()


        return render(request, 'main/news_page.html',
                      {'main_news': main_news, 'bottom_news_politics': bottom_news,
                       'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all()
            for element in another_array:
                if (search in element.title):
                    searched_news.append(element)

            return render(request, 'main/search_result_page.html', {'searched_news': searched_news})

        else:
            main_news = News.objects.filter(type='Новости').order_by('-id')[:4]
            bottom_news = News.objects.filter(type='Новости').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/news_page.html',
                          {'main_news': main_news, 'bottom_news': bottom_news,
                           'form': form})

class ChelyabinskPage(View):

    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(type='Челябинск').order_by('-id')[:4]
        bottom_news = News.objects.filter(type='Челябинск').order_by('-id')[4:]
        form = SearchForm()


        return render(request, 'main/chelyabinsk_page.html',
                      {'main_news': main_news, 'bottom_news_politics': bottom_news,
                       'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all()
            for element in another_array:
                if (search in element.title):
                    searched_news.append(element)

            return render(request, 'main/search_result_page.html', {'searched_news': searched_news})

        else:
            main_news = News.objects.filter(type='Челябинск').order_by('-id')[:4]
            bottom_news = News.objects.filter(type='Челябинск').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/chelyabinsk_page.html',
                          {'main_news': main_news, 'bottom_news': bottom_news,
                           'form': form})

class CovidPage(View):



    def get(self, request, *args, **kwargs):
        main_news = News.objects.filter(type='COVID-19').order_by('-id')[:4]
        bottom_news = News.objects.filter(type='COVID-19').order_by('-id')[4:]
        form = SearchForm()


        return render(request, 'main/covid_page.html',
                      {'main_news': main_news, 'bottom_news_politics': bottom_news,
                       'form': form})

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            searched_news = []
            another_array = News.objects.all()
            for element in another_array:
                if (search in element.title):
                    searched_news.append(element)

            return render(request, 'main/search_result_page.html', {'searched_news': searched_news})

        else:
            main_news = News.objects.filter(type='COVID-19').order_by('-id')[:4]
            bottom_news = News.objects.filter(type='COVID-19').order_by('-id')[4:]
            form = SearchForm()


            return render(request, 'main/covid_page.html',
                          {'main_news': main_news, 'bottom_news': bottom_news,
                           'form': form})