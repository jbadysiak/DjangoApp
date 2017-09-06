from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    #url(r'^login/$', views.user_login, name='login')
    url(_(r'^loginwithoutgoogle/$'), login, name='loginwithoutgoogle'),
    url(_(r'^login/$'), views.user_login, name='login'),
    url(_(r'^logout/$'), logout, name='logout'),
    url(_(r'^logout-then-login/$'), logout_then_login, name='logout_then_login'),
    url(_(r'^dashboard/$'), views.dashboard, name='dashboard'),
    url(_(r'^edit/$'), views.edit, name='edit'),
    url(_(r'^password-change/$'), password_change, name='password_change'),
    url(_(r'^password-change/done/$'), password_change_done, name='password_change_done'),
    url(_(r'^password-reset/$'), password_reset, name='password_reset'),
    url(_(r'^password-reset/done/$'), password_reset_done, name='password_reset_done'),
    url(_(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$'), password_reset_confirm, name='password_reset_confirm'),
    url(_(r'^password-reset/complete/$'), password_reset_complete, name='password_reset_complete'),
    url(_(r'^register/$'), views.register, name='register'),
]

