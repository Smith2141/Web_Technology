from django.http import HttpResponse, HttpResponseNotFound


def test(request, name):
    if name in ['root', 'login', 'signup', 'question', 'ask',
                'popular', 'new']:
        return HttpResponse('OK')
    else:
        return HttpResponseNotFound('404')
