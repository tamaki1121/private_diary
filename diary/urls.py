from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('base', views.BaseView.as_view(), name="base"),
    # path('', views.index , name="index"),
]
