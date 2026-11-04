from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class BootstrapFormMixin:
    def _style_fields(self):
        for field in self.fields.values():
            css = "form-control"
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                css = "form-select"
            field.widget.attrs["class"] = f"{field.widget.attrs.get('class', '')} {css}".strip()


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style_fields()


class ProfileUpdateForm(BootstrapFormMixin, forms.ModelForm):
    # "role" is left out on purpose so users can't promote themselves
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style_fields()