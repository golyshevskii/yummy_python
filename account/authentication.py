# импорт модели Profile для поиска пользователя в базе данных
# importing the Profile model to find a user in the database
from account.models import Profile
# унаследование методов класса BaseBackend
# inheritance of methods of the BaseBackend class
from django.contrib.auth.backends import BaseBackend


# авторизация пользователя с помощью email
# user authorization using email
class EmailAuthBackend(BaseBackend):
    # переопределение метода authenticate добавление проверки на валидность email + password
    # overriding the authenticate method adding a check for the validity of email + password
    def authenticate(self, request, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            # получение пользователя относительно введенного email или username
            # getting the user relative to the entered email or username
            user = Profile.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except Profile.DoesNotExist:
            return None

    # получения пользователя из базы данных относительно его id
    # getting a user from the database relative to his id
    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
