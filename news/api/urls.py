from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('sites/', views.WebsiteSettingsList.as_view()),
    path('site/<pk>/', views.WebsiteSettingsDetail.as_view()),
]

