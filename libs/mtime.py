from datetime import datetime, timedelta
import random, os, logging

logger = logging.getLogger(__name__)

def make_trigger_datetime(max_min=10, max_sec=59, max_id=3):
    """ Make datetime for trigger

        Arguments :
         max_min: random maximum number of minutes
         max_sec: random maximum number of seconds
         max_id: random maximum number of modules
        Returns :
         trigger_filename: trigger filename
         False: exception

    """
    try:
        # formatter datetime
        fmt = '%Y%m%d%H%M%S'
        # offset
        min_delta = random.randint(0,max_min)
        sec_delta = random.randint(0,max_sec)
        mod_id = random.randint(0,max_id)

        #make datetime
        end_dt = datetime.now()
        stt_dt = end_dt - timedelta(minutes=min_delta) - timedelta(seconds=sec_delta)

        #combined string
        trigger_filename = str(mod_id).zfill(3) + '-' + stt_dt.strftime(fmt) + '-' + end_dt.strftime(fmt) + '.tgr'
        logger.info('Make trigger filename: ' + trigger_filename)
    
        return trigger_filename

    except:
        logger.error('Something error to making trigger filename')
        return False

    
def replicate_trigger(dir_path, tgr_filename):
    """ Replicate triggr file

        Arguments :
         dir_path: Path to directory for replication
         tgr_filename: trigger filename
        Returns :
         True or False
    """
    try:
        # Make directory when nothing
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, tgr_filename), 'w'):
            pass
        logger.info('Write trigger file: ' + os.path.join(dir_path, tgr_filename))
        return True

    except FileNotFoundError as err:
        logger.error('Write error: ' + err)
        return False

    except FileExistsError as err:
        logger.error('Write error: ' + err)
        return False