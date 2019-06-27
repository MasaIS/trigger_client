
import os
import ftplib
import logging

logger = logging.getLogger(__name__)

def ftp_init(ipaddr, ftptimeout=60):
    """Create FTP class instance

        Arguments :
         ipaddr: IP address of FTP servier
         ftptimeout: connection timeout
        Returns :
         ins: FTP class instance

    """
    ins = False
    try:
        ins = ftplib.FTP(host=ipaddr, timeout=ftptimeout)
        logger.info('FTP connect: ' + ipaddr)
        return ins

    except ftplib.all_errors as err:
        logger.error('FTP connect error: ' + str(err))
        return ins


def ftp_login(ftp, user, password):
    """ Login FTP server
        
        Arguments :
         ftp: FTP class instance
         user: FTP login user
         password: FTP login password
        Returns :
         True or False
    
    """
    try:
        res = ftp.login(user, password)
        logger.info('FTP login: ' + res)
        return True


    except ftplib.all_errors as err:
        logger.error('FTP logine error: ' + str(err))
        ftp.close()
        return False

def ftp_cwd(ftp, chgdir):
    """ Change directory for FTP server
        
        Arguments : 
         ftp: FTP class instance
         chgdir: change directory
        Returns :
         True or False
    """
    try:
        logger.debug('FTP currnet directory: ' + ftp.pwd())
        #print(ftp.dir())
        res = ftp.cwd(chgdir)
        logger.info('FTP cwd: ' + res)
        logger.debug('FTP changed directory: ' + ftp.pwd())
        return True

    except ftplib.all_errors as err:
        logger.error('FTP cwd error: ' + str(err))
        ftp.close()
        return False


def ftp_transfer(ftp, filename):
    """ Transfer file to FTP server
        
        Arguments :
         ftp: FTP class instance
         filename: temporary filename
        Returns :
         none
    """
    # transfer temp.tmp
    try:
        tx_file = os.path.join(os.getcwd(), filename)
     
        with open(tx_file, 'rb') as fp:
            res = ftp.storbinary('STOR ' + os.path.basename(tx_file), fp)
            logger.info('FTP transfer: ' + res)

        return True

    except ftplib.all_errors as err:
        logger.error('FTP transfer error: ' + str(err))
        ftp.close()
        return False


def ftp_rename(ftp, old_name, new_name):
    """ Rename file on FTP server

        Argument :
         ftp: FTP class instance
         filename: temporary filename
        Return :
         flag: True or False
    """
    # rename
    try:
        # get filelist
        filelist = ftp.nlst(".")
        # flag to rename file
        flag = False
        for f in filelist:
            if f == old_name:
                res = ftp.rename(old_name, new_name)
                logger.info('FTP rename: ' + res)
                flag = True
                break
            else:
                flag = False
                continue
        if flag == False:
            logger.warn('FTP rename warn: ' + 'Target file is not exist.')
        return flag

    except ftplib.all_errors as err:
        logger.error('FTP rename error: ' + str(err))
        ftp.close()
        return False
    

def ftp_logout(ftp):
    """ Logout FTP server
        
        Arguments :
         ftp: FTP class instance
        Returns :
         none
    
    """
    try:
        res = ftp.quit()
        logger.info('FTP logout: ' + res)
        return True
        
    except ftplib.all_errors as err:
        logger.error('FTP logout error: ' + str(err))
        ftp.close()
        return False
