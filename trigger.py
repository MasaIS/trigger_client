#!/user/bin/python3

from libs import txftp, mtime, argp
from time import sleep
import sys

if __name__ == "__main__":
    #sleep(10)
    ipaddr, user, passwd, tdir, tfilename, max_min, max_sec, max_id = argp.struct_args()

    trigger_filename = mtime.make_trigger_datetime()
    print(trigger_filename)

    # Create FTP Instance
    ftp_ins = txftp.ftp_init(ipaddr,10)
    if ftp_ins == False:
        sys.exit(1)
    if txftp.ftp_login(ftp_ins, user, passwd) == False:
        sys.exit(1)
    if txftp.ftp_cwd(ftp_ins, tdir) == False:
        sys.exit(1)
    if txftp.ftp_transfer(ftp_ins, tfilename) == False:
        sys.exit(1)
    if txftp.ftp_rename(ftp_ins, tfilename, trigger_filename) == False:
        sys.exit(1)
    if txftp.ftp_logout(ftp_ins) == False:
        sys.exit(1)