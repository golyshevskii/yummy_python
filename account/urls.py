# импорт метода path для определения маршрутов
# import path method to define routes
from django.urls import path
from django.contrib.auth import views as auth_views
# импорт контроллеров для отправки ответа на запрос пользователя
# import controllers to send a response to a user request
from account.views import *


app_name = 'account'

# пути ведущие к страницам относительно заданного шаблона(запроса пользователя)
# paths leading to pages relative to the given template(user request)
urlpatterns = [
    path('delete-user/done/', UserDeleteDone.as_view(), name='delete_user_done'),  # страница успешного удаления пользователя
    path('delete-user/', UserDelete.as_view(), name='delete_user'),  # страница удаления пользователя
    path('password-change/', PasswordChange.as_view(), name='password_change'),  # страница изменения пароля
    path('edit/', UserEdit.as_view(), name='edit'),  # страница редактирования информации пользователя
    path('register/activate/<str:sign>/', user_activate, name='register_activate'),  # страница активации
    path('register/done/', RegisterDone.as_view(), name='register_done'),  # страница успешной регистрации
    path('register/', Register.as_view(), name='register'),  # страница регистрации
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),  # страница успешной смены пароля
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),  # страница смены пароля
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),  # страница об успешном запросе сброса пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),  # страница сброса пароля
    path('login/', Login.as_view(), name='login'),  # страница входа
    path('logout/', Logout.as_view(), name='logout'),  # страница выхода
    path('', Account.as_view(), name='profile'),  # страница профиля пользователя
]