"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    # include('pybo.urls') 로 써줌으로써 pybo/ 로 시작 되는 페이지 요청은 모두
    # pybo/urls.py 파일에 있는 URL 매핑을 참고하여 처리하라는 의미
    path('common/', include('common.urls')),
    # common/으로 시작하는 URL은 모두 common/urls.py 파일을 참조할 것임.
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
