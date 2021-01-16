from django.urls import path
from . import views

app_name='app5'
urlpatterns=[
    path('register/',views.register,name='registeration'),
    path('login/',views.user_login,name='user_login'),
]
