from django.http import HttpResponse


def test(request, *args, **kwargs):
    if request in ('root', 'login', 'signup', 'question', 'ask',
                   'popular', 'new'):
        return HttpResponse('OK')
    else:
        return HttpResponse('404')
