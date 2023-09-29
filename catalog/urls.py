from django.urls import path
from catalog.views import (
    index,
    ClothingTypeListView,
    ClothingTypeCreateView,
    ClothingTypeUpdateView,
    ClothingTypeDeleteView,
    MaterialListView,
    MaterialCreateView,
    MaterialUpdateView,
    MaterialDeleteView,
    SizeListView,
    SizeCreateView,
    SizeUpdateView,
    SizeDeleteView,
)
urlpatterns = [
    path("", index, name="index"),
    path(
        "clothings-types/",
        ClothingTypeListView.as_view(),
        name="clothing-type-list",
    ),
    path(
        "clothings-types/create",
        ClothingTypeCreateView.as_view(),
        name="clothing-type-create",
    ),
    path(
        "clothings-types/<int:pk>/update/",
        ClothingTypeUpdateView.as_view(),
        name="clothing-type-update",
    ),
    path(
        "clothings-types/<int:pk>/delete/",
        ClothingTypeDeleteView.as_view(),
        name="clothing-type-delete",
    ),

    path(
        "materials/",
        MaterialListView.as_view(),
        name="material-list",
    ),
    path(
        "materials/create",
        MaterialCreateView.as_view(),
        name="material-create",
    ),
    path(
        "materials/<int:pk>/update/",
        MaterialUpdateView.as_view(),
        name="material-update",
    ),
    path(
        "materials/<int:pk>/delete/",
        MaterialDeleteView.as_view(),
        name="material-delete",
    ),

    path(
        "sizes/",
        SizeListView.as_view(),
        name="size-list",
    ),
    path(
        "sizes/create",
        SizeCreateView.as_view(),
        name="size-create",
    ),
    path(
        "sizes/<int:pk>/update/",
        SizeUpdateView.as_view(),
        name="size-update",
    ),
    path(
        "sizes/<int:pk>/delete/",
        SizeDeleteView.as_view(),
        name="size-delete",
    ),




]
app_name = "catalog"
