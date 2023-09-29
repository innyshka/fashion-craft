from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from catalog.models import (
    Clothing,
    Designer,
    Size,
    Material,
    ClothingType
)


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "clothing_type")
    list_filter = ("clothing_type",)
    search_fields = ("name",)


@admin.register(Designer)
class DesignerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("pseudonym",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "pseudonym",
                )
            }
        ),
    )


admin.site.register(Size)
admin.site.register(ClothingType)
admin.site.register(Material)
admin.site.unregister(Group)

