from django.conf.urls import url

import userProfile.views

urlpatterns = [
    url(r'^profile/', userProfile.views.user_profile),
]
