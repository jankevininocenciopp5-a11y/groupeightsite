from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.login_view),
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.edit_gender),
    path('gender/delete/<int:genderId>', views.delete_gender),
    path('user/list', views.user_list),
    path('user/add', views.add_user),
    path('user/edit/<int:userId>', views.edit_user),
    path('user/delete/<int:userId>', views.delete_user),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('user/passwordchange/<int:userId>', views.password_change),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)