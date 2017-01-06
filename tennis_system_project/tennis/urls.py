from django.conf.urls import url
from tennis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_player/$', views.add_player, name='add_player'),
    url(r'^test/$',views.test_view,name = 'test_view'),
]
