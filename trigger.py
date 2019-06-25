#!/user/bin/python3

from libs import txftp, mtime, argp
from time import sleep

if __name__ == "__main__":
    #sleep(10)
    ipaddr, user, passwd, tdir, tfilename, max_min, max_sec, max_id = argp.struct_args()

    trigger_filename = mtime.trigger_datetime()
    print(trigger_filename)

    # Create FTP Instance
    ftp_ins = txftp.ftp_init(ipaddr)

    #ftp_login(ftp_ins, 'ftpuser', 'p@ssword123')
    txftp.ftp_login(ftp_ins, user, passwd)
    txftp.ftp_cwd(ftp_ins, tdir)
    txftp.ftp_transfer(ftp_ins, tfilename)
    txftp.ftp_rename(ftp_ins, tfilename, trigger_filename)

    txftp.ftp_logout(ftp_ins)