import re

from django.conf import settings
from django.views.static import serve


class _BaseStaticServe(object):
    url = None
    root = None
    regex_ptr = r'^/%s(?P<path>.*)$'

    @property
    def regex(self):
        if not hasattr(self, '_regex'):
            self._regex = re.compile(self.regex_ptr % self.url)
        return self._regex

    def process_request(self, request):
        if settings.DEBUG:
            match = self.regex.search(request.path)
            if match:
                return serve(request, match.group(1), self.root)


class StaticServe(_BaseStaticServe):
    url = settings.STATIC_URL
    root = settings.STATIC_ROOT

