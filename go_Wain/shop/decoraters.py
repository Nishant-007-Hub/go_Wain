from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User


def only_superuser_allow(function):

    def wrap(request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    return wrap