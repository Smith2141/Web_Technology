from django.http import HttpResponse


def test(request, name, *args, **kwargs):
    if name in ['root', 'login', 'signup', 'question', 'ask',
                'popular', 'new']:
        return HttpResponse('OK')
    else:
        return HttpResponse('404')
