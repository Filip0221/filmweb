from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from filmweb.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmweb/', include('filmweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register/", register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

