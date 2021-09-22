import datetime

class LogEntry:
    def __init__(self, action, user='', ipAddress=''):
        self.action = action
        self.ipAddress = ipAddress
        self.user = user

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.ipAddress, self.user)