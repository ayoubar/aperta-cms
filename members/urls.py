from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required

from .forms import ListMembersForm, ModifyMemberForm, ModifyRoleForm
from .views import ModifyMemberWizard, show_role_form
from .views import index, profile, add, list
from .views import role_add

# modify wizard #
#forms
modify_member_forms = [
        ('list'         , ListMembersForm),
        ('member'       , ModifyMemberForm),
        ('role'         , ModifyRoleForm),
]
#condition dict
modify_member_condition_dict = {
	'role'		: show_role_form,
}

#view
modify_member_wizard = ModifyMemberWizard.as_view(modify_member_forms, condition_dict=modify_member_condition_dict)
#wrapper with specific permissions
modify_member_wrapper = permission_required('cms.BOARD',raise_exception=True)(modify_member_wizard)

urlpatterns = patterns('',
  url(r'^$', index, name='index'),
  url(r'^add/', add, name='add'),
  url(r'^role/add/', role_add, name='role_add'),
  url(r'^modify/', modify_member_wrapper, name='modify'),
  url(r'^list/', list, name='list'),

  url(r'^profile/(?P<username>.+?)', profile, name='profile'),
)
