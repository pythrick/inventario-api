from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from inventario import models


@admin.register(models.Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    list_display = ("name", "email", "created_at")
    readonly_fields = ("id", "last_login", "created_at", "updated_at")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("id", "name", "email")
    ordering = ("name",)

    fieldsets = (
        (None, {"fields": ("id", "email", "password")}),
        (_("Informações Pessoais"), {"fields": ("name",)}),
        (_("Permissões"), {"fields": ("is_active", "is_staff", "is_superuser"),}),
        (
            _("Datas importantes"),
            {"fields": ("last_login", "created_at", "updated_at")},
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2"),}),
    )
