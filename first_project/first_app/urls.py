from django.conf.urls import url
from first_app import views

# template taging
app_name = 'first_app'

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r"^help/", views.help, name="help"),
  url(r"^users/", views.users, name="users"),
  url(r'^home/', views.home, name="home"),
  url(r'^formpage/', views.form_name_view, name="form_page"),
]
