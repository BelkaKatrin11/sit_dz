from django.shortcuts import render


def info(request):
    user_agent = request.META['HTTP_USER_AGENT']
    user_ip = request.META.get('REMOTE_ADDR')
    return render(request, 'base.html', {'user_agent': user_agent, 'user_ip': user_ip})
