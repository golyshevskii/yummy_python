# импорт метода render для формирования ответа пользователю
# import of the render method to form a response to the user
from django.shortcuts import render, get_object_or_404
# импорт декоратора login_required + LoginRequiredMixin для проверки авторизации пользователя
# import the login_required decorator + LoginRequiredMixin to check user authorization
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# импорт объектов для создания представления страниц
# importing objects to create page views
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth import logout
from django.core.signing import BadSignature
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from account.forms import UserRegistrationForm, UserEditForm
from account.models import Profile
# иморт экземпляра класса Signer для экономии оперативной памяти
# importing an instance of the Signer class to save RAM
from account.utilities import signer


# класс для отправки страницы входа пользователя на сайт
# class for sending the user login page to the site
class Login(LoginView):
    template_name = 'account/login.html'


# класс для отправки страницы выхода пользователя
# class for sending the user logout page
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'account/logout.html'


# метод для отправки страницы профиля авторизованному пользователю
# method to send profile page to authorized user
class Account(LoginView):
    template_name = 'account/profile.html'


# класс для представления формы при регистрации пользователя
# class for form submission during user registration
class Register(CreateView):
    model = Profile
    form_class = UserRegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:register_done')


# класс для уведомления об успешной регистрации пользователя
# class for notification of successful user registration
class RegisterDone(TemplateView):
    template_name = 'account/register_done.html'


# метод для подтверждения активации
# method to confirm activation
def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'account/bad_signature.html')
    user = get_object_or_404(Profile, username=username)
    if user.is_activated:
        template = 'account/user_is_activated.html'
    else:
        template = 'account/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


# класс представления формы для редактирования информации о пользователе
# form submission class for editing user information
class UserEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = UserEditForm
    template_name = 'account/edit.html'
    success_url = reverse_lazy('account:profile')
    success_message = 'yami! profile updated successfully'

    # метод получения индекса пользователя в базе данных
    # method for getting the user's index in the database
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    # метод извлечения исправляемого поля
    # method to retrieve the field to be corrected
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


# класс для изменения пароля пользователя
# class for changing user password
class PasswordChange(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:profile')
    success_message = 'password changed'


# класс для удаления пользователя
# class for deleting a user
class UserDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'account/delete_user.html'
    success_url = reverse_lazy('account:delete_user_done')

    # сохранение индекса пользователя
    # save user index
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    # предварительный выход из аккаунта перед удалением пользователя
    # preliminary log out of the account before deleting the user
    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)

    # метод поиска пользователя
    # user search method
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


# класс для уведомления об успешном удалении пользователя
# class for notification of successful user deletion
class UserDeleteDone(TemplateView):
    template_name = 'account/delete_user_done.html'
