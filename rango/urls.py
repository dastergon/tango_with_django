from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/', views.add_page, name='add_page'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
            views.show_category, name='show_category'),
    url(r'about/', views.about, name='about'),
    url(r'^$', views.index, name='index'),
]
