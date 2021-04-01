import datetime
from time import strftime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        # Now = now.strftime('%H:%M')
        # ans = Now.split(':')
        ans = [now.hour, now.minute]
        return ans

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        # Now = now.strftime('%H:%M')
        ans = [now.day, now.month, now.year]
        return ans
    
    """@staticmethod
    def get_year():
        now = datetime.datetime.now()
        # Now = now.strftime('%H:%M')
        ans = now.year()
        return ans"""