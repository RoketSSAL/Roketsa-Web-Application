from django.urls import path, include
from .views import IndexView, ChangeThemeView

urlpatterns = [
    path("", IndexView, name="home"),
    path("change_theme/", ChangeThemeView),
    path("mailing_list/", include("news.urls")),
]
