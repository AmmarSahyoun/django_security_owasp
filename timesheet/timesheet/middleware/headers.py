from django.utils.deprecation import MiddlewareMixin

class SecureHeaders(MiddlewareMixin):
    def process_response(self, request, response):
        response['Server'] = "None"
        response['Content-Security-Policy'] = "script-src 'self'"
        return response