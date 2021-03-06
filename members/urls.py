from django.conf.urls import include, url

from .views import list, add, modify
from .views import roles, r_add, r_modify, r_remove, r_type
from .views import profile, p_modify


urlpatterns = [
  url(r'^$', list, name='list'),
  url(r'^add/', add, name='add'),
  url(r'^modify/(?P<mem_id>.+?)/$', modify, name='modify'),

  url(r'^roles/$', roles, name='roles'),
  url(r'^roles/add/$', r_add, name='role_add'),
  url(r'^roles/modify/(?P<role_id>.+?)/$', r_modify, name='role_modify'),
  url(r'^roles/remove/(?P<role_id>.+?)/$', r_remove, name='role_remove'),
  url(r'^roles/type/$', r_type, name='role_type_add'),

  url(r'^profile/modify/(?P<username>.+?)/$', p_modify, name='profile_modify'),
  url(r'^profile/(?P<username>.+?)/$', profile, name='profile'),
]
