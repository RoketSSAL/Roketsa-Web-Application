from django.urls import path
from .views import MailingListAddView, MailingListRemoveView

urlpatterns = [
    path("add", MailingListAddView),
    path("remove", MailingListRemoveView),
]
