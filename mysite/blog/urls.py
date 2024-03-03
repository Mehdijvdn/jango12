from django.urls import path
from . import views
from .views import post_list , post_detail

from django.views.generic import RedirectView


app_name = 'blog'

urlpatterns = [
# post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    post_detail,
    name='post_detail'),
    path ('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    ]