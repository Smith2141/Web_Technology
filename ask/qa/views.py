from django.http import HttpResponse, HttpResponseNotFound


def test(request):
    # if name in ['root', 'login', 'signup', 'question', 'ask',
    #             'popular', 'new']:
    return HttpResponse('OK')
    # else:
    #     return HttpResponse('404')
