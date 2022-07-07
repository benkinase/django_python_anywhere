"""config URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


admin.site.site_header = 'Gbenimako Admin'
admin.site.site_title = 'django-anywhere-admin'
admin.site.site_url = 'http://gbenimako.com/'
admin.site.index_title = 'Main Admin Panel'
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset',),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
    path('', include("hotel.urls")),
    path('', include("store.urls")),
    path('', include("jobhunt.urls")),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    re_path(r'^.*',views.index, name='index' ),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
