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
    DesignerListView,
    DesignerDetailView,
    DesignerCreateView,
    DesignerUpdateView,
    DesignerDeleteView,
    ClothingListView,
    ClothingDetailView,
    ClothingCreateView,
    ClothingUpdateView,
    ClothingDeleteView,
    toggle_assign_to_clothing


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

    path(
        "designer/",
        DesignerListView.as_view(),
        name="designer-list"
    ),
    path(
        "designer/<int:pk>/",
        DesignerDetailView.as_view(),
        name="designer-detail"
    ),
    path(
        "designer/create/",
        DesignerCreateView.as_view(),
        name="designer-create"
    ),
    path(
        "designer/<int:pk>/update/",
        DesignerUpdateView.as_view(),
        name="designer-update",
    ),
    path(
        "designer/<int:pk>/delete/",
        DesignerDeleteView.as_view(),
        name="designer-delete",
    ),

    path("clothes/", ClothingListView.as_view(), name="clothing-list"),
    path("clothes/<int:pk>/", ClothingDetailView.as_view(), name="clothing-detail"),
    path("clothes/create/", ClothingCreateView.as_view(), name="clothing-create"),
    path("clothes/<int:pk>/update/", ClothingUpdateView.as_view(), name="clothing-update"),
    path("clothes/<int:pk>/delete/", ClothingDeleteView.as_view(), name="clothing-delete"),
    path(
        "clothes/<int:pk>/toggle-assign/",
        toggle_assign_to_clothing,
        name="toggle-clothing-assign",
    ),
]
app_name = "catalog"
