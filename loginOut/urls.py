"""loginOut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import loginOut.views

urlpatterns = [
    url(r'^articles/',include('login.urls')),
    url(r'^accounts/',include('userProfile.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', loginOut.views.login),
    url(r'^accounts/logout/$', loginOut.views.logout),
    url(r'^accounts/auth/$', loginOut.views.auth_view),
    url(r'^accounts/loggedin/$',loginOut.views.loggedin),
    url(r'^accounts/invalid/$', loginOut.views.invalid_login),
    url(r'^accounts/register/$',loginOut.views.register_user),
    url(r'^accounts/register_success/$',loginOut.views.register_success),
]
