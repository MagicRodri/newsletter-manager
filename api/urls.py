from django.urls import path
from .views import ClientList, ClientDetail,NewsletterList, NewsletterDetail,MessageList,MessageDetail

urlpatterns = [
    path('',NewsletterList.as_view()),
    path('<str:pk>/',NewsletterDetail.as_view()),
    path('client/', ClientList.as_view() ),
    path('client/<str:pk>/', ClientDetail.as_view()),   
    path('message/', MessageList.as_view() ),
    path('message/<str:pk>', MessageDetail.as_view() ),
]
