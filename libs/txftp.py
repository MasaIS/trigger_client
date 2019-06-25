
import os
import ftplib


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
        return ins

    except ftplib.all_errors as err:
        print('FTP error:', err)
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
        print('FTP login:', res)
        return True


    except ftplib.all_errors as err:
        print('FTP error:', err)
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
        print('FTP currnet directory:', ftp.pwd())
        #print(ftp.dir())
        res = ftp.cwd(chgdir)
        print('FTP cwd:', res)
        print('FTP changed directory:', ftp.pwd())
        return True

    except ftplib.all_errors as err:
        print('FTP error:', err)
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
        tx_file = os.path.join(os.getcwd() + "\\" + filename)
        #print(tx_file)        
        with open(tx_file, 'rb') as fp:
            res = ftp.storbinary('STOR ' + os.path.basename(tx_file), fp)
            print('FTP transfer:', res)

        return True

    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()
        return False


def ftp_rename(ftp, old_name, new_name):
    """ Rename file on FTP server

        Argument :
         ftp: FTP class instance
         filename: temporary filename
        Return :
         True or False
    """
    # rename
    try:
        # get filelist
        filelist = ftp.nlst(".")
        #print(filelist)
        for file in filelist:
            if file == old_name:
                res = ftp.rename(old_name, new_name)
                print('FTP rename:', res)
            else:
                continue
        return True

    except ftplib.all_errors as err:
        print('FTP error:', err)
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
        print('FTP logout:', res)
        return True
        
    except ftplib.all_errors as err:
        print('FTP error:', err)
        ftp.close()
        return False
