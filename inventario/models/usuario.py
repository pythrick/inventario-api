from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from inventario.managers import UsuarioManager
from inventario.mixins import ModelMixin


class Usuario(ModelMixin, AbstractBaseUser, PermissionsMixin):
    class Meta:
        abstract = False
        app_label = "inventario"
        db_table = "usuarios"
        ordering = ("created_at",)
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    email = models.EmailField(verbose_name=_("E-mail"), unique=True)
    name = models.CharField(verbose_name=_("Nome"), max_length=150)
    is_staff = models.BooleanField(verbose_name=_("Faz parte do time?"), default=False)
    is_active = models.BooleanField(verbose_name=_("Está ativo?"), default=False)

    def __str__(self):
        return self.name

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "password",
    ]
