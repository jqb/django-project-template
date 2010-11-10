from django.conf import settings


def conf(request):
    """
    Template context processor that provide
    CONF variable to templates.
    """
    context = {}

    for s in getattr(settings, 'TEMPLATE_SETTINGS', []):
        context[s] = getattr(settings, s)

    return context
