"""leave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from leave_manager import viewsets
from rest_framework_simplejwt import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(router.urls)),
    url(r'^api/auth/access-token/', auth_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/employee', viewsets.EmployeeViewset.as_view()),
    url(r'^api/leave', viewsets.LeaveViewset.as_view()),
    url(r'^api/auth/refresh-token/', auth_views.TokenRefreshView.as_view(), name='token_refresh_view')
]
