from django.conf.urls import url
from basic_app import views

# template taging
app_name = 'basic_app'

urlpatterns = [
  url(r'^$', views.home, name="home"),
  url(r"^login/", views.user_login, name="user_login"),
  url(r"^register/", views.register, name="register"),
]
