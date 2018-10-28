from django.conf.urls import url
from chatbot import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'^returnAnswer/$', views.returnAnswer, name='returnAnswer'),
    #url(r'^answer/', views.returnAnswer, name='answer'),
    path('', views.returnAnswer, name='returnAnswer'),
]
