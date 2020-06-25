from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url(r'^$', views.apiOverview, name='api_overviewt'),
    url(r'^student-list/$', views.StudentList, name='student-list'),
    url(r'^student-detail/(?P<pk>\d+)/$', views.StudentDetail, name='student-detail'),
    url(r'^student-create/$', views.StudentPost, name='student-post'),
    url(r'^student-update/(?P<pk>\d+)/$', views.StudentUpdate, name='student-update'),
    url(r'^student-delete/(?P<pk>\d+)/$', views.StudentDelete, name='student-delete'),
    
    url(r'^profile-list/$', views.ProfileList, name='profile-list'),
    url(r'^profile-create/$', views.ProfilePost, name='profile-post'),

    url(r'^user-list/$', views.UserList.as_view(), name='user-list'),
    url(r'^user-register/$', views.UserRegister, name='user-register'),
    url(r'^user-login/$', obtain_auth_token, name='user-login'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
