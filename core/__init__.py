import datetime
from time import strftime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        # Now = now.strftime('%H:%M')
        ans = [now.hour, now.minute]
        return ans