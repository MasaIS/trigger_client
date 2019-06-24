#!/user/bin/python3

import os
import glob
import ftplib

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

def ftp_transfer(ftp):
    """ Transfer file to FTP server
        
        Arguments :
         ftp: FTP class instance
        Returns :
         none

    """
    try:
        tx_file = os.path.join(os.getcwd() + '\\triggers\\temp.tmp')
        #print(tx_file)        
        with open(tx_file, 'rb') as fp:
            res = ftp.storbinary('STOR ' + os.path.basename(tx_file), fp)
            print('FTP transfer:', res)

    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()

def ftp_rename(ftp):
    """ Rename temporary file at FTP server

        Arguments :
         ftp: FTP class instace

        Returns :
         none
         
    """


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

# Create FTP Instance
ftp_ins = ftplib.FTP('192.168.31.1')

ftp_login(ftp_ins, 'gnss', 'gnss4600')
ftp_cwd(ftp_ins, 'trig')
ftp_transfer(ftp_ins)

ftp_logout(ftp_ins)
