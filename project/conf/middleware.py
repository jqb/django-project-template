import re

from django.conf import settings
from django.views.static import serve


class _BaseStaticServe(object):
    url = None
    root = None
    regex_ptr = r'^%s(?P<path>.*)$'

    @property
    def regex_string(self):
        return self.regex_ptr % self.url.lstrip('/')

    @property
    def regex(self):
        if not hasattr(self, '_regex'):
            self._regex = re.compile(self.regex_string)
        return self._regex

    def process_request(self, request):
        if settings.DEBUG:
            path = request.path.lstrip('/')
            match = self.regex.search(path)
            if match:
                return serve(request, match.group(1), self.root, show_indexes=True)


class StaticServe(_BaseStaticServe):
    url = settings.STATIC_URL
    root = settings.STATIC_ROOT


class MediaServe(_BaseStaticServe):
    url = settings.MEDIA_URL
    root = settings.MEDIA_ROOT
