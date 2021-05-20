# импорт пакета datetime для расчета времени и даты внесенных изменений на сайте администрации
# import of the datetime package to calculate the time and date of the changes made on the administration website
import datetime
from django.contrib import admin
# импорт метода send_activation_notification для повторной отправки с сайта администрации уведомлений активации
# import of the send_activation_notification method to resend activation notifications from the administration site
from account.utilities import send_activation_notification
from account.models import Profile


# метод для отправки писем пользователям, которые не прошли активацию
# method for sending emails to users who did not pass activation
def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
        modeladmin.message_user(request, 'requirement letters sent')


send_activation_notifications.short_description = 'sending activation requests'


# класс для фильтрации пользователей прошедших и не прошедших активацию
# class for filtering users who passed and did not pass activation
class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Activated?'
    parameter_name = 'actstate'

    # метод возвращающий перечень доступных для выбора значений, по которым будет выполняться фильтрация
    # method that returns a list of values available for selection, by which filtering will be performed
    def lookups(self, request, model_admin):
        return ('activated', 'done'), ('threedays', '3 days'), ('week', 'week')

    # метод, вызываемый после щелчка пользователя на одном из значений и возвращающий соответствующим образом отфильтрованный набор записей
    # a method that is called after the user clicks on one of the values and returns an appropriately filtered recordset
    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


# list_display - атрибут, задает набор выводимых в списке полей
# search_fields - атрибут, указывает перечень полей модели, по которым будет выполняться фильтрация записей
# list_filter - атрибут, указывает перечень полей, по которым можно будет выполнять быструю фильтрацию
# fields - атрибут, задает последовательность (список или кортеж) имен полей, выводимых в форме
# actions - регистрация действий в модели


# класс представления информации о пользователях на странице администрации
# class for presenting information about users on the administration page
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('is_active', 'is_activated'),
              ('is_staff', 'is_superuser'), 'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)


# регистрация модели Profile на странице администрации сайта
# registering the Profile model on the site administration page
admin.site.register(Profile, ProfileAdmin)
