#!/user/bin/python3

import os
import ftplib
import dateutil
from datetime import datetime, timedelta

def ftp_login(ftp, user, password):
    """ Login FTP server
        
        Arguments :
         ftp: FTP class instance
         user: FTP login user
         password: FTP login password
        Returns :
         none
    
    """
    try:
        ftp.login(user, password)
        print('FTP login')
        #ftp.sendcmd('TYPE I')


    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()

def ftp_cwd(ftp, chgdir):
    """ Change directory for FTP server
        
        Arguments : 
         ftp: FTP class instance
         chgdir: change directory
        Returns :
         none

    """
    try:
        print('FTP currnet directory:', ftp.pwd())
        #print(ftp.dir())
        ftp.cwd(chgdir)
        print('FTP changed directory:', ftp.pwd())

    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()

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
        tx_file = os.path.join(os.getcwd() + "\\" + filename)
        #print(tx_file)        
        with open(tx_file, 'rb') as fp:
            res = ftp.storbinary('STOR ' + os.path.basename(tx_file), fp)
            print('FTP transfer:', res)

    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()


def ftp_rename(ftp, filename):
    """ Rename file on FTP server

        Argument :
         ftp: FTP class instance
         filename: temporary filename
        Return :
         none

    """
    # rename
    try:
        # get filelist
        filelist = ftp.nlst(".")
        #print(filelist)
        for file in filelist:
            if file == filename:
                res = ftp.rename(filename, 'new.tgr')
                print('FTP rename:', res)
            else:
                continue

    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()
    



def ftp_logout(ftp):
    """ Logout FTP server
        
        Arguments :
         ftp: FTP class instance
        Returns :
         none
    
    """
    try:
        ftp.quit()
        print('FTP logout')
        
    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()


if __name__ == "__main__":
    #pass
    fmt = '%Y%m%d%H%M%S'
    stt_dt = datetime.now()
    
    print(stt_dt.strftime(fmt), type(stt_dt))




    # Create FTP Instance
    ftp_ins = ftplib.FTP('192.168.56.101')

    ftp_login(ftp_ins, 'ftpuser', 'p@ssword123')
    ftp_cwd(ftp_ins, 'trig')
    ftp_transfer(ftp_ins, 'tmp_trigger')
    ftp_rename(ftp_ins, 'tmp_trigger')

    ftp_logout(ftp_ins)
