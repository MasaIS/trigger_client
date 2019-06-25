from datetime import datetime, timedelta
import random


def trigger_datetime(max_min=10, max_sec=59, max_id=3):
    """ Make datetime for trigger

        Arguments :
         max_min: random maximum number for minutes
         max_sec: random maximum number for seconds
         max_id: random maximum number for modules
        Returns :
         trigger: trigger filename

    """
    fmt = '%Y%m%d%H%M%S'
    min_delta = random.randint(0,max_min)
    sec_delta = random.randint(0,max_sec)
    mod_id = random.randint(0,max_id)

    end_dt = datetime.now()
    stt_dt = end_dt - timedelta(minutes=min_delta) - timedelta(seconds=sec_delta)
    
    #print('Start datetime:', stt_dt.strftime(fmt), type(stt_dt))
    #print('End datetime:', end_dt.strftime(fmt), type(end_dt))
    #print('During time(min):', min_delta)
    #print('During time(sec):', sec_delta)
    #print('Machine id:', mod_id)

    return str(mod_id).zfill(3) + '-' + stt_dt.strftime(fmt) + '-' + end_dt.strftime(fmt) + '.tgr'

    
