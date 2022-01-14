from django.template.defaulttags import url
from django.urls import path, re_path
from . import views
from .views import Index, FinancesPage, PoliticsPage, ArticleDetailView, SportPage, NewsPage, ChelyabinskPage, CovidPage

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('finances', FinancesPage.as_view(), name='finances'),
    path('politics', PoliticsPage.as_view(), name='politics'),
    path('sport', SportPage.as_view(), name='sport'),
    path('news', NewsPage.as_view(), name='news'),
    path('chelyabinsk', ChelyabinskPage.as_view(), name='chelyabinsk'),
    path('covid', CovidPage.as_view(), name='covid')
]