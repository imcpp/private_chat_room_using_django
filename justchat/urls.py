from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("search/",views.search,name='search'),
    path("profile/",views.profile,name='profile'),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path('chat/', include('chat.urls', namespace='chat')),
]
