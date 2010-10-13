from django.conf.urls.defaults import *
from django.conf import settings
# from django.core.urlresolvers import reverse
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns(
    '',
    # (r'^admin/', include(admin.site.urls)),
    )


urlpatterns += patterns(
    'django.views.generic',
    (r'^$', 'simple.direct_to_template', {'template': 'project_base.html'}),
    # (r'^$', 'simple.redirect_to', {'url': ''}),
    )


if settings.DEBUG:
    urlpatterns += patterns(                                
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        )
