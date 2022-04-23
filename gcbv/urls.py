from django.urls import path
from . import views

app_name = 'gcbv'

urlpatterns = [
    path('make_list/', views.MakeList.as_view(), name='make_list'),
    path('auto_list/', views.AutoList.as_view(), name='auto_list'),

    path('make_detail/<int:pk>/', views.MakeDetail.as_view(), name='make_detail'),
    path('auto_detail/<int:pks>/', views.AutoDetail.as_view(), name='auto_detail_pk'),
    path('auto_detail/<slug:slugify>/', views.AutoDetail.as_view(), name='auto_detail_slug'),

    path('form/', views.FormExView.as_view(), name='form_view'),

    path('make_create/', views.MakeCrate.as_view(), name='make_create'),
    path('auto_create/', views.AutoCrate.as_view(), name='auto_create'),

]
