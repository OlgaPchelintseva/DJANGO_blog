# прослойка проверяет блокировку пользователя и если пользователь заблокирован, не пропускает дальше и вызывает логаут
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

class BlockCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = getattr(request.user, 'profile', None)
            if profile and profile.is_curently_blocked():
                if profile.blocked_untill:
                    date_str = profile.blocked_untill.strftime('%d.%m.%Y %H:%i')
                    messages.error(request, f'Ваш аккаунт заблокирован до {date_str}')
                else:
                    messages.error(request, f'Ваш аккаунт заблокирован навсегда')
                logout(request)
                return redirect('login')
            return self.get_response(request)
                