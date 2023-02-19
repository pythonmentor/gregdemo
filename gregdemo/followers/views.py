from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FollowedRelationshipCreationForm

User = get_user_model()


class FollowersIndexView(LoginRequiredMixin, CreateView):
    form_class = FollowedRelationshipCreationForm
    success_url = reverse_lazy("followers:index")
    template_name = "followers/index.html"

    def get_form_kwargs(self):
        """Initialise le user du formullaire avec l'utilisateur connecté."""
        kwargs = super().get_form_kwargs()
        kwargs["initial"] = {"user": self.request.user}
        return kwargs

    def get_context_data(self, **kwargs):
        """Ajout de données au contexte du template."""
        context = super().get_context_data(**kwargs)
        context["followed_users"] = User.objects.filter(
            followed_by__user=self.request.user
        )
        return context


followers_index = FollowersIndexView.as_view()
