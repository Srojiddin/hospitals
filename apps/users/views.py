from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from apps.users.forms import UserCreationForm, UserUpdateForm
from django.views.generic import DeleteView


User = get_user_model()


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/account.html'
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


# def logout_logics(request):
#     logout(request)
#     return redirect('login')
#
#
# def login_logics(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#
#             return redirect('is_person', user.id)
#
#         error = "Неправильный логин или пароль!"
#         return render(request, 'users/sign_in.html', locals())
#
#     return render(request, 'users/sign_in.html')
#
#
# def signup_logics(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         repassword = request.POST['repassword']
#         phone_number = request.POST['phone_number']
#
#         if password != repassword:
#             return render(request, 'users/sign_up.html', {'error': "Пароли не совподают!"})
#
#         if User.objects.filter(username=username).exists():
#             return render(request, 'users/sign_up.html', {'error': "Такой пользователь уже есть!"})