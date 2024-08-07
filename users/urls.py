from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.urls import path, reverse_lazy
from django.views.decorators.cache import cache_page
from users.apps import UsersConfig
from users.services import email_verification
from users.views import RegisterView, ProfileView, UserDetailView, UserListView, UserUpdateView

app_name = UsersConfig.name


urlpatterns = [
    # Сервис пользователя
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirm/<str:token>', email_verification, name='email-confirm'),

    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',
                                                        email_template_name='users/password_reset_email.html',
                                                      success_url=reverse_lazy('users:password_reset_done')),
                                                        name='password_reset'),

    path('password-reset/done/', PasswordResetView.as_view(template_name='users/password_reset_done.html'),
                                                        name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                                                              success_url=reverse_lazy('users:login')), name='password_reset_confirm'),
    # Сервис менеджера
    path('user_list', cache_page(60)(UserListView.as_view(template_name='manager/user_list.html')), name='user_list'),
    path('user/<int:pk>/', cache_page(60)(UserDetailView.as_view(template_name='manager/user_info.html')), name='user_info'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update')
]