from django.conf.urls import url
from find_your_psychiatrist.users.views import *


urlpatterns = [
    url(r'^$', UserListView.as_view()),
]
