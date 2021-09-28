from django.core.exceptions import PermissionDenied
from website.models.logEntry import LogEntry
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def logged_permission_required(permission):
    def inner_function(function):
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            if request.user.has_perm(permission):
                return function(request, *args, **kwargs)
            else:
                username = None
                if request.user.is_authenticated:
                    username = request.user.username
                ip = request.META.get('REMOTE_ADDR')
                logger.warning(LogEntry(action='Authorization fail: ' + request.path, ipAddress=ip, user=username))
                raise PermissionDenied('Permission Denied!')
        return wrapper
    return inner_function