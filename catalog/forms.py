from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from catalog.models import Size, Designer, Clothing


class ByNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class DesignerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = "__all__"


class DesignerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Designer
        fields = UserCreationForm.Meta.fields + (
            "pseudonym",
            "first_name",
            "last_name",
        )


class DesignerUpdateForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = ("first_name", "last_name", "pseudonym", "username")


class ClothingForm(forms.ModelForm):
    designer = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Clothing
        fields = "__all__"
