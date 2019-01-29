from django.urls import path, re_path

from poll_test_app import views

app_name = 'poll_test_app'

urlpatterns = [
    path('api/polls', views.poll_list),
    path('api/polls/<int:id>', views.poll_detail),
    path('api/options', views.option_list),
    path('api/options/<slug:slug_option>', views.option_detail),
]
