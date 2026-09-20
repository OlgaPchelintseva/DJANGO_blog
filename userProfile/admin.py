from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline): # StackedInline - кода используем связи один к одному или многие ко многим
    model = Profile
    can_delete = False
    fields = ('is_moderator', 'is_blocked', 'blocked_until', 'bio', 'avatar')

class CastomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_moderator', 'is_blocked')

    def is_moderator(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.is_moderator
        return False
    
    def is_blocked(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.is_blocked
        return False
    
    is_blocked_boolean = True
    is_blocked_short_description = 'Заблокирован'

admin.site.unregister(User)
admin.site.register(User, CastomUserAdmin)