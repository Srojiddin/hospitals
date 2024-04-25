from django.views import generic
from django.contrib.auth import get_user_model
from apps.users.forms import UserCreationForm, UserUpdateForm
from django.views.generic import DeleteView


User = get_user_model()


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/index.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users_update.html'
    context_object_name = 'user'
    success_url = '/index.html'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    context_object_name = 'user'
    success_url = '/index.html'