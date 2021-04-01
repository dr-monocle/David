import datetime
from time import strftime
import core.info


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


class NameInfo:
    def __init__(self):
        pass

    @staticmethod
    def set_name(name):
        try:
            data.name = name
            return 'Action completed successfuly!'
        
        except:
            return 'I could not set your name. Please try again.'
        
    @staticmethod
    def get_name():
        data = info.name
              
        return data

