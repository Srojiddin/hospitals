from django.urls import path

from apps.users.views import UserCreateView, UserDetailView, UserUpdateView,UserDeleteView

urlpatterns = [
    path('user/list/', UserCreateView.as_view(), name='user_list'),
    path('user/detail/', UserDetailView.as_view(), name='user_detail'),
    path('user/detail/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/', UserDeleteView.as_view(), name='user_delete')
]


