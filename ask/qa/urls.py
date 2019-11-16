from ask.qa.views import test


urlpatterns = patterns('ask.qa.views',
    url(r'^$', test)
)
