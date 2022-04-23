from django.urls import path
from . import views
urlpatterns = [
    path('make_list/', views.MakeList.as_view()),
    path('auto_list/', views.AutoList.as_view()),

    path('make_detail/<int:pk>/', views.MakeDetail.as_view()),
    path('auto_detail/<int:pks>/', views.AutoDetail.as_view()),
    path('auto_detail/<slug:slugify>/', views.AutoDetail.as_view()),

    path('form/', views.FormExView.as_view()),


]
