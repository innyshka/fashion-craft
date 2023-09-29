from django.urls import path
from catalog.views import (
    index,
    ClothingTypeListView,
    ClothingTypeCreateView,
    ClothingTypeUpdateView,
    ClothingTypeDeleteView,

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




]
app_name = "catalog"
