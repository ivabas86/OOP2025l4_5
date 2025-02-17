from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .forms import TemplateForm
from django.views import View
from django.views.generic import TemplateView

class MyTempView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        form = TemplateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            email = form.cleaned_data.get("my_email")
            message = form.cleaned_data.get("my_message")
            # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
            # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP
            user_agent = request.META.get('HTTP_USER_AGENT')
            return JsonResponse(
                data=[text, email, message, ip, user_agent],
                safe=False, json_dumps_params={"indent": 4})
        return render(request, 'landing/index.html', context={'form': form})
