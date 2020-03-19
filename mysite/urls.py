"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# 인터넷 페이지는 고유한 url을 갖고 있다. 애플리케이션은 사용자가 url을 입력하면
# 어떤 내용을 보여줘야 하는지 알고 있어야 함
# 장고는 urlconf를 사용. urlconf는 장고에서 url과 일치하는 뷰를 찾기위한 패턴들의 집합
# #

from django.contrib import admin
from django.urls import path, include

# 장고는 admin/ 로시작하는 모든 url을 view와 대조해서 찾아낸다
# 무수히 많은 url이 admin url에 포함될 수 있어 일일이 모두 쓸 수 없음
# 그래서 정규표현식을 사용#

# mysite/urls.py 를 깨끗한 상태로 만들기 위해 blog 애플리케이션에서
# 메인 mysite/urls.py 파일로 url들을 가져올 것#

# blog.urls(blog/urls.py) 가져오기#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
]
