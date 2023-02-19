from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import UserFollows

User = get_user_model()


class FollowedRelationshipCreationForm(forms.ModelForm):
    """Formulaire destiné à suivre d'autres utilisateurs."""

    followed_user = forms.CharField(
        label="Utilisateur à suivre", required=True
    )

    class Meta:
        model = UserFollows
        fields = ("user",)
        widgets = {
            "user": forms.HiddenInput(),
        }

    def clean_followed_user(self):
        """Valide que l'utilisateur à suivre existe."""
        followed_user = self.cleaned_data.get("followed_user")
        try:
            user = User.objects.get(username=followed_user)
        except User.DoesNotExist:
            raise ValidationError("L'utilisateur choisi n'existe pas !")
        return user

    def save(self, commit=True):
        """Sauve la nouvelle relation user-follower_user."""
        self.instance.followed_user = self.cleaned_data.get("followed_user")
        return super().save(commit=commit)
