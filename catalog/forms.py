from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Size, Designer, Clothing, Material


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
            "description"
        )


class DesignerUpdateForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = ("first_name", "last_name", "pseudonym", "username",  "description")


class ClothingForm(forms.ModelForm):
    designer = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    size = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Clothing
        fields = "__all__"


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    pseudonym = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pseudonym",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
                }
            ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta(UserCreationForm.Meta):
        model = Designer
        fields = (
            "username",
            "pseudonym",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
