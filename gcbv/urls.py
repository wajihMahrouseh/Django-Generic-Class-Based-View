from django.urls import path
from . import views
urlpatterns = [
    path('make_list/', views.MakeList.as_view()),
    path('auto_list/', views.AutoList.as_view()),
]
