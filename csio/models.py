from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(_('Data urodzenia'), blank=True, null=True)
    photo = models.ImageField(_('Zdjęcie'), upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return _('Profil użytkownika {}.').format(self.user.username)
