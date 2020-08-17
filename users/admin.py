from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('id','phone', 'nickname')
    list_filter = ('phone', 'is_staff')
    fieldsets = (
        (None, {"fields": ('phone', 'password'),}),
        ("Personal info", {"fields": ('nickname', 'email','avatar', 'uin',
                        'first_name', 'last_name', 'birth_date',
                        'created_at', 'gender', 'like', 'dislike',
                        'last_online')}),
        ("Permissions", {"fields": ('is_moder', 'is_staff', 'is_active')})
    )
    readonly_fields = ('created_at', )

    def rating(self, obj):
        return obj.rating()


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}
            ),
    )

    search_fields = ('phone',)
    ordering = ('phone',)

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(UserAdmin).get_inline_instances(request, obj=obj)

admin.site.register(User, UserAdmin)
admin.site.register(history)
admin.site.register(PhoneOTP)

