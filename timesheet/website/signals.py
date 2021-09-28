from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from website.models.logEntry import LogEntry
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def on_login(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    logger.warning(LogEntry(action='on_login', ipAddress=ip, user=user.username))

@receiver(user_logged_out)
def on_logout(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    logger.warning(LogEntry(action='on_logout', ipAddress=ip, user=user.username))

# @receiver(user_login_failed)
# def on_login_fail(sender, credentials, **kwargs):
#     logger.warning(LogEntry(action='on_login_fail', user=credentials.get('username', None)))