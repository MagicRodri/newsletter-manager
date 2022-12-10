from django.urls import path
from .views import ClientList, ClientDetail,NewsletterList, NewsletterDetail,MessageList,MessageDetail

urlpatterns = [
    path('',NewsletterList.as_view()),
    path('<int:pk>/',NewsletterDetail.as_view()),
    path('client/', ClientList.as_view() ),
    path('client/<int:pk>/', ClientDetail.as_view()),   
    path('message/', MessageList.as_view() ),
    path('message/<int:pk>', MessageDetail.as_view() ),
]
